import sys
def cat():
    print('Meow2!')
def dog():
    print('Woof2!')
def default():
    print('Hello2 i am default')

def main():
    if sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1] == 'dog':
        dog()
    else:
        default()
if __name__ == '__main__':
    main()
