
# call function from outside
# int(  input('number?')  )

name: str = input('whats your name? ')

print(name, 'your name is in length', len(name))

#       variable name
print(f"{name} your name is in length len(name)")

#     text-name
print(f"name your name is in length len(name)")

print(name, 'your name is in length', len(name))
print(f"{name} your length name is in {len(name)}")

first_name = "Petros"
last_name = "Borchardt"
id = "63 251283 B 185"
phone = "0419-0288803"

print(first_name, last_name, "id number ", id, " phone ", phone)
# last_name  first_name   id                          phone
# Borchardt, Petros id[3 251283 B 185] phone-number(0419-0288803)