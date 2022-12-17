class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = [0]*256

        for x in range(0, image.shape[0]):
            for y in range(0, image.shape[1]):
                hist[image[x, y]] += 1
        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram it to find the otsu's threshold assuming that the input hstogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value (otsu's threshold)"""

        threshold = 0
        total = sum(hist)
        size = len(hist)

        p_hist = [0] * size
        for i in range(size):
            p_hist[i] = hist[i] / total

        list_var = list()
        for t in range(0, size):
            q1 = sum(p_hist[t] for t in range(0, t + 1))
            q2 = sum(p_hist[t] for t in range(t + 1, size))

            if q1 == 0:
                u1 = 0
                var1 = 0
            else:
                u1 = sum(t * p_hist[t] for t in range(0, t + 1)) / q1
                var1 = sum((t - u1) * (t - u1) * p_hist[t] for t in range(0, t + 1)) / q1
            if q2 == 0:
                u2 = 0
                var2 = 0
            else:
                u2 = sum(t * p_hist[t] for t in range(t + 1, size)) / q2
                var2 = sum((t - u2) * (t - u2) * p_hist[t] for t in range(t + 1, size)) / q2

            var = q1 * var1 + q2 * var2
            list_var.append(var)

        threshold = list_var.index(min(list_var))

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        hist = BinaryImage.compute_histogram(self, bin_img)
        otsu_threshold = BinaryImage.find_otsu_threshold(self, hist)

        for row in range(0, image.shape[0]):
            for col in range(0, image.shape[1]):
                if image[row][col] <= otsu_threshold:
                    bin_img[row][col] = 255
                else:
                    bin_img[row][col] = 0

        return bin_img