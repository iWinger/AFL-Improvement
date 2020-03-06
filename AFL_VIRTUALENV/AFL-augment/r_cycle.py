import sys
import os
from cycle import Cycle

def main():
    cycle = Cycle("tokens", "program")
    return cycle.calculate()

if __name__ == '__main__':
    main()
