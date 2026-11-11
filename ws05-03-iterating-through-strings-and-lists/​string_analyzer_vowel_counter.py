sentence = input("Enter a sentence: ")

space = " "
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
space_count = 0

for character in sentence.lower():
    if character in vowels:
        vowel_count += 1
    elif character in sentence.lower():
        consonant_count +=1
    else:
        character in sentence.lower()
        space_count += 1
        
print("Vowels", vowel_count)
print("Consonants", consonant_count)
print("Spaces", space_count)


