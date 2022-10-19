lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

# print(lst[3][1][2])

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

# print(d['k1'][3]["tricky"][3]["target"][3])

def domainGet(domain):
  domain = domain.split("@")
  return domain[1]

# print(domainGet('user@domain.com'))

def findDog(x):
  lst = x.split()
  for word in lst:
    if word.lower() == "dog":
      return True

# print(findDog('Is there a dog here?'))

def countDog(x):
  lst = x.split()
  num = 0
  for word in lst:
    if word.lower() == "dog":
      num += 1

  return(num)

z = countDog('This dog runs faster than the other dog dude!')

# print(z)

seq = ['soup','dog','salad','cat','great']
for word in seq:
    if word[0] != "s":
        seq.remove(word)

print(seq)