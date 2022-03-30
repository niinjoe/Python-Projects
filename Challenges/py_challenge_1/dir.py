with open("dir.txt") as f:
    lines = f.readlines()

# der_list = ""
# split_at = 40

# izq, der = lines[0][:split_at], lines[0][split_at:]

# print(der)

# for i in range(len(lines)):
#   izq, der = lines[i][:split_at], lines[i][split_at:]
#   der_list += der

der_list = ""
for i in range(len(lines)):
    line = lines[i][40:]
    der_list += line

with open("new_dir.txt", "w") as txt:
    txt.write(der_list)
    txt.close
