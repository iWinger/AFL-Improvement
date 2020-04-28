import sys
import os
from cycle import Cycle

def main(*args):
    cycle = Cycle()
    cycle.readFile("sample_cycle.py")
    if(len(sys.argv) != 2):
        print('Error, you need to put in a function!')
        return
    method = globals()[sys.argv[1]]
    cycle.calculate(method)
    cycle.has_loop(method)
    cycle.has_decisions(method)
    cycle.has_exit_points(method)
    cycle.evaluateComplexity()
    
#Output should be 3
def example_one(a,b):
    if a and b:
        x = 5
    else:
        x = 3


#The resulting cyclomatic complexity should be 3. This is code from https://www.tutorialspoint.com/software_testing_dictionary/cyclomatic_complexity.htm
def example_two(a,b,c):
    if a == 10:
        if b > c:
            a = b
        else:
            a = c

    print(a)
    print(b)
    print(c)

#Output should be 2
def example_three(a_list):
    for element in a_list:
        if element > 5:
            element = 3
 
    return None

def example_four(a_list,b_list):
    i = 10
    for a in a_list:
        if a > 5 and b > 3:
            if a > 6:
                a = 10
                if a > 7:
                    a = 11
                    if a > 9:
                        a = 15
                    else: 
                        a = 30
                else:
                    a = 20
            else:
                a = 9
            a = 7
        else:
            b = 6
    while(i < 30):
        if i > 15:
            if i > 17:
                i + 2
                if i > 19:
                    if i > 20:
                       break
                    i + 3
                else:
                    i + 4
            else:
                i + 3
            i = i + 1
        else:
            i = i + 2
        i+=1
        
    return None


if __name__ == '__main__':
    main()
