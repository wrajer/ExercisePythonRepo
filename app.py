def function1(age):
    return "You were born in " + str(2024 - age)


age = 20
price = 19.95
boolen1 = 1
if boolen1 == True:
    print("test1", age)
print("test2" + str(age))

# name=input("What is your name? ")
# print("Hi ", name)
# age=input("What is your age? ")
# print(function1(int(age)))

course = "Python text"
print(course.upper())

# print(5/3)
# print(5//3)
# print(5%3)
# print(5 ** 3)
# age += 3
# print ("test1",age)
# i=0
# while (i<=4_00):
#    print(i * "y")
#    i+=1

names = ["mis", "rower", "egon"]
print(names[0])
print(names[-3])
print(names[0:3])
print(names[0 : names.__len__()])
print(names.__len__())

for item in names:
    if item in ["mis"]:
        print(item)

# for item in range(3, 100, 4):
#     print(item)


expenses = [10.5, 8, 5, 15, 20, 5, 3]

sum2 = 0

for expense in expenses:
    sum2 += expense

print(sum2)

total = sum(expenses)

print(total)

expenses = 0
expensesList = []

# for i in range(1, 6, 1):
#     ex = float(input("Enter expenses: "))
#     expenses += ex
#     expensesList.append(ex)

# print(expensesList)
# print(expenses)

money_owned = 50000
apr = 0.12
payment = 1000
months = 2


monthly_rate = apr / 12

for i in range(months):
    money_owned *= 1 + monthly_rate
    print(str(i) + ".Money owned : " + str(money_owned))
    money_owned -= payment

dictonary = {"Monday": "Lody", "Tuesday": "Kopytka"}
dictonary.update({"Wednesday": "Kasza"})
dictonary["Friday"] = "Schabowy"
print(dictonary)

print(dictonary.get("Friday"))
print(dictonary.get("Sunday"))

for key, menu in dictonary.items():
    print(key + " : " + menu)


contacts = {
    "number": 4,
    "students": [
        {"name": "jas", "email": "jase@com"},
        {"name": "jas2", "email": "jase2@com"},
        {"name": "ja3", "email": "ja3e@com"},
        {"name": "jas4", "email": "jas4@com"},
    ],
}

print(contacts["students"])
print(contacts["students"][2])

for i in range(contacts["number"]):
    print(contacts["students"][i]["email"])

#powysze działa ale poniższe jest chybałądniejsze 
for student in contacts["students"]:
    print(student["email"])

print("---------------------")
for key, email in contacts["students"][1].items():
    print(email)
