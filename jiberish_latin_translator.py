#get sentence to translate from user

original = input("Please enter your sentence: ").strip().lower()

# split sentence into words

words = original.split()

# loop through the words and convert to jiberish latin

translated_to_jiberish_latin = []

#if word starts with vowel just add 'yay'

#if word starts with consonant move the first letter to the end of the word and add 'yay'

for word in words:
    if word[0] in "aeiou":
        translated_word = word + "yay"
        translated_to_jiberish_latin.append(translated_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest_of_the_word = word[vowel_pos:]
        translated_word = the_rest_of_the_word + cons + "yay"
        translated_to_jiberish_latin.append(translated_word)


#stick words back together

output = " ".join(translated_to_jiberish_latin)

# output translated sentence

print(output)
