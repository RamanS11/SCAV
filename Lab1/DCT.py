from scipy.fftpack import dct, idct
from skimage.io import imread
from skimage.color import rgb2gray
import cv2
import numpy as np
import matplotlib.pylab as plt

imag = rgb2gray(imread("Lenna.png"))    # Charge the image in grayscale.

imF = cv2.dct((imag))                   # Use the DCT function from CV2, and the inverse to get the  reconstruction.
im1 = cv2.idct(imF)

# check if the reconstructed image is nearly equal to the original image
np.allclose(imag, im1)

plt.gray()
# plot original and reconstructed images with matplotlib.pylab
plt.subplot(121), plt.imshow(imag), plt.axis('off'), plt.title('original', size = 10)
plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('reconstructed (DCT+IDCT)', size = 10)
plt.show()
