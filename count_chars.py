#FPSemana02

#Count the amount of letters in every word in a phrase and show the amount next to the word

user_dict = {}

phrase =(str(input("Enter any phrase: ")))
print(phrase)
phrase = phrase.split()

user_dict = {}

    
for letter_c in phrase:
    user_dict[letter_c] = len(letter_c)
        
print(user_dict)
