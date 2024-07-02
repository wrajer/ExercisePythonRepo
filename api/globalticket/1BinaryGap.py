def countgap(number=int):

    binar = bin(number)[2:]
    maxGap = 0

    while True:
        if binar.count("1") < 2:
            break

        if binar.count("0") < 1:
            break

        first1 = binar.find("1")
        second1 = binar.find("1", first1 + 1)
        if second1 == -1:
            break

        if (second1 - first1 - 1) > maxGap:
            maxGap = second1 - first1 - 1

        binar = binar[second1:]

    return maxGap


print(str(300), " - ", bin(300)[2:], " gap is ", str(countgap(300)))
print(str(30), " - ", bin(30)[2:], " gap is ", str(countgap(30)))
print(str(3), " - ", bin(3)[2:], " gap is ", str(countgap(3)))
print(str(0), " - ", bin(0)[2:], " gap is ", str(countgap(0)))
print(str(99999999), " - ", bin(99999999)[2:], " gap is ", str(countgap(99999999)))
print(
    str(2147483647), " - ", bin(2147483647)[2:], " gap is ", str(countgap(2147483647))
)
