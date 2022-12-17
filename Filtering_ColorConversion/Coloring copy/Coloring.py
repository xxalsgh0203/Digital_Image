import numpy as np
import math as math

class Coloring:

    def intensity_slicing(self, image, n_slices):
        '''
       Convert greyscale image to color image using color slicing technique.
       takes as input:
       image: the grayscale input image
       n_slices: number of slices
        
       Steps:
 
        1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        2. Randomly assign a color to each interval
        3. Create and output color image
        4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
 
       returns colored image
       '''
        # 1. create n+1 intervals
        intervals = np.linspace(0, image.max(), n_slices + 1)

        # 2. create n random colors
        colors = np.random.randint(0, 255, (n_slices, 3))

        # 3. create color image
        color_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

        # 4. iterate through image and assign colors to color image
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(n_slices):
                    if image[i, j] <= intervals[k + 1]:
                        color_image[i, j] = colors[k]
                        break

        return color_image

    def color_transformation(self, image, n_slices, theta):
        '''
        Convert greyscale image to color image using color transformation technique.
        takes as input:
        image:  grayscale input image
        colors: color array containing RGB values
        theta: (phase_red, phase,_green, phase_blue) a tuple with phase values for (r, g, b) 
        Steps:
  
         1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
         2. create red values for each slice using 255*sin(slice + theta[0])
            similarly create green and blue using 255*sin(slice + theta[1]), 255*sin(slice + theta[2])
         3. Create and output color image
         4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
  
        returns colored image
        '''

        intervals = []
        for i in range(n_slices):
            intervals.append(i * (255 / n_slices))
        intervals.append(255)

        r = []
        g = []
        b = []
        for i in range(n_slices):
            r.append(np.abs(255 * np.sin(i + theta[0])))
            g.append(np.abs(255 * np.sin(i + theta[1])))
            b.append(np.abs(255 * np.sin(i + theta[2])))

        coloredImage = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(1, n_slices):
                    if intervals[k] <= image[i][j] and image[i][j] < intervals[k + 1]:
                        coloredImage[i][j][0] = r[k]
                        coloredImage[i][j][1] = g[k]
                        coloredImage[i][j][2] = b[k]
                        break

        return coloredImage



        

