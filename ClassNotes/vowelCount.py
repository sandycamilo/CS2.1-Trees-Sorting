'''Write a recursive function called vowel_count() to count the number of vowels in a given string, for example:
If you give vowel_count() the string “makeschool” it will return 4
'''

def vowel_count(str):
  vowels = "a,e,i,o,u"
  count = 0 
  for letters in vowels:
    if letters in vowels:
      count = count + 1

str = "makeschool"
print(vowel_count(str))
# print(vowel_count("makeschool"))#should print 4
# print(vowel_count("dsfgh"))#should print 0