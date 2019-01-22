def main():
    # Exercise1()
    # Exercise2()
    # Exercise3()


def Exercise1():
    for nums in range(0, 7):#i want to make it print 1 through 6 so i set it to 7 so it would stop at 6

        if (nums == 3 or nums == 6):
            continue #making it skip 3 and 6

        print(nums) #printing the results


#     Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#
# Hint: Use 'continue' statement.
#
# Expected Output :
# ```0 1 2 4 5```
#

def Exercise2():



    numEven = 0 #making a variable to put my even numbers in
    numsOdd = 0 #makimg a variable to put my odd numbers in

    for numbers in range(0,11): #creating a random range starting at 0 and ending at 10

        if (numbers % 2 == 0): #if numbers are even the add the number to my numEven variable
            numEven += 1


        else:
            numsOdd += 1 #add the number into my odd

    print("Number of even numbers: " + str(numEven))
    print("Number of odd numbers: " + str(numsOdd))

#
#     Write a Python program to count the number of even and odd numbers from a series of numbers.
#
# Sample numbers: ```numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)```
#
# Expected Output :
# ```
# Number of even numbers : 5
# Number of odd numbers : 4


def Exercise3():


    sequence = "" #making an empty string so i can add my inputed string

    while(True): #it will continue until false which will be never so its an infinite loop
        userInput = input("Enter anything you like ")
        if(userInput == ""): # this code breaks it if it is an empty string
            break

        sequence += (userInput+"\n")# using to escape into a new line and also add the inout into the empty sequence

    print(sequence) #printing my sequence
#
#     Write a Python program that accepts a sequence of lines (blank line to terminate) as input and
#     prints the lines as output after User enters a blank line to end.
#
# Do not use an array to hold the lines of text
#
# Hints:
# You can use ```"\n"``` if you want to add a line break between sentences
#
#





























if __name__ == '__main__':
    main()