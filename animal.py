import sys
def cat():
    print('meow\n'*10)
def default():
    print('We Will Smash THEM all')
def main():
    if sys.argv[1]=='Cat':
        cat()
    else:
        default()
if  __name__=='__main__':
    main()
