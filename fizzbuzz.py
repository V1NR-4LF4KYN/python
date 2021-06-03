#python3

'''
The Players count. When they get to 3 - any multiple of 3 - they have to say "FIZZ"
And any mutliple of 5 they say "BUZZ"
If their number is a multiple of 3 And 5 the have to say "FIZZBUZZ"

'''

# funcs
def forloop():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZBUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            print(i)

# main-loop
def main():
    forloop()

# calling main func
main()