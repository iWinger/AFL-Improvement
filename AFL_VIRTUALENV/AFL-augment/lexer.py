# Lexical analysis
import ply.lex as lex
import re
import sys
import os
# This is the token list to feed into the lexer
tokens = (
        'NUMBER', 
        'PLUS', 
        'MINUS', 
        'TIMES', 
        'DIVIDE', 
        'LPAREN', 
        'RPAREN',
        'FOR',
        'WHILE',
        'IF',
        'AND',
)
'''
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
'''
t_FOR = r'for'
t_WHILE = r'while' # This should cover do while / while
t_IF = r'if'
t_AND = r'&&' # Translates to another if condition

'''
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t
'''

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = " \t"

def t_error(t):
   # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

