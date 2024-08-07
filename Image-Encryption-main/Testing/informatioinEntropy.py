import numpy as np
from scipy.stats import entropy
from math import log, e
from PIL import Image

def entropy1(labels, base=None):
  value,counts = np.unique(labels, return_counts=True)
  return entropy(counts, base=base)


img = Image.open('Lenna.png')

img_array=np.array(img)

imgE = Image.open('lennaNewLogic.png')

img_arrayE=np.array(imgE)
print('original = ',entropy1(img_array,2))
print('Encrypted = ',entropy1(img_arrayE,2))