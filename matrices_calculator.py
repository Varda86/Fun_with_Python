#FUNctions
def create_matrix():
    while True:
        try:
            n = int(input("\nInsert the numbers of rows and press Enter-->"))
            m = int(input("Insert the numbers of columns and press enter-->"))
            if n < 0 or m < 0:
                print("Insert a positive number...")
            else:
                break
        except ValueError:
            print("Insert two integer numbers...please...")
    matrix = []
    while True:
        try:
            print("Insert the values of the matrix:")
            for x in range(n):
                row = []
                for y in range(m):
                    y = float(input("Insert the value and press Enter: "))
                    row.append(y)
                matrix.append(row)
            break
        except ValueError:
            print("Insert just numbers...please...")
    return(matrix)

def insert_SC():
    while True:
        try:
            R = float(input("\nInsert the scalar and press enter-->"))
            break
        except ValueError:
            print("Insert just numbers...please...")
    return(R)

def visualize():
    if not matrixA:
        print("\nMatrix A doesn't exist")
    else:
        n = len(matrixA)
        print("\nMatrix A:")
        for x in range(n):
            print(matrixA[x])
    if not matrixB:
        print("Matrix B doesn't exist")
    else:
        n = len(matrixB)
        print("Matrix B:")
        for x in range(n):
            print(matrixB[x])
    if scalar == 0:
        print("Scalar doesn't exist")
    else:
        print(f"Scalar: {scalar}")

def transpose():
    if not matrixA:
        print("\nMatrix A doesn't exist")
    else:
        n = len(matrixA)
        m = len(matrixA[0])
        print("\nTransposed Matrix A:")
        for x in range(m):
            print("\n")
            for y in range(n):
                print(str(matrixA[y][x]) + " ", end="")
        print("\n")

def prod_sc():
    if not matrixA:
        print("\nMatrix A doesn't exist")
    elif scalar == 0:
        print("\nScalar doesn't exist")
    else:
        n = len(matrixA)
        m = len(matrixA[0])
        prod = []
        for x in range(n):
            row = []
            for y in range(m):
                y = matrixA[x][y]*scalar
                row.append(y)
            prod.append(row)
        print("\nProduct of Matrix A and Scalar:")
        for x in range(n):
            print(prod[x])

def somma():
    if not matrixA:
        print("\nMatrix A doesn't exist")
    elif not matrixB:
        print("\nMatrix B doesn't exist")
    else:
        n = len(matrixA)
        m = len(matrixA[0])
        o = len(matrixB)
        p = len(matrixB[0])
        if n != o or m != p:
            print("It's not possible to sum the matrices, they don't have the same number of raws and columns")
        else:
            somma = []
            for x in range(n):
                row = []
                for y in range(m):
                    num = matrixA[x][y] + matrixB[x][y]
                    row.append(num)
                somma.append(row)
            print("The sum of the inserted matrices is:")
            for x in range(n):
                print(somma[x])

def prod_ab():
    if not matrixA:
        print("\nMatrix A doesn't exist")
    elif not matrixB:
        print("\nMatrix B doesn't exist")
    else:
        n = len(matrixA)
        m = len(matrixA[0])
        o = len(matrixB)
        p = len(matrixB[0])
        if m != o:
            print(''' The product is impossible!!
            The number of columns of Matrix A
            must be equal to the number of rows of Matrix B.
            Suggestion: try to switch them.
            ''')
        else:
            prod = []
            for x in range(n):
                row = []
                for y in range(p):
                    num = 0
                    for z in range(m):
                        num = num + (matrixA[x][z] * matrixB[z][y])
                    row.append(num)
                prod.append(row)
            print("The product between Matrix A and Matrix B is:")
            for x in range(n):
                print(prod[x])

def switch():
    switched_matrixA = matrixB
    switched_matrixB = matrixA
    return(switched_matrixA, switched_matrixB)

#CENTRAL CODE WITH GLOBAL MATRICES:
matrixA = []
matrixB = []
scalar  = 0

while True:
    choice = (input('''\nPress the button:
    1. Insert matrix A
    2. Insert matrix B
    3. Insert scalar R
    4. Visualize Matrix A, B end the scalar
    5. Trasposed of Matrix A
    6. R*A
    7. A+B
    8. A*B
    9. Switch A e B
    10. Exit
    --> '''))

    if choice == '1':
        matrixA = create_matrix()
    elif choice == '2':
        matrixB = create_matrix()
    elif choice == '3':
        scalar = insert_SC()
    elif choice == '4':
        visualize()
    elif choice == '5':
        transpose()
    elif choice == '6':
        prod_sc()
    elif choice == '7':
        somma()
    elif choice == '8':
        prod_ab()
    elif choice == '9':
        try:
            (matrixA, matrixB) = switch()
        except:
            print("Matrices A and/or B don't exist")
    elif choice == '10':
        print("\nCIAO CIAO!!\n")
        break
    else:
        print("\nPlease, digit one of the suggested numbers...")
