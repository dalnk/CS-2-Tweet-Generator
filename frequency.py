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

# let's see the fruits of our labour
# print(clean_list)

# let's count up the frequencies
histogram = {}
for token in clean_list:
    # some vodo to init and avoid null pointer
    histogram[token] = histogram[token] if token in histogram else 0 + 1

# sort the dictionary
sorted_list = [(k, histogram) for k in sorted(histogram, key=histogram.get, reverse=True)]

writer = open('output_histogram.txt', 'w')
for line in histogram.keys():
    buffer = '%s %d' % (line, histogram[line])
    writer.write(buffer)
print("wrote sorted histogram to ./output_histogram.txt")
