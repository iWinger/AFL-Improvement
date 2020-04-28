# AFL-Improvement

## Objective

American Fuzzy Lop Improvement is a project designed to **find security vulnerabilities** in software. Fuzzing is the idea of taking random inputs and essentially brute-forcing them to see if we crash somewhere in the program, which would expose the vulnerability. Our objective is to find a metric other than code coverage, such as nested method depth.

### How To Run
cd into directory ~/AFL-Improvement/AFL_VIRTUALENV/AFL-augment/OUR_CODE
[example_one, example_two, example_three, example_four]
Examples)
python r_cycle.py example_two
=> This will generate a detailed documentation on the results of the new metric cyclomatic complexity.
python r_cycle.py example_four
=> This will generate a McCabe Cyclomatic Complexity score of 11 (which signals that we might need to refactor code)

### Why
Instead of improving existing features, our team decided to create our own new metric to add an improvement to AFL. We believe cyclomatic complexity would help in terms of refactoring the code if it is too complex, eliminating bugs that would remain hidden. This means that this code does not support Google Suites / LAVA because we are adding a new metric in, and not improving existing ones.
Cyclomatic complexity is extremely useful because it helps with testability and maintainability. Testability and maintainability take up a huge amount of time in the software development cycle, and it is crucial that we do all we can to streamline the process. By running this program, you would easily be able to tell if you need to refactor the code or not based on the algorithm we produced. We included a rating score in the output to show how each example stacks up against the cyclomatic complexity test. 

## How It Works
We calculated cyclomatic complexity through the formula (E-N+2xP), where E = number of edges, N = number of nodes, and P = number of exit points. We walked through the AST (Abstract Syntax Tree) and found corresponding nodes, such as If / While / Return nodes, and calculated the edges accordingly, and the exit points as well. The reason why we decided to use an AST, was to detect nested if statements, because that would change the calculations as opposed to parsing tokens.

## Collaborators (GitHub users):

iWinger (Contribution: 20pts/20)
lawyang14 (Contribution: 18pts/20)
amurao1998 (Contribution: 18pts/20)
Rutgers-Yang-Bao (Contribution: 5pts/20) 
sabackwon (Contribution: 5pts/20)
pinkjim  (Contribution: 5pts/20)
