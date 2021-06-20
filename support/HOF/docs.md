# Functions:

## map
    - Takes a function and a list, then applies that function to each value in the list
    - Returns a list of the returned values

## filter
    - Takes a boolean-function and a list, then applies that function to each value in the list
    - For every value that returns true from the boolean-function, that value is appended to a return list
    - Returns a list of all the filtered values

## fold
    - Takes an initial value (I), a two-parametered function (F), and a list (L)
    - Calls F on I and the first value in L
    - The result becomes the new I value
    - Loops this until L is fully traversed
    - Returns the final value of I

## repeat
    - Takes a function (F), an argument (A), and a positive integer (I)
    - Returns f(f(... (x) ...))
    - (The number of times F occurs is equal to I)

## factorial
    - Returns the factorial of a number (N)

## harmonic_series
    - Takes a positive integer (N) and returns the value of N from the Harmonic Series

## flatten
    - Takes a list (L) made of sub-lists and returns a single list with all values at the top level

### product
    - Takes two variables (x,y) and returns their product

### compose
    - Takes two functions (f,g) and returns f(g)
    - f(g) is a lambda function, so it can be used like so:
        `f: returns x * 2; g: returns x + 2`
        `h = compose(f,g)`
        `h(x): returns f(g(x)) or (x + 2) * 2`

### square
    - returns x ** 2

### sqrt
    - returns x ** .5 (square root)

### harmonic
    - returns 1/x (a reciprocal)

### concat
    - returns string1 + string2

### find_big
    - Takes two numbers, returns the larger

### find_lil
    - Takes two numbers, returns the smaller

### find_max
    - Takes a list of numbers, returns the largest

### find_min
    - Takes a list of numbers, returns the smallest

### is_prime
    - Takes a number, returns bool reflecting if it is a prime number

### sum_two
    - Takes two numbers, returns the sum

### longer
    - Takes two strings, returns the longer; if equal lengths, returns the first string

### sum_lst
    - Takes a list of numbers, returns the sum of all of them combined

### square_lst
    - Takes a list of numbers, returns a list with the respective square of each number    

### sum_sq
    - Returns the total sum of all the squares in a list (L)

### sq_sum
    - Returns the square of the total sum of a list (L)

### prime_factorization
    - Takes an integer (N) and returns the prime factorization of it