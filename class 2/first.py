num = int(input("Enter a number: "))
 

if num > 0:
    #This block is idented,so it only runs if num is positive
    print("The number is positive")
    print("This is inside the 'if' block")
else:
    #This block is indented,so it only runs if num is NOT positive
    print("The number is zero or negative")
    print("This is part of the  'else' block.")


#This line is not indented,so it runs after the if-else block
print("Program ended,.")