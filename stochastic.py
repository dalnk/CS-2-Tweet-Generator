import random
import frequency
import sys

def main(argv):
    # stop execution if file not specified
    if len(argv) == 0:
        raise Exception("No file specified")

    h = frequency.histogram(argv[1])
    # call sample
    print(sample(h))

def sample(h):
    r = random.random()
    f = convert_freq(h)
    i = float(0)
    for w in f:
        i = i + w[1]
        if i > r:
            return w[0]

def convert_freq(h):
    freq = []
    for t in h:
        freq.append((t[0], frequency.freq(h,t[0])))
    return freq


if __name__ == "__main__":
    main(sys.argv)
