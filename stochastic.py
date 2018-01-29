import random
import frequency

def main(argv):
    # stop execution if file not specified
    if len(argv) == 1:
        raise Exception("No file specified")

    h = frequency.histogram(argv[1])
    # call sample
    # sample()

def sample(h):
    r = random.random()


if __name__ == "__main__":
    main(sys.argv)
