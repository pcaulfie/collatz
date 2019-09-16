# The number we will perform the Collatz operation on
n = int(input("enter a positive integer: "))

# Keep looping until we reach 1
while n != 1:
    # Print the current value of n
    print (n)
    # check if n is even
    if n % 2 == 0:
        # if n is even, divide it my two
        n = n // 2
    else:
        # if n is odd, multiply it by three and add one
        n = (3 * n) + 1
# finall print the 1.
print (n)
