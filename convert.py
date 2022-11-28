from words import words

words = words.splitlines()
words = [word.strip() for word in words]
print(words)
my_file=open('output.txt','w')

for word in words:
    print(word, file=my_file)
my_file.close()
