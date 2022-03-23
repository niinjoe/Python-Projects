with open("export1.csv", "r") as f:
  lines = f.readlines()

izq_list = ""
for i in range(5):
  x = str(lines[i].split("@healthpromed.org"))
  izq_list += x

print(izq_list)

with open("usernames.csv", "w") as users:
  users.write(izq_list)
  users.close