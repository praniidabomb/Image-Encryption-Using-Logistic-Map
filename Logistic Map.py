from PIL import Image
import numpy as np

def decimalToBinary(num):
    return format(num, '08b')

im = Image.open("Your Image").convert('L')
image_array = np.array(im)
row, col = image_array.shape

r = 3.99
N = row * col
x = 0.5 + np.zeros(N)
for n in range(N-1):
    x[n+1] = r * x[n] * (1 - x[n])
y = x.reshape(row, col)
p = y*255
z = p.astype('int64')
imgg2 = np.zeros(N)
imgg = imgg2.reshape(row, col)
for i in range(row):
    for j in range(col):
        p = decimalToBinary(image_array[i][j])
        key = decimalToBinary(z[i][j])
        a = [int(x) for x in str(p)]
        b = [int(x) for x in str(key)]
        string = ""
        for x in range(8):
            string = string + str(a[x] ^ b[x])
        imgg[i][j] = int(string[::-1], 2)

img2 = Image.fromarray(np.uint8(imgg))
img2.show()
img2 = img2.save("Your Cipher Image Name")
