password = input("Enter new password: ")
result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

result["digit"] = False
for i in password:
    if i.isdigit():
        result["digits"] = True
result["digits"] = False

result["uppercase"] = False

for i in password:
    if i.isupper():
        result["uppercase"] = True

result["uppercase"] = False

print(result)

if all(result.values()):
    print("You have a strong password!")
else:
    print("You have a weak password!")

