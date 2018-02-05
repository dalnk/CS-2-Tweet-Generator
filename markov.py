import sys
import stochastic
import frequency

def main(argv):
    n = prep_markov(argv[1])
    print(make_sentence(n, 20))

def prep_markov(filename):
    nodes = {}

    # base
    base = frequency.read_tokens(filename)

    # step through corpus
    for i in range(len(base)):
        if nodes[base[i]]:
            if not i+1 = len(base):
                if nodes[base[i]][base[i+1]]:
                    nodes[base[i]][base[i+1]] += 1
                else:
                    nodes[base[i]]


        nodes[b[0]] = make_word_dict(b[0], base)

    return nodes

def make_sentence(nodes, length):
    result = ""
    curr = next(iter(nodes))
    for i in range(length):
        temp = stochastic.sample(nodes[curr].items())
        result = result + temp + " "
        curr = temp
    return result

def make_word_dict(word, base):
    result = {}
    found = False
    for b in base:
        if found:
            result[b] = int(result.get(b) or 0) + 1
            found = False

        if b == word:
            found = True
    return result

# function to generate the histograms
#
# Stepper function to then print sentences
#

if __name__ == "__main__":
    main(sys.argv)
