in_fn=input("enter filename" )
fin=open(in_fn,"r")
largest_word=""
wordcount=0
charcount=0
for word in fin.read().split():
    wordcount=wordcount+1
    charcount=charcount+len(word)
    if len(word)>len(largest_word):
        largest_word=word
print("no of words: ",wordcount)
print("no of letters: ",charcount)
print("largest word: ",largest_word)
