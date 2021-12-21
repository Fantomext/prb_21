def PalindromeIs(lengthMyStr, count):
    count = 0
    for x in range(lengthMyStr):
        if myStr[0+x] == myStr[-1-x]:
            count += 1
            if count == lengthMyStr:
                print("Строка является палиндромом")
            else:
                print("Строка не является палиндромом")

print("Введите строку")
myStr = input()
lengthMyStr = len(myStr)
count = 0

PalindromeIs(lengthMyStr, count)
