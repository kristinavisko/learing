"""If you have a sentence: "Hello World is the best association ever" 
get all vowels out of it and print a sentence without them. 
You can save this in a new variable. 
Then, remove all consonants from the same sentence and print it out."""

x = "Hello World is the best association ever"
y = (list(x))
sentence = ""
without_cons = ""
i = 0
for i in y:
    if (i != "a") and (i != "e") and (i != "i") and (i != "o") and (i != "u"):
        sentence += i
    else:
        without_cons += i
print (sentence)
print (without_cons)


