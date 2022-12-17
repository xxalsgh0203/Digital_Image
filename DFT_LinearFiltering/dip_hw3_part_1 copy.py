"""dip_hw3_part_1.py: Starter file to run howework 3"""
import cv2
from frequency_filtering import dft
from numpy.random import rand
import numpy as np
# Example Usage: ./dip_hw3_part_1
# Example Usage: python dip_hw3_part_1.py

__author__      = "Pranav Mantini"
__email__ = "pmantini@uh.edu"
__version__ = "1.0.0"

def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def main():
    """ The main funtion that parses input arguments, calls the approrpiate
     interpolation method and writes the output image"""

    # Initialize a matrix of 25X25 pixels
    input_matrix = np.int_(rand(15, 15)*256)
#     input_matrix = np.array([
#     [145,  73, 210,  59, 228,  58,  49,   2, 119, 112, 226,  17, 168, 107,  39],
#     [155,  22,  96, 225, 220,  35,190,  63,  88, 121,  40, 173, 215,  73, 195],
#     [227, 168,  68,  65, 208, 206,  12,  52, 231, 142, 247, 109, 147,  44, 230],
#     [ 74,  91,  50, 193,   8,  44, 116,  35, 149, 237, 181,  60, 146,  32, 168],
#     [ 71,  14,  54, 180,  16,  89, 252, 155,  77,  22, 186, 123, 115, 236, 183],
#     [ 51, 106, 182,  26, 199, 251,  65, 108, 204, 194, 232, 178, 230, 253,  83],
#     [162, 204, 127,  51, 231, 174,  80, 227, 177, 151, 227,  88, 138, 136,   7],
#     [250, 101, 213, 125,  99, 198,  62,   1,  75, 169,  15, 181, 199, 141,  11],
#     [188, 201, 189, 117,  30,  36,  19, 245, 178,  16,  70,  26, 195,  73, 151],
#     [154,  40, 192, 113, 181, 244,   5, 240, 145, 105,  57,  67, 155, 188, 190],
#     [221,  87, 206,  36,  29, 156, 250, 114, 198, 201, 108,   2,  36, 248, 178],
#     [205, 170, 170, 240,  12,  85,  66, 180,  91, 168,  59, 189, 160,  94, 242],
#     [ 35,  92, 198,  71,  98,  43,  43,  30, 249, 123, 175, 167, 213,  72,  81],
#     [ 33, 125, 135, 183, 192, 207,  49, 135,  91,  41,  43, 184, 103,  82,  38],
#     [103, 217, 125,   0, 129,  78,  50, 172, 221, 163, 123, 110,  42,  90, 144]
# ])

    print("---------------Input Matrix----------------")
    print(input_matrix)

    dft_obj = dft.Dft()

    # Compute dft
    fft_matrix = dft_obj.forward_transform(input_matrix)
    print("---------------Forward Fourier Transform----------------")
    print(fft_matrix)

    # Compute the inverse Fourier transfrom
    ift_matrix = dft_obj.inverse_transform(fft_matrix)
    print("---------------Inverse Fourier Transform----------------")
    print(ift_matrix)
    
    # Compute the magnitude of the inverse dft
    magnitude_matrix = dft_obj.magnitude(ift_matrix)
    print("---------------Magnitude of the inverse Fourier Transform ----------------")
    print(magnitude_matrix)


if __name__ == "__main__":
    main()







