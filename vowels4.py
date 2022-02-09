vowels=['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found={}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter]+=1
        
for v,k in sorted(found.items()):
    print(v, 'was found', k, 'time(s).')

