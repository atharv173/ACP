start = int(input("Enter the starting number: "))

end = int(input("Enter the ending number: "))

squares = []

for num in range(start, end + 1):    #loops through numbers from start to end
    square = num ** 2          
    squares.append(square)     

even_squares = []
odd_squares = []

for value in squares:
    if value % 2 == 0:         
        even_squares.append(value)
    else:                      
        odd_squares.append(value)


print("\nAll square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)



#for num in range(start, end + 1):
#explanation :-
# for → starts a loop
#num → variable that stores each number during the loop
#range(start, end + 1) → generates numbers from start up to end

#What this line does:
#It creates a loop that runs from the starting number to the ending number (including the end value)