import sys
import stochastic
import frequency

def main(argv):
    corpus = frequency.histogram(argv[1])
    for i in range(50):
        print(stochastic.sample(corpus) + "  " + stochastic.sample(corpus) + "  " + stochastic.sample(corpus))


if __name__ == "__main__":
    main(sys.argv)
