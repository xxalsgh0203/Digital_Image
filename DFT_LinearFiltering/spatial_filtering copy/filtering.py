import numpy as np
import math as math

class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        """Initialzes/Computes and returns a 5X5 Gaussian filter"""
        G = np.zeros([5, 5])
        sigma = 1
        sum = 0

        for x in range(-2, 3):
            for y in range(-2, 3):
                G[x+2, y+2] = (1 / (2 * math.pi * sigma**2)) * (math.exp(-(x**2 + y**2) / (2 * sigma**2)))
                sum += G[x+2, y+2]

        G *= 1 / sum
        return G

    def get_laplacian_filter(self):
        """Initialzes and returns a 3X3 Laplacian filter"""

        L = np.array([[0, -1, 0],
                      [-1, 4, -1],
                      [0, -1, 0]])

        return L

    def filter(self, filter_name):
        """Perform filtering on the image using the specified filter, and returns a filtered image
            takes as input:
            filter_name: a string, specifying the type of filter to use ["gaussian", laplacian"]
            return type: a 2d numpy array
                """

        if filter_name == "gaussian":
            temp = np.pad(self.image, pad_width=2)
            filter = self.get_gaussian_filter()
            final_image = temp.copy()

            for i in range(2, temp.shape[0]-2):
                for j in range(2, temp.shape[1]-2):
                    sum = 0
                    sum += (filter[0, 0] * temp[i - 2, j - 2])
                    sum += (filter[0, 1] * temp[i - 2, j - 1])
                    sum += (filter[0, 2] * temp[i - 2, j])
                    sum += (filter[0, 3] * temp[i - 2, j + 1])
                    sum += (filter[0, 4] * temp[i - 2, j + 2])

                    sum += (filter[1, 0] * temp[i - 1, j - 2])
                    sum += (filter[1, 1] * temp[i - 1, j - 1])
                    sum += (filter[1, 2] * temp[i - 1, j])
                    sum += (filter[1, 3] * temp[i - 1, j + 1])
                    sum += (filter[1, 4] * temp[i - 1, j + 2])

                    sum += (filter[2, 0] * temp[i, j - 2])
                    sum += (filter[2, 1] * temp[i, j - 1])
                    sum += (filter[2, 2] * temp[i, j])
                    sum += (filter[2, 3] * temp[i, j + 1])
                    sum += (filter[2, 4] * temp[i, j + 2])

                    sum += (filter[3, 0] * temp[i+1, j - 2])
                    sum += (filter[3, 1] * temp[i+1, j - 1])
                    sum += (filter[3, 2] * temp[i+1, j])
                    sum += (filter[3, 3] * temp[i+1, j + 1])
                    sum += (filter[3, 4] * temp[i+1, j + 2])

                    sum += (filter[4, 0] * temp[i+2, j - 2])
                    sum += (filter[4, 1] * temp[i+2, j - 1])
                    sum += (filter[4, 2] * temp[i+2, j])
                    sum += (filter[4, 3] * temp[i+2, j + 1])
                    sum += (filter[4, 4] * temp[i+2, j + 2])
                    final_image[i, j] = sum

            return final_image[2:final_image.shape[0]-2, 2:final_image.shape[1]-2]

        if filter_name == "laplacian":
            temp = np.pad(self.image, pad_width=1)
            Lalacian_filter = self.get_laplacian_filter()
            final_image = temp.copy()

            for i in range(1, temp.shape[0]-1):
                for j in range(1, temp.shape[1]-1):
                    sum = 0
                    sum += (Lalacian_filter[0, 0] * temp[i - 1, j - 1])
                    sum += (Lalacian_filter[0, 1] * temp[i - 1, j])
                    sum += (Lalacian_filter[0, 2] * temp[i - 1, j + 1])

                    sum += (Lalacian_filter[1, 0] * temp[i, j - 1])
                    sum += (Lalacian_filter[1, 1] * temp[i, j])
                    sum += (Lalacian_filter[1, 2] * temp[i, j + 1])

                    sum += (Lalacian_filter[2, 0] * temp[i + 1, j - 1])
                    sum += (Lalacian_filter[2, 1] * temp[i + 1, j])
                    sum += (Lalacian_filter[2, 2] * temp[i + 1, j + 1])
                    if sum < 0:
                        final_image[i, j] = 0
                    else:
                        final_image[i, j] = sum

            return final_image[2:final_image.shape[0]-2, 2:final_image.shape[1]-2]


