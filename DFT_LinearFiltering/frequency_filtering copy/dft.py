# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import math
import numpy as np
import math as math
class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""

        (rows, cols) = matrix.shape
        temp_matrix = np.zeros((rows, cols), dtype=complex)
        for u in range(matrix.shape[0]):
            for v in range(matrix.shape[1]):
                for i in range(matrix.shape[0]):
                    for j in range(matrix.shape[1]):
                        temp_matrix[u][v] = temp_matrix[u][v] + matrix[i][j] * (math.cos(2 * np.pi * (u * i + v * j) / 15) - 1J * math.sin(2 * np.pi * (u * i + v * j) / 15))

        return temp_matrix

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        You can implement the inverse transform formula with or without the normalizing factor.
        Both formulas are accepted.
        takes as input:
        matrix: a 2d matrix (DFT) usually complex
        returns a complex matrix representing the inverse fourier transform"""

        (rows, cols) = matrix.shape
        temp_matrix = np.zeros((rows, cols), dtype=complex)
        for u in range(matrix.shape[0]):
            for v in range(matrix.shape[1]):
                for i in range(matrix.shape[0]):
                    for j in range(matrix.shape[1]):
                        temp_matrix[u][v] = temp_matrix[u][v] + matrix[i][j] * (math.cos(2 * np.pi * (u * i + v * j) / 15) - 1J * math.sin(2 * np.pi * (u * i + v * j) / 15))

        return temp_matrix

    def magnitude(self, matrix):
        """Computes the magnitude of the input matrix (iDFT)
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the complex matrix"""
        temp2 = np.zeros((matrix.shape[0], matrix.shape[1]))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                temp2[i][j] = math.sqrt(math.pow(np.real(matrix[i][j]), 2) + math.pow(np.imag(matrix[i][j]), 2))
        return temp2
