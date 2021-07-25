from hashtable.hashtable import *
import re


def hashmap_repeated_word(input_string):
    hashtable = Hashtable(1024)
    li = re.sub('[^\w\d ]','',input_string).split()
    for i in li:
        if hashtable.contains(i.lower()):
            return i
        else:
            hashtable.add(i.lower(),0)
    return None

if __name__ == "__main__":

    input_string1 = 'Once upon a time, there was a brave princess who...'
    input_string2= 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
    input_string3 = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    input_string4 = ''
    input_string5 = 'Hi I am Abdullah'
    print(hashmap_repeated_word(input_string1))
    print(hashmap_repeated_word(input_string2))
    print(hashmap_repeated_word(input_string3))
    print(hashmap_repeated_word(input_string4))
    print(hashmap_repeated_word(input_string5))