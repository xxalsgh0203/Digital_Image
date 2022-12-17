import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randint

class CellCounting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        regions = dict()

        [rows, columns] = np.shape(image)
        new_region_image = np.pad(np.zeros((rows, columns), dtype=int), (1, 0), 'constant', constant_values=0)

        count = 0
        for i in range(rows):
            for j in range(columns):
                # print(regions)
                top = new_region_image[i, j+1]
                left = new_region_image[i+1, j]
                # new region
                if left == 0 and top == 0 and image[i, j] == 255:
                    count = count + 1
                    new_region_image[i+1, j+1] = count
                    regions[str(new_region_image[i+1, j+1])] = []
                    regions[str(new_region_image[i+1, j+1])].append((i, j))
                # assign same region as top
                elif left == 0 and top != 0 and image[i, j] == 255:
                    new_region_image[i+1, j+1] = top
                    regions[str(new_region_image[i + 1, j + 1])].append((i, j))
                # assign same region as left
                elif left != 0 and top == 0 and image[i, j] == 255:
                    new_region_image[i+1, j+1] = left
                    regions[str(new_region_image[i + 1, j + 1])].append((i, j))
                # if both are same
                elif left != 0 and top != 0 and left == top and image[i, j] == 255:
                    new_region_image[i+1, j+1] = left
                    regions[str(new_region_image[i + 1, j + 1])].append((i, j))
                # if top and left pixels belong to different regions, make them same
                elif left != 0 and top != 0 and left != top and image[i, j] == 255:
                    new_region_image[i+1, j+1] = top    # current
                    new_region_image[i+1, j] = top      # left
                    regions[str(new_region_image[i+1, j+1])].append((i, j))
                    regions[str(new_region_image[i+1, j+1])].extend(regions[str(left)])
                    regions[str(left)].clear()

        for i in range(1, len(regions)+1):
            if len(regions[str(i)]) == 0:
                regions.pop(str(i))

        # number of regions
        print("\nNumber of regions: ", len(regions))

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        for key, value in list(region.items()):
            if len(value) < 15:
                region.pop(key)

        stats = region
        count = 0
        for key, value in list(region.items()):
            count += 1
            area = len(value)
            Xc, Yc = (1 / area) * np.sum(value, axis=0)
            centroid = (np.uint8(Xc), np.uint8(Yc))
            stats[key] = []
            stats[key].append(centroid)
            stats[key].append(area)
            print("Region: ", count, "Area: ", area, "Centroid", centroid)

        return stats

    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        comp_image = image.copy()

        for key, value in list(stats.items()):
            centroid = value[0]
            area = value[1]
            cv2.putText(comp_image, '*' + str(key) + ',' + str(area), (centroid[1], centroid[0]), cv2.FONT_HERSHEY_DUPLEX, 0.3, 80)

        return comp_image