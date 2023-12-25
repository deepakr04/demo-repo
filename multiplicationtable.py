def multipleTable(m, n):
    print("Multiplication table by DR")

    print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15')
    print('--+---------------------------------------------------------------')
    # Display each row of products:
    for n1 in range(m, n):
        print(str(n1).rjust(2), end='')
        print('|', end='')
        for n2 in range(m,n):
            print(str(n1*n2).rjust(3), end=' ')
        print()

if __name__ == '__main__':
    start = 0
    end = int(input("Enter the Number, which Prints the Table upto : "))
    multipleTable(start, end)