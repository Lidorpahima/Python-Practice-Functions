from math import factorial
#~~~~~~~~~~~~~~~~~~ QEUSTION 1 ~~~~~~~~~~~~~~~~~~~~~~~
#this function will help the funnciton finishTime to add the string to the values we calculated instead of writing the same code in the function finishTime
#easyer to read and understand the code
def addString(hour,min,sec,days):
    hour_str = str(hour).zfill(2)#fill the string with zeros (0) to the left of the string
    min_str = str(min).zfill(2) #fill the string with zeros (0) to the left of the string
    sec_str = str(sec).zfill(2) #fill the string with zeros (0) to the left of the string
    days_str = str(days).zfill(0) #fill the string with zeros (0) to the left of the string
    #check the values we calculated and return the correct pronounce
    if(hour > 1 and min == 0 and sec == 0): 
        return( f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hours exactly')
    if(hour == 1 and min == 0 and sec == 0):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour exactly'
    if(hour == 1 and min > 1 and sec > 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {min} minutes, {sec} seconds'
    if(hour > 1 and min == 1 and sec > 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hours, {min} minute, {sec} seconds'
    if(hour > 1 and min > 1 and sec == 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hours, {min} minutes, {sec} second'
    if(hour == 1 and min == 1 and sec > 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {min} minute, {sec} seconds'
    if(hour > 1 and min == 1 and sec == 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hours, {min} minute, {sec} second'
    if(hour == 1 and min > 1 and sec == 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {min} minutes, {sec} second'
    if(hour == 1 and min == 1 and sec == 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {min} minute, {sec} second'
    if(hour > 1 and min > 1 and sec > 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hours, {min} minutes, {sec} seconds'
    if(hour == 0 and min > 1 and sec == 0):  
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {min} minutes'
    if(hour == 0 and min == 1 and sec == 0):    
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {min} minute'
    if(hour == 0 and min == 0 and sec > 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {sec} seconds'
    if(hour == 0 and min == 0 and sec == 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {sec} second'
    if(hour == 0 and min == 1 and sec == 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {min} minute, {sec} second'
    if(hour == 1 and min == 1 and sec == 0):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {min} minute'
    if(hour == 1 and min == 0 and sec == 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {sec} second'
    if(hour == 1 and min == 0 and sec > 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {sec} seconds'
    if(hour == 1 and min > 1 and sec == 0):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {min} minutes'
    if(hour == 1 and min > 1 and sec == 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {min} minutes, {sec} second'
    if(hour == 1 and min == 1 and sec > 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hour, {min} minute, {sec} seconds'
    if(hour > 1 and min == 0 and sec > 1):
        return f'the finish time[{hour_str}:{min_str}:{sec_str}({days_str})]: {hour} hours, {sec} seconds'

def finishTime(hour,min,sec,flightTime):
    if  (hour < 0 or hour > 24) or (min < 0 or min > 60) or (sec < 0 or sec > 60): # check the input values
        if (hour < 0 or hour > 24):
            print(hour, ' hours value error !!!')
        if (min < 0 or min > 60):
            print(min, ' minutes value error !!!')
        if (sec < 0 or sec > 60):
            print(sec, ' seconds value error !!!')     
        return #return if the input values are not correct
    if (flightTime < 0): # check the flight time
        print('flight time cant be negative')
        return #return if the flight time is negative
    if(flightTime == 0): # if the flight time is 0 so will input the values 
         print(addString(hour,min,sec,0))
            
    if(flightTime > 0): # if the flight time is positive so will input the values
        days = int(flightTime/86400) # calculate the days
        flightTime = flightTime - (days*86400)
        hour = int(flightTime/3600) # calculate the hours
        flightTime = flightTime - (hour*3600)
        min = int(flightTime/60) # calculate the minutes
        flightTime = flightTime - (min*60)
        sec = int(flightTime/1) # calculate the seconds 
        if(days == 1): # check if the days are 1 so will print at the end day and the values we calculated
            print(addString(hour,min,sec,days), '(+', days, 'day)')
        if(days > 1): # check if the days are more than 1 so will print at the end days and the values we calculated
            print(addString(hour,min,sec,days),'(+',days,'days)')
        if(days == 0): # check if the days are 0 so will print the values we calculated
            print(addString(hour,min,sec,days))

#~~~~~~~~~~~~~~~~~~ QEUSTION 2 ~~~~~~~~~~~~~~~~~~~~~~~
def digits(num):
    count = 0
    copyNum = num
    if (num <= 0 ): # check if the number is positive
        print('only positive numbers')
        return
    while (copyNum > 0): # count the digits so we will know how to calculate the values
        count += 1
        copyNum = copyNum // 10
    if(count == 1): # check if the number is one digit 
        if(num % 2 == 0):
            print('one digit - even')
            return
        else:
            print('one digit - odd')  
            return 
    if(count == 2): # check if the number is two digits
        firstNum = num % 10
        num //= 10
        secondNum = num % 10
        if((firstNum + secondNum) % 2 == 0):
            print('two digits - even')
            return
        else:
            print('two digits - odd') 
            return
    if(count == 3): # check if the number is three digits
        firstNum = num % 10
        num //= 100
        thirdNum = num % 10
        if((firstNum + thirdNum) % 2 == 0): 
            print('three digits - even')
            return
        else:
            print('three digits - odd')
            return
    if(count == 4): # check if the number is four digits
        num = num // 10
        secondNum = num % 10
        num = num // 10
        thirdNum = num % 10
        if((secondNum + thirdNum) % 2 == 0): 
            print('four digits - even')
            return
        else:
            print('four digits - odd')
            return
    if(count == 5): # check if the number is five digits
        num = num // 100
        thirdNum = num % 10
        if(thirdNum % 2 == 0): 
            print('five digits - even')
            return
        else:
            print('five digits - odd')
            return
            
#~~~~~~~~~~~~~~~~~~ QEUSTION 3 ~~~~~~~~~~~~~~~~~~~~~~~
def correctNumber(num): # this function will check if the number is correct
    return correctNumberHealper(num) # will return the function correctNumberHealper with the input number


def correctNumberHealper(num): # this helper function will check if the number is correct
    count = 0
    copyNum = num
    while (copyNum > 0): # count the digits so we will know how to calculate the values
        count+=1
        copyNum = copyNum // 10
    if (count != 3): # check if the number is not 3 digits
        return False
    firstNum = num % 10 # save the first digit
    num = num // 10
    secondNum = num % 10 # save the second digit
    num = num // 10
    thirdNum = num % 10 # save the third digit
    if((firstNum % 2 == 0 and secondNum % 2 == 0 and thirdNum % 2 == 0) or (firstNum %2 == 1 and secondNum % 2 == 1 and thirdNum % 2 == 1)): # check if all the digits are even or all the digits are odd
        return True
    else:
        return False

#~~~~~~~~~~~~~~~~~~ QEUSTION 4 ~~~~~~~~~~~~~~~~~~~~~~~
def figure(n):
    if n <= 0 or n % 2 == 0:
        print("please enter only positive odd numbers")
        return

    middle = n // 2
    max_num = 9
    current_num = 1
    for i in range(middle + 1): # will print the top part of the diamond
        spaces = ' ' * (middle - i) #will print the space until the middle - i
        numbers = [] # will save the numbers we will print 
        for j in range(2 * i + 1): # this part will print the numbers
            numbers.append(str(current_num)) # add the number to the list we created
            current_num += 1 # add 1 to the current number
            if current_num > max_num: # check if the current number is bigger than the max number (9)
                current_num = 1 # if the current number is bigger than the max number so will start from 1
        print(spaces + ''.join(numbers)) # print the spaces and than will add numbers we created from the list (numbers)

    for i in range(middle - 1, -1, -1): # will print the bottom part of the diamond (the same like top but in reverse order)
        spaces = ' ' * (middle - i)#will print the space until the middle - i
        numbers = []# will save the numbers we will print 
        for j in range(2 * i + 1):# this part will print the numbers
            numbers.append(str(current_num))# add the number to the list we created
            current_num += 1# add 1 to the current number
            if current_num > max_num:# check if the current number is bigger than the max number (9)
                current_num = 1# if the current number is bigger than the max number so will start from 1
        print(spaces + ''.join(numbers))

#~~~~~~~~~~~~~~~~~~ QEUSTION 5 ~~~~~~~~~~~~~~~~~~~~~~~
def value(num):# this function will return the sum of the digits and the max digit
    return countDigits(num) + maxDigit(num)
    
def countDigits(num):# this function will count the digits in recursive way
    if num == 0:# if the number is 0 so will return 0
        return 0
    return 1 + countDigits(num // 10) # will return 1 and add the next digit to the sum
    
def maxDigit(num, current_max=0):# this function will return the max digit in recursive way
    if num == 0:# if the number is 0 so will return the current max
        return current_max
    current_digit = num % 10# will save the current digit
    if current_digit > current_max:# check if the current digit is bigger than the current max
        current_max = current_digit
    return maxDigit(num // 10, current_max)# will return the max digit
        
#~~~~~~~~~~~~~~~~~~ QEUSTION 6 ~~~~~~~~~~~~~~~~~~~~~~~
def pascal(n,k):# n is the row and k is the column
    if n < 0 or k < 0 or k > n: # if the input is invalid so will return -1
        return -1
    if k == 0 or k == n: # final case if k is 0 or k is n so will return 1
        return 1
    return pascal(n-1, k-1) + pascal(n-1, k)  #n-1 and k-1 will reduse until we will get to the final case in column and n-1 and k will reduse until we will get to the final case of the row (in the end will add +1 each time we will get to the final case)

#~~~~~~~~~~~~~~~~~~ QEUSTION 7 ~~~~~~~~~~~~~~~~~~~~~~~
def reduce(num):#this function will reduce the number 0 if contains and will return the number without the 0
    if num == 0:#base case if the number is 0 so will return 0
        return 0
    negative = False# will save if the number is negative so we will return the number with the negative sign in the end
    if num < 0:# check if the number is negative
        negative = True# if the number is negative so will save the negative value
        num = -num # will change the number to positive
    
    if num % 10 == 0: # check if the last digit is 0
        result = reduce(num // 10)# if the last digit is 0 so will remove the 0 and will return the number without the 0
    else: 
        result = num % 10 + 10 * reduce(num // 10) # if the last digit is not 0 so will return the number without the 0 and will add the last digit to the number without the 0

    if negative == True: # check if the number was negative
        return -result # if the number was negative so will return the number with the negative sign
    else:
        return result # if the number was positive so will return the number without the negative sign
#~~~~~~~~~~~~~~~~~~ QEUSTION 8 ~~~~~~~~~~~~~~~~~~~~~~~
def isPrimary(num):# this function will check if the number is prime
    if (num < 2 or num % 2 == 0): # check if the number is less than 2 or the number is even so will return False
        return False
    for i in range(3, int((num//2) + 1), 2): # i will start from 3 and will check comper the number to the input number and will add 2 each time we will check the number (we will check only the odd numbers)
        if(num % i == 0): # check if the number is divided by i so will return False because 
            return False
        
    return True

#~~~~~~~~~~~~~~~~~~ DRIVER ~~~~~~~~~~~~~~~~~~~~~~~
def driver():
    print('Q#1')
    finishTime(2,3,5,0)
    finishTime(23,5,10,0)
    finishTime(0,0,0,83110)
    finishTime(0,0,0,3667)
    finishTime(0,0,0,82800)
    finishTime(0,0,0,82810)
    finishTime(0,0,0,91215)
    finishTime(0,0,0,177615)                                                              
    finishTime(100,200,300,0)                                                              
    print('\nQ#2')
    digits(6)
    digits(63)
    digits(163)
    digits(1653)
    digits(16453)
    print('\nQ#3')
    print(correctNumber(2648))
    print(correctNumber(75))
    print(correctNumber(345))
    print(correctNumber(315))
    print(correctNumber(648))
    print('\nQ#4')
    figure(11)
    figure(12)
    print('\nQ#5')
    print(countDigits(7145))
    print(maxDigit(7145))
    print(value(7145))
    print(value(15))
    print(value(351))
    print('\nQ#6')
    print(pascal(3,2))
    print(pascal(10,4))
    print(pascal(5,3))
    print('\nQ#7')
    print(reduce(-160760))
    print(reduce(1020034000))
    print('\nQ#8')
    print(isPrimary(23))
    print(isPrimary(21))
driver()