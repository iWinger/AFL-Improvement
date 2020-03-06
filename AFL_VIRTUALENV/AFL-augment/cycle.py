# Lexical analysis
import ply.lex as lex
from lexer import lexer
import re
import sys
import os

class Cycle:
    def __init__(self,keywords,program):
        self.keywords = keywords
        self.program = program

    def calculate(tokens): 
        data =  '''for3 + 4 * 10 + -20 *2'''
        # Give the lexer some input
        lexer.input(data)
                 
        # Tokenize
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input
            print(tok)

        
    
    def readFile(program):
        myfile = open(program, "r")
        print(myfile.read(5))
