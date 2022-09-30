import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """

        # add your code here
        final_image = image_left.copy()

        rowsize = image_left.shape[0]
        colsize = image_right.shape[1]

        for i in range(rowsize):
            for j in range(column, colsize):
                final_image[i, j] = image_right[i, j]

        # Please do not change the structure
        return final_image  # Currently the original image is returned, please replace this with the merged image

    def intensity_scaling(self, input_image, column, alpha, beta):
        """
        Scale your image intensity.

        input_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        # add your code here
        final_image = input_image.copy()

        rowsize = input_image.shape[0]
        colsize = input_image.shape[1]

        for i in range(rowsize):
            for j in range(column):
                final_image[i, j] = final_image[i, j] * alpha
            for j in range(column, colsize):
                final_image[i, j] = final_image[i, j] * beta

        # Please do not change the structure
        return final_image  # Currently the input image is returned, please replace this with the intensity scaled image

    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)

        input_image: the input image
        column: image column at which left section ends

        return: output_image
        """

        # add your code here

        #add all the pixels up then divide to counter number
        final_image = input_image.copy()

        rowsize = input_image.shape[0]
        colsize = input_image.shape[1]

        left_total = 0
        left_pixel_count = 0

        # compute average intensity of left pixel
        for i in range(rowsize):
            for j in range(column):
                left_total = left_total + input_image[i, j]
                left_pixel_count = left_pixel_count + 1

        left_average = left_total / left_pixel_count

        # compute offset
        left_offset = 128 - left_average

        # add the offset of the left section
        for i in range(rowsize):
            for j in range(column):
                if final_image[i, j] + left_offset > 255:
                    final_image[i, j] = 255
                elif final_image[i, j] + left_offset < 0:
                    final_image[i, j] = 0
                else:
                    final_image[i, j] = final_image[i, j] + left_offset

        # compute average intensity of right pixel
        right_total = 0
        right_pixel_count = 0

        for i in range(rowsize):
            for j in range(column, colsize):
                right_total = right_total + input_image[i, j]
                right_pixel_count = right_pixel_count + 1

        right_average = right_total / right_pixel_count

        # compute offset
        right_offset = 128 - right_average

        # add the offset to the right section
        for i in range(rowsize):
            for j in range(column, colsize):
                if final_image[i, j] + right_offset > 255:
                    final_image[i, j] = 255
                elif final_image[i, j] + right_offset < 0:
                    final_image[i, j] = 0
                else:
                    final_image[i, j] = final_image[i, j] + right_offset

        return final_image   # Currently the input image is returned, please replace this with the centralized image
