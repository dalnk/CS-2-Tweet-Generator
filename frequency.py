import sys
import string

def main(argv):
    # stop execution if file not specified
    if len(argv) == 1:
        raise Exception("No file specified")
    h = histogram(argv[1])
    save_histogram(h, "sample.histogram")

def histogram(filename):
    # lets open up that file
    corpus = open(filename,'r')

    # read that shit into a list
    dirty_list = corpus.read().split('\n')

    # pile all the lines into one list
    clean_list = []
    for line in dirty_list:
        clean_list.extend(line.split(' '))

    # purge those empty strings
    clean_list = list(filter(None, clean_list))

    # let's count up the frequencies
    histogram = {}
    for token in clean_list:
        t = token.lower()
        # some vodo to init and avoid null pointer
        histogram[token] = histogram[token] + 1 if token in histogram else 1

    return sorted(histogram.items(), key=lambda tup: tup[1], reverse=True)

# output files for quick storage
def save_histogram(histogram, filename):
    # open output file and write it sorted
    writer = open(filename, 'w')
    for line in histogram:
        print(line)
        buffer = '%s %d\n' % (line[0], line[1])
        writer.write(buffer)
    print("wrote sorted histogram to ./output_histogram.txt")

def unique_words(histogram):
    return len(histogram)

def freq(histogram, word):
    d = dict(histogram)
    u = unique_words(histogram)
    f = d.get(word)
    return f / float(u)

# todo read histogram files
# def read_histogram(filename):

# this script requires a path be passed to it
if __name__ == "__main__":
    main(sys.argv)

