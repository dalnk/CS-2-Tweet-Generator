import sys

# lets get the text file location
print(sys.argv)

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
print(clean_list)
