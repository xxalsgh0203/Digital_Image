from .interpolation import interpolation
import numpy as np
import math

class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):
        """Computes the forward rotated image by an angle theta
                image: input image
                theta: angle to rotate the image by (in radians)
                return the rotated image"""

        #find the min and max width of the final image

        rotation_matrix = np.array([[math.cos(theta), -math.sin(theta)],
                                          [math.sin(theta), math.cos(theta)]])

        corners = {"tl": np.array([0, 0]),
                   "tr": np.array([0, image.shape[1]]),
                   "bl": np.array([image.shape[0], 0]),
                   "br": np.array([image.shape[0], image.shape[1]])}

        rotate_corners = dict() # create dictionary
        min_x, min_y, max_x, max_y = np.inf, np.inf, -np.inf, -np.inf

        for i in corners:
            rotate_corners[i] = np.sum(rotation_matrix * corners[i], axis=1)
            if rotate_corners[i][0] > max_x:
                max_x = rotate_corners[i][0]
            if rotate_corners[i][0] < min_x:
                min_x = rotate_corners[i][0]
            if rotate_corners[i][1] > max_y:
                max_y = rotate_corners[i][1]
            if rotate_corners[i][1] < min_y:
                min_y = rotate_corners[i][1]

        # Size of rotated image
        row = int(max_x - min_x)
        col = int(max_y - min_y)

        # Create rotated image (R) of size(row, col)
        rot_img = np.zeros((row, col), np.uint8)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                temp_x = i * rotation_matrix[0][0] + j * rotation_matrix[0][1]
                temp_y = i * rotation_matrix[1][0] + j * rotation_matrix[1][1]
                rot_x = int(temp_x - min_x)
                rot_y = int(temp_y - min_y)

                if rot_x < rot_img.shape[0] and rot_y <rot_img.shape[1] and rot_x >= 0 and rot_y >= 0:
                    rot_img[rot_x][rot_y] = image[i, j]

        return rot_img

    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        """Computes the reverse rotated image by an angle theta
                rotated_image: the rotated image from previous step
                theta: angle to rotate the image by (in radians)
                Origin: origin of the original image with respect to the rotated image
                Original shape: Shape of the orginal image
                return the original image"""
        rotation_matrix = np.array([[math.cos(theta), math.sin(theta)],
                                    [-math.sin(theta), math.cos(theta)]])

        reversed_img = np.zeros((original_shape[0], original_shape[1]), np.uint8)

        for i in range(rotated_image.shape[0]):
            for j in range(rotated_image.shape[1]):
                temp_i = i - origin[0]
                temp_j = j - origin[1]
                rotated_x = int(temp_i * rotation_matrix[0][0] + temp_j * rotation_matrix[0][1])
                rotated_y = int(temp_i * rotation_matrix[1][0] + temp_j * rotation_matrix[1][1])

                if rotated_x < original_shape[0] and rotated_y < original_shape[1] and rotated_x>= 0 and rotated_y >= 0:
                    reversed_img[rotated_x, rotated_y] = rotated_image[i][j]

        return reversed_img

    def rotate(self, image, theta, interpolation_type):
        """Computes the rotated image by an angle theta and perfrom interpolation
                image: the input image
                theta: angle to rotate the image by (in radians)
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the rotated image"""

        # Compute Rotation matrix
        rotation_forward = np.array([[math.cos(theta), -math.sin(theta)],
                                          [math.sin(theta), math.cos(theta)]])

        rotation_inverse = np.array([[math.cos(theta), math.sin(theta)],
                                    [-math.sin(theta), math.cos(theta)]])

        corners = {"tl": np.array([0, 0]),
                   "tr": np.array([0, image.shape[1]]),
                   "bl": np.array([image.shape[0], 0]),
                   "br": np.array([image.shape[0], image.shape[1]])}

        rotate_corners = dict() # create dictionary
        min_x, min_y, max_x, max_y = np.inf, np.inf, -np.inf, -np.inf

        for i in corners:
            rotate_corners[i] = np.sum(rotation_forward * corners[i], axis=1)
            if rotate_corners[i][0] > max_x:
                max_x = rotate_corners[i][0]
            if rotate_corners[i][0] < min_x:
                min_x = rotate_corners[i][0]
            if rotate_corners[i][1] > max_y:
                max_y = rotate_corners[i][1]
            if rotate_corners[i][1] < min_y:
                min_y = rotate_corners[i][1]

        # Size of rotated image
        row = int(max_x - min_x)
        col = int(max_y - min_y)

        rot_img = np.zeros((row, col), np.uint8)

        O_x = -min_x
        O_y = -min_y

        if interpolation_type == "nearest_neighbor":
            for i_N in range(rot_img.shape[0]):
                for j_N in range(rot_img.shape[1]):
                    i_temp = i_N - O_x
                    j_temp = j_N - O_y
                    i_nn = int(np.round(i_temp * rotation_inverse[0][0] + j_temp * rotation_inverse[0][1]))
                    j_nn = int(np.round(i_temp * rotation_inverse[1][0] + j_temp * rotation_inverse[1][1]))
                    if i_nn < image.shape[0] and j_nn < image.shape[1] and i_nn >=0 and j_nn >= 0:
                        rot_img[i_N][j_N] = image[i_nn][j_nn]

        if interpolation_type == "bilinear":
            for i_N in range(row):
                for j_N in range(col):
                    i_temp = i_N - O_x
                    j_temp = j_N - O_y
                    i_nn = i_temp * rotation_inverse[0][0] + j_temp * rotation_inverse[0][1]
                    j_nn = i_temp * rotation_inverse[1][0] + j_temp * rotation_inverse[1][1]
                    x1 = math.floor(i_nn)
                    x2 = math.ceil(i_nn)
                    y1 = math.floor(j_nn)
                    y2 = math.ceil(j_nn)
                    if 0 <= x1 < image.shape[0] and 0 <= y1 < image.shape[1] and 0 <= x2 < image.shape[0] and 0 <= y2 < image.shape[1]:
                        p1 = np.array([x1, y1, image[x1, y1]])
                        p2 = np.array([x2, y1, image[x2, y1]])
                        p3 = np.array([x1, y2, image[x1, y2]])
                        p4 = np.array([x2, y2, image[x2, y2]])
                        intensity = interpolation()
                        rot_img[i_N][j_N] = intensity.bilinear_interpolation(p1, p2, p3, p4, i_nn, j_nn)

        return rot_img

