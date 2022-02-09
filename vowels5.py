vowels=['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found={}

for letter in word:
    if letter in vowels:
        found[letter]+=1
        
for v,k in sorted(found.items()):
    print(v, 'was found', k, 'time(s).')

