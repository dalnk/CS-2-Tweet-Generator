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
    f = convert_freq(h, count_words(h))
    i = float(0)
    for w in f:
        i = i + float(w[1])
        if i > r:
            return w[0]

def convert_freq(h, count):
    freq = []
    for t in h:
        freq.append((t[0], frequency.freq(h,t[0],count)))
    return freq

def count_words(h):
    words = 0
    for n in h:
        words = words + n[1]
    return words


if __name__ == "__main__":
    main(sys.argv)
