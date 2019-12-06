import imageio
import numpy as np

lena = imageio.imread('lena.png', pilmode='RGB')
images = []

for x in range(0, 6):
    noisy = lena + 10 * lena.std() * np.random.random(lena.shape)
    images.append(noisy)


imageio.mimsave("myGalena2.gif", images)
