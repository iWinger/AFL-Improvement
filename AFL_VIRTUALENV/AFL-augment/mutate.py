#This is a python file that should recursively check through the files supplied by the argument and then modify seed selection

import os
import sys
import angr # suite of python libraries for symbolic execution


class Mutate(object):
    ''' This is the class for mutating seeds '''
    def __init__(self, input_str, fuzz_bitmap, argv=None):
        self.input_str = input_str
        self.fuzz_bitmap = fuzz_bitmap
        self.argv = argv

    def mutate(self):
                

