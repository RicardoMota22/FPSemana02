#FPSemana02

#Count the amount of letters in every word in a phrase and show the amount next to the word
phrase =(str(input("Enter any phrase: ")))
print(phrase)
phrase = phrase.split()
def b():
    
    for letter_c in phrase:
        print(letter_c,":",len(letter_c))

b()