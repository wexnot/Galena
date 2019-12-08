from statistics import mean

class Positive:
    """ This is where all positive emotions inherit. """
    index = 100.0

class Negative:
    """ This is where all negative emotions inherit. """
    index = -100.0

class Happy(Positive):
    happiness_matrix = [(0., 0., 0.),
                        (10., 10., 10.),
                        (0., 10., 0.)]

    @classmethod
    def transform_to_happy(cls, response):
        apply_variation = list(map(lambda x: x * response, cls.happiness_matrix[1]))
        spice = mean(apply_variation) / cls.index
        return spice


class Sad(Negative):
    pass

class Joy(Happy):
    pass

class Anger(Sad):
    pass

class Content(Happy):
    pass

class Depressed(Sad):
    pass

def main():
    print(Happy.transform_to_happy(9))

if __name__ == "__main__":
    main()
