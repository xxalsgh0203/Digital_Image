import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randint

class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Implement the blob coloring algorithm
        takes a input:
        image: binary image
        return: a list/dict of regions"""
        r = [[0] * len(image[0]) for _ in range(len(image))]
        k = 1
        regions = dict()
        for row in range(0, len(image)):
            for col in range(0, len(image[0])):
                if row == 0 and col == 0:
                    if image[row][col] == 255:
                        r[row][col] = k
                        k += 1
                elif row == 0:
                    if image[row][col] == 255 and image[row][col - 1] == 255:
                        r[row][col] = r[row][col - 1]
                elif col == 0:
                    if image[row][col] == 255 and image[row - 1][col] == 255:
                        r[row][col] = r[row - 1][col]
                else:
                    if image[row][col] == 255 and image[row][col - 1] == 0 and image[row - 1][col] == 0:
                        r[row][col] = k
                        k += 1
                    if image[row][col] == 255 and image[row][col - 1] == 0 and image[row - 1][col] == 255:
                        r[row][col] = r[row - 1][col]
                    if image[row][col] == 255 and image[row][col - 1] == 255 and image[row - 1][col] == 0:
                        r[row][col] = r[row][col - 1]
                    if image[row][col] == 255 and image[row][col - 1] == 255 and image[row - 1][col] == 255:
                        r[row][col] = r[row - 1][col]
                        if r[row][col - 1] != r[row - 1][col]:
                            for x in range(0, row):
                                for y in range(0, col):
                                    if r[x][y] == r[row][col - 1]:
                                        r[x][y] = r[row - 1][col]

        for row in range(0, len(r)):
            for col in range(0, len(r[0])):
                if r[row][col] in regions.keys() and r[row][col] != 0:
                    regions.setdefault(r[row][col], []).append([row, col])
                elif r[row][col] != 0:
                    regions[r[row][col]] = [[row, col]]

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list/dict of pixels in a region
        returns: region statistics"""

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)
        count = 0
        stats = []
        for key in region.keys():
            if len(region[key]) > 15:
                area = len(region[key])
                pixels = region[key]
                x = 0
                y = 0
                count += 1
                for points in pixels:
                    x += points[0]
                    y += points[1]
                x /= len(region[key])
                y /= len(region[key])
                centroid = (int(x), int(y))
                stats.append([count, area, centroid])
                print("Region: ", count, "Area: ", area, "Centroid", centroid)
        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>

        return stats


    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        Make a copy of the image on which you can write text.
        takes as input
        image: a list/dict of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        # comp_image = np.copy(image)

        # for line in stats:
        #     area = str(line[1])
        #     centroid = line[2]
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     color = (0, 0, 255)
        #     comp_image = cv2.putText(image, "*", (centroid[0], centroid[1]), font, 0.25, color, 1)
        #     comp_image = cv2.putText(image, area, (centroid[0] + 2, centroid[1] + 2), font, 0.5, color, 1)
        #
        # return comp_image

        comp_image = np.uint8(255 - image)

        for key, value in list(stats.items()):
            centroid = value[0]
            area = value[1]
            cv2.putText(comp_image, '.' + str(key) + ',' + str(area), (centroid[1], centroid[0]), cv2.FONT_HERSHEY_DUPLEX,
                        0.3, 80)

        return comp_image
