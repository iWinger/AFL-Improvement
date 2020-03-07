import sys
import os
from cycle import Cycle

def main():
    cycle = Cycle("tokens")
    cycle.readFile("test-instr.c")
    cycle.calculate()
    cycle.evaluateComplexity()
    
    return None

if __name__ == '__main__':
    main()
