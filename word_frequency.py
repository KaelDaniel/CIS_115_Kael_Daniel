#This program cuts a sentence and then counts the frequency of each word in the sentence.

yeet = input("Please enter a sentence: ") #user input a sentence

frequency = {} #dictionary to hold word frequency

def word_frequency(sentence): #function to count word frequency
    words = sentence.split() #split the sentence into words
    for word in words: #for loop to count each word
        if word in frequency: #if word is already in dictionary, increment its count
            frequency[word] += 1
        else: #if word is not in dictionary, add it with count 1
            frequency[word] = 1

word_frequency(yeet) #call the function with user input before printing the frequency so the dictionary is populated

print(frequency)