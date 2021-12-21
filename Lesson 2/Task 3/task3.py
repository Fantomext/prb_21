nonRecurringCount = 0
checkRecurring = 0

def NonRecurring(nonRecurringCount,checkRecurring):
    print("Введите строку")
    myStr = input()

    for i in range(len(myStr)):
        checkRecurring = 0
        for y in range(len(myStr)):
            if myStr[i] == myStr[y]:
                checkRecurring +=1
        if checkRecurring == 1:
            nonRecurringCount += 1
    print("неповторяющихся символов", nonRecurringCount) 

        

NonRecurring(nonRecurringCount,checkRecurring)

