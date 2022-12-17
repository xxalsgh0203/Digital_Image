# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv

import numpy as np


class Filtering:

    def __init__(self, image):
        """initializes the variables for frequency filtering on an input image
        takes as input:
        image: the input image
        """
        self.image = image
        self.mask = self.get_mask

    def get_mask(self, shape):
        """Computes a user-defined mask
        takes as input:
        shape: the shape of the mask to be generated
        rtype: a 2d numpy array with size of shape
        """
        # mask = np.zeros((shape[0], shape[1]))
        # for i in range(0, mask.shape[0]):
        #     for j in range(0, mask.shape[1]):
        #         D = np.sqrt((i - int(mask.shape[0]/2))**2 + (j - int(mask.shape[1]/2))**2)
        #         if D <= mask.shape[0]/2:
        #             mask[i, j] = 1
        #         else:
        #             mask[i, j] = 0

        mask = np.zeros(shape, dtype = complex)

        for x in range(shape[0]):
            for y in range(shape[1]):
                if x > 238 and x < 249 and y < 241 and y > 228:
                    mask[x][y] = 0
                elif x > 261 and x < 274 and y < 284 and y > 272:
                    mask[x][y] = 0
                elif x > 272 and x < 286 and y < 220 and y > 206: #left under
                    mask[x][y] = 0
                elif x > 223 and x < 237 and y < 304 and y > 291: #up right
                    mask[x][y] = 0
                else:
                    mask[x][y] = 0.9

        return mask

    def post_process_image(self, image):
        """Post processing to display DFTs and IDFTs
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        You can perform post processing as needed. For example,
        1. You can perfrom log compression
        2. You can perfrom a full contrast stretch (fsimage)
        3. You can take negative (255 - fsimage)
        4. etc.
        """
        ppimage = np.zeros((image.shape[0], image.shape[1]))
        a = np.min(image)
        b = np.max(image)
        (rows, cols) = image.shape

        if b-a == 0:
            k = 0
        else:
            k = 255 / (b - a)

        for i in range(rows):
            for j in range(cols):
                ppimage[i, j] = np.round(k*(image[i, j] - a))

        return np.uint8(ppimage)

    def filter(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering
        ----------------------------------------------------------
        You are allowed to use inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do post processing on the magnitude and depending on the algorithm (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8
        """

        #1. Compute the fft of the image
        fftimage = np.fft.fft2(self.image)

        #2. shift the fft to center the low frequencies
        shift_FFT = np.fft.fftshift(fftimage)
        magnitude_DFT = np.log(np.abs(shift_FFT))
        dft = self.post_process_image(magnitude_DFT)

        #3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape)
        mask = self.get_mask(np.shape(self.image))

        #4. filter the image frequency based on the mask (Convolution theorem)
        filteredImage = np.multiply(mask, shift_FFT)
        magnitude_Filtered_DFT = np.log(np.abs(filteredImage) + 1)
        filteredDFT = self.post_process_image(magnitude_Filtered_DFT)

        #5. compute the inverse shift
        inverse_shift_FFT = np.fft.ifftshift(filteredImage)

        #6. compute the inverse fourier transform
        inverseDFT = np.fft.ifft2(inverse_shift_FFT)

        #7. compute the magnitude
        magnitude = np.uint8(np.abs(inverseDFT))

        #8. You will need to do post processing on the magnitude and depending on the algorithm (use post_process_image to write this code)
        filteredImage = self.post_process_image(magnitude)

        return [filteredImage, dft, filteredDFT]
