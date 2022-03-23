from asyncore import write

with open('dir.txt') as f:
    lines = f.readlines()

der_list = ""
split_at = 40

# for n in range(len(lines)):
#   izq, der = lines[n].split(' ', 16)
#   list.append(der) 

# print(list)

# izq, der = lines[0][:split_at], lines[0][split_at:]

# print(der)

for i in range(len(lines)):
  izq, der = lines[i][:split_at], lines[i][split_at:]
  der_list += der

# der_string = ""

# for i in der_list:
#   der_string += i

# print(der_string)

with open("new_dir.txt", "w") as txt:
  txt.write(der_list)
  txt.close