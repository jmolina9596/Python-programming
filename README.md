# Python-programming
#This code is for homework 6 
##
# This program has 4 functions that each do a different task
#

#Define constant variables (list hardcoded).

ONE_TEN = [1,2,3,4,5,6,7,8,9,10]

def main():
    print("The original data for all functions is:", ONE_TEN)
    print("After swapping frist and last",swap(ONE_TEN))
    print("After replacing all even elements with a zero",evenZero(ONE_TEN))
    print("After returning the second-largest element in the list", secondLargest(ONE_TEN))
    print("After checking if the list was currently sorted in increasing order", sortOrder(ONE_TEN))


#Demonstrate swapping the first and last element.
def swap(ONE_TEN):
    data = list(ONE_TEN)
    temp = data[0]
    data [0] = data[len(data)-1]
    data[len(data)-1] = temp
    return data
    #print("After swapping first and last:",data)

#Demonstrate replacing all even elements with a zero
def evenZero(ONE_TEN):
    data = list(ONE_TEN)
    for i in range(0, len(data)):
        if data[i] %2==0:
            data[i] = 0
    return data
    #print("After replacing all even elements with a zero", data)

#Demonstrate returning the second-largest element in the list
def secondLargest(ONE_TEN):
    data = list(ONE_TEN)
    data.sort()
    temp = data[len(data)-2]
    return temp

#Demonstrate returning true if the list is currently sorted in increasing order

def sortOrder(ONE_TEN):
    original_data = list(ONE_TEN)
    sorted_data = list(ONE_TEN)
    sorted_data.sort()
    print(original_data)
    print(sorted_data)
    for i in range(0, len(sorted_data)):
        if sorted_data[i] != original_data[i]:
            return "an element in the list is not sorted"
    return "True"
    
    

main()


