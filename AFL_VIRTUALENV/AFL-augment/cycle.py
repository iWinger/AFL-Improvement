'''
Lexical analysis for cyclomatic complexity.
To calculate cyclomatic complexity, apply the given formula: 
E (Number of edges in flow chart ) - N (Number of nodes in flow chart) + 2P (Number of nodes that have exit points)
'''

import ply.lex as lex
from lexer import lexer
from collections import defaultdict
import re
import sys
import os

class Cycle:
    def __init__(self,keywords,dictionary=defaultdict(int),edges=0, nodes=0, connected=0):
        self.keywords = keywords # Array of tokens
        self.dictionary = dictionary
        self.edges = edges
        self.nodes = nodes
        self.connected = connected

    def calculate(self):
        lexer.input(self.keywords)
        while True:
            tok = lexer.token()
            if not tok: 
                break      
            if tok.type == "IF":
                self.dictionary["IF"] += 1
            elif tok.type == "AND":
                self.dictionary["AND"] += 1
            elif tok.type == "FOR":
                self.dictionary["FOR"] += 1
            elif tok.type == "WHILE":
                self.dictionary["WHILE"] += 1
            
                 
            
    def evaluateComplexity(self):
        for key in self.dictionary:
            self.nodes += self.dictionary[key]

            if key == "IF":
                print('The number of ' + key + ' statements are: ' + str(self.dictionary[key]))
            elif key == "AND":
                print('The number of ' + key + ' statements are: ' + str(self.dictionary[key]))
            elif key == "FOR":
                print('The number of ' + key + ' loops are: ' + str(self.dictionary[key]))
            elif key == 'WHILE':
                print('The number of ' + key + ' loops are: ' + str(self.dictionary[key]))
        
        print('The number of nodes are: ' + str(self.nodes))
    
    def readFile(self,program):
        with open(program, "r+") as myfile:
            for line in myfile:
                self.keywords += line
            
