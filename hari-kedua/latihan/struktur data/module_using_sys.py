import sys

print('Command line arguments are :')
for i in sys.argv :
    print(i)


print('\n\nPython path is ', sys.path, '\n')



# $ python module_using_sys.py we are arguments    # each arg is separated by white space
# The command line arguments are:
# module_using_sys.py
# we
# are
# arguments
