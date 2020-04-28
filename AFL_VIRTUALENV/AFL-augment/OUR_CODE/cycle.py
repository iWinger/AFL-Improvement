'''
Lexical analysis for cyclomatic complexity.
To calculate cyclomatic complexity, apply the given formula: 
E (Number of edges in flow chart ) - N (Number of nodes in flow chart) + 2P (Number of nodes that have exit points)
Or, another formula is the number of decisions + 1
'''
import ply.lex as lex
from lexer import lexer
from collections import defaultdict
import re
import ast
import inspect
import symtable
import sample_cycle

class Cycle:
    def __init__(self,keywords="",dictionary=defaultdict(int),edges=0, nodes=0, exit_points=0, astInfo=[]):
        self.keywords = keywords # Array of tokens
        self.dictionary = dictionary
        self.edges = edges
        self.nodes = nodes
        self.exit_points = exit_points
        self.astInfo = []
        
    def calculate(self,function):
         print(inspect.getsource(function)) 
         lexer.input(inspect.getsource(function))
        
        #Tokenize
         
         while True:
             tok = lex.token()
             if not tok:
                 break
             if tok.type == 'ELSE':
                 self.edges += 2
                 self.nodes += 1
        

    ''' This function checks if a function has a loop or not. '''
    def has_loop(self,function):
        loops = ast.For, ast.While
        container = []
        towalk = ast.parse(inspect.getsource(function))
        #print(towalk.
        nodes = ast.walk(towalk)
       # table = symtable.symtable(self.keywords, "sample_cycle.py", "exec")
       # print(self.keywords)
       # print(table.get_children()[0].get_identifiers())

         
        ''' Steps into the debugger and looks at the number object to evaluate '''
        for node in nodes:
            if isinstance(node, ast.For):
                sub_container = []
                #print(ast.dump(node))
                self.astInfo.append(ast.dump(node))
                # This steps into the generator code
                # print([n for n in nodes])
                start_variable = node.target.id
                #print(start_variable.operand_value)
                #exec(compile(start_variable, filename="<cast>", mode="exec"))
                #extra_nodes = ast.walk(ast.parse(inspect.getsource(function)))
                #for ex in extra_nodes:
                 #   if ex.id == start_variable:
                  #      print('hi')

                #print(ast.literal_eval(start_variable))
                # This number is the end range variable.
                #end_range = node.iter.args[0]
                
                container.append("for")
               # sub_container.append(ast.literal_eval(end_range))
            
                
            elif isinstance(node,ast.While):
                sub_container = []
                self.astInfo.append(ast.dump(node)) 
                #print(ast.dump(node))
                start_variable = node.test.left.id
                #table.lookup("string").is_assigned()
                

                number = node.test.comparators[0]
                container.append("while")
                #sub_container.append(ast.literal_eval(number))
        for loop in container:
            self.nodes += 2

        for loop in container:
            self.edges += 2
            
        

        return container

    def has_decisions(self, function):
        decisions = ast.If
        container = []
        nodes = ast.walk(ast.parse(inspect.getsource(function)))

        for node in nodes:
            if isinstance(node, ast.If): 

                self.astInfo.append(ast.dump(node))
                container.append("if")
                if isinstance(node.body[0],ast.If):
                    self.nodes += 1
                    self.edges += 1
                    
                # Now we have to count the number of ands ==> nested ifs

            elif isinstance(node, ast.And):
                #print(ast.dump(node))
                self.astInfo.append(ast.dump(node))
            
                container.append("and")
                
        
        for decision in container:
           if decision is 'if':
               self.nodes += 2
           elif decision is 'and':
               self.nodes += 2
          # else:
           #    self.nodes += 1
        
        for decision in container:
            self.edges += 2

        return container
        
    def has_exit_points(self, function):
        exits = ast.Return
        container = []
        nodes = ast.walk(ast.parse(inspect.getsource(function)))
        has_exit = False

        for node in nodes:
            if isinstance(node, ast.Return):
                has_exit = True

                self.astInfo.append(ast.dump(node))
                #print(ast.dump(node))
                container.append("return")
                

            elif isinstance(node, ast.Break):

                self.astInfo.append(ast.dump(node))
               # print(ast.dump(node))
                has_exit = True
            
                container.append("break")
                
        
        if has_exit is True:
            for exit in container:
                self.exit_points += 1;
        else:
            self.exit_points = 1 # End of the program
        #Evaluate number of exit_points    
    

        return container

            
    def evaluateComplexity(self): 
        print('This is the abstract syntax tree information regarding important nodes: ')
        print('------------------------------------------------------------------------')
        for astnode in self.astInfo:
            print(astnode)
        print('-------------------------------------------------------------------------')

        print('The number of edges are: ' + str(self.edges))
        print('The number of nodes are: ' + str(self.nodes))
        print('The number of exit points are: ' + str(self.exit_points))
        print('Cyclomatic complexity is calculated by: ' + ' E - N + 2P => ' + str(self.edges - self.nodes + 2*self.exit_points))
        print('Rating scale:')
        print('1-10 = Low risk')
        print('11-20 = Moderate risk')
        print('21-50 = High risk')
        print('>50 = Very complex and needs refactoring')

    def readFile(self,program):
        with open(program, "r+") as myfile:
            for line in myfile:
                self.keywords += line
            
