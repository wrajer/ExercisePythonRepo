import os

cwd = os.getcwd()
print(cwd)

lookUp = "haslo"

newFile = open("newfile.txt", "a", encoding="utf-8")

try:
    with open("acro.txt") as file:  # jeśli mamy with to sam zamknie nam plik,
        # start file operation
        # result = file.read()  # czyta cały plik
        # resultLine = file.readline()
        # print(resultLine)
        # resultLine = file.readline()
        # print(resultLine)
        # resultLines = file.readlines()

        # # print(result)
        # print(resultLine)
        # print(resultLines)

        # aby loopować po kązdej lini możmey zrobić po prostu
        for line in file:
            print(line)
            if lookUp in line:
                print("Uwaga znaleziono w tym", lookUp)
                newFile.write(f"Uwaga znaleziono w tym {lookUp} \n")
except FileNotFoundError as e:
    print("File not found")


# inny sposob to, ale jest dluzszy
file2 = open("acro.txt")
try:
    # di operation
    pass
finally:
    file2.close

newFile.close()
