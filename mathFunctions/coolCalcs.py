## function to add two numbers
def addNumbers(number1, number2):
    '''provise 2 numbers as parameteres. 
    function returns total
    '''
    return number1 + number2
    
## function to subtract two numbers
def subNumbers(number1, number2):
    '''provide 2 numbers as parameters. 
    function subtracts 2 from 1, returns total.
    '''
    return number1-number2

## function that gathers all files ina folder together
import glob
def gatherFiles(path):
    '''
    provide path as string with file pattern (e.g. *.csv)
    returns all target files in a list'''
    return glob.glob(path)