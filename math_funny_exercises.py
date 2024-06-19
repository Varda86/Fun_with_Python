print("\nMATH EXCERCISES SOLVED WITH PYTHON\n")
#Funcion to create an integer number:
def insert_number():
    while True:
        try:
            n = int(input("Insert an integer number:"))
        except:
            print("I said to insert an integer number!!!!")
        else:
            break
    return n
#Function to create a list of random numbers
def random_numbers_list():
    print("Choose the number of values of the list")
    lung_list = insert_number()
    print("The values are between ")
    x = insert_number()
    print(" and ")
    y = insert_number()
    from random import randint
    list_n = [randint(x,y) for n in range (lung_list)]
    return list_n


#Function to calculate the highest common factor
def HCF(m, n):
    if n<=0 or m<=0:
        print("Some of the inserted numbers are equals or less than 0.")
    else:
        print("the highest common factor between ", n, " and ", m, " is:")
        while n != m:
            if n>m:
                n=n-m
            else:
                m=m-n
        print(n)

#Function to calculate the prime factorization
def prime_fact(x):
    print(f"The prime factorization of {x} is:")
    y = 2
    factors = []
    while x != y:
        if x % y == 0:
            factors.append(y)
            x = x/y
        else:
            y += 1
    factors.append(y)
    print(factors)

#Function to calculate the average of a list of numbers
def media(list_n):
    return sum(list_n)/len(list_n)




print("\nEXERCISE 1: FIND THE HIGEST COMMON FACTOR OF TWO NUMBERS\n")
#Let's ask to the user two integer numbers
print("Insert the numbers:")
m = insert_number()
n = insert_number()
#Now we calculate di HCF of the choosen numbers
HCF(m, n)

print("\nESERCISE 2:  FACTORIZATION OF A SELECTED NUMBER\n")
#Let's ask to the user one integer number
print("Insert the numbers:")
n = insert_number()
#Ora calcoliamo la sua scomposizione in fattori primi
prime_fact(n)


print("\nEXERCISE 3: FIND THE AVERAGE OF A RANDOM LIST OF INTEGER NUMBERS\n")
#Let's ask to the user to create a list of integer numbers
list_n = random_numbers_list()
#Calculate the average
print(f"The average of the numbers {list_n} is {media(list_n)}")


print("\nEXERCISE 4: SUM OF THE FIRST N NATURAL NUMBERS...\n")
# Calcoliamo la somma dei primi 6 numeri naturali e la somma del loro quadrato con ciclo for e formule di Gauss
n = 6
m = 0
for num in range(1,n+1):
    m = m+num
print(f"The sum of the first {n} natural numbers using a for cicle is: {m}")
print(f"Their sum using Gauss Formula is: {(n*(n+1)/2)}")

print("\n...AND THE SUM OF THE FIRST N SQUARED NATURAL NUMBERS: ")
n = 6
m = 0
for num in range(1,n+1):
    m = m+num**2
print(f"The sum of the first squared {n} natural numbers using a for cicle is: {m}")
print(f"Their sum using Gauss Formula is: {(n*(n+1)*(2*n+1))/6}")
