from PIL import Image
import numpy as np

def decimalToBinary(num):
    return format(num, '08b')

im = Image.open("frame.png").convert('L')
image_array = np.array(im)

r = 3.99
N = 384000
x = .5 + np.zeros(N)
for n in range(N-1):
    x[n+1] = r * x[n] * (1 - x[n])
y = x.reshape(800, 480)
p = y*255
z = p.astype('int64')
imgg2 = np.zeros(384000)
imgg = imgg2.reshape(800, 480)
for i in range(800):
    for j in range(480):
        p = decimalToBinary(image_array[i][j])
        key = decimalToBinary(z[i][j])
        a = [int(x) for x in str(p)]
        b = [int(x) for x in str(key)]
        string = ""
        for x in range(8):
            string = string + str(a[x] ^ b[x])
        imgg[i][j] = int(string[::-1], 2)

img2 = Image.fromarray(imgg, 'L')
img2.show()
