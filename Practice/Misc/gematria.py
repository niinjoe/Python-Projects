letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

palabra = input("type word: ")

total = 0
for n in (palabra):
  total += letters.index(n)+1

print(total)