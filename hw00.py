#Homework 00
#Justin Gallicchio
#CSE 2050

import sys

if __name__ == '__main__':
    numbers = []
    for line in sys.stdin:
        for n in line.split():
            numbers.append(n)

#function that parses each element in a list object and checks for numbers.
#It then separates the numbers and adds them to a new list and returns that new list
def check_list(list):
    num_list = []
    for item in list:
        try:
            num_list.append(float(item))
        except ValueError:
            pass

    '''for item in list:
        if isinstance(item, int):
            num_list.append(item)
        elif isinstance(item, float):
            num_list.append(item)'''

    return num_list

#function used to find the mean of the numbers in the list
def mean(list):
    work_list = check_list(list)
    total = 0

    for num in work_list:
        total = total + num

    try:
        return total / len(work_list)
    except ZeroDivisionError:
        print('Division by Zero')

#function to find the median of all of the numbers in a list
def median(list):
    work_list = check_list(list)
    work_list.sort()
    try:
        if(len(work_list) > 1):
            if ((len(work_list) % 2) == 0):
                return float(min(work_list[((len(work_list)//2) - 1)], work_list[(len(work_list)//2)]))
            else:
                return float(work_list[(len(work_list)//2)])
        else:
            return work_list[0]
    except IndexError:
        print('List is empty')
#print(numbers)

#function to find the mode of all the numbers in a list.
def mode(list):
    work_list = check_list(list)
    work_list.sort()
    cur_num = 0.0
    mode_num = 0.0
    occ = 0.0
    if(len(work_list) > 1):
        for num in work_list:
            #if statement to account for zero as the start of the list
            if(num == 0):
                occ = work_list.count(num)
            #statement to check if the number being evaluated by the loop is the same
            #as the last evaluated number
            if(cur_num != num):
                cur_num = num
                #statement to decide which number occurs the most
                if(work_list.count(cur_num) > occ):
                    mode_num = cur_num
                    occ = work_list.count(cur_num)
    #special case if the list only contains 1 number
    elif(len(work_list) == 1):
        print(work_list[0])
    #special case if the list doesn't contain numbers or is empty
    else:
        print('List is empty or has no numbers')

    return mode_num

#print(mean([2, 1, 2, 1, 1.5, 1.5, 1.5]))
#print(median([2, 1, 2, 1, 1.5, 1.5, 1.5]))
#print(mode([2, 1, 2, 1, 1.5, 1.5, 1.5]))
print(mean(numbers))
print(median(numbers))
print(mode(numbers))
