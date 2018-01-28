import sys

# lets open up that file
corpus = open(sys.argv[1],'r')

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
    # some vodo to init and avoid null pointer
    histogram[token] = histogram[token] + 1 if token in histogram else 1

# open output file and write it sorted
writer = open('output_histogram.txt', 'w')
for line in sorted(histogram.items(), key=lambda tup: tup[1], reverse=True):
    print(line)
    buffer = '%s %d\n' % (line[0], line[1])
    writer.write(buffer)
print("wrote sorted histogram to ./output_histogram.txt")
