# import imageio
# import numpy as np
#
# lena = imageio.imread('sadlena.png', pilmode='RGB')
# images = []
#
# for x in range(0, 6):
#     noisy = lena + 3 * lena.std() * np.random.random(lena.shape)
#     images.append(noisy)
#
#
# imageio.mimsave("sadmyGalena.gif", images)

import numpy as np
import imageio
import emotions

class Twilight:
    """ This is where she will be created """
    images = []
    # These are the emotional images created
    happy = emotions.Happy.transform_to_happy(9)

    def __init__(self, name):
        self.name = name

    def change(self, image, emotion):

        for x in range(6):
            noisy = image + self.happy * image.std() * np.random.random(image.shape)
            self.images.append(noisy)

        imageio.mimsave("newGalena.gif", self.images)

lena = imageio.imread("lena.png")
gabriella = Twilight("Lena")
gabriella.change(lena, 9)
