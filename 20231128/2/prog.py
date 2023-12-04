from math import inf
import sys

tags = {}
Approved_tags = []
code = []

def matcher(words):
    match words:
        case ['store', value, var]:
            code.append(' '.join(words))
        
        case ['add' | 'sub' | 'mul' | 'div', src, operand, dst]:
            code.append(' '.join(words))
    
        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle', \
                src, operand, tag]:
            Approved_tags.append(tag)
            code.append(' '.join(words))
            
        case ['out', var]:
            code.append(' '.join(words))
        
        case ['stop']:
            code.append(' '.join(words))
        
        case [word, *args]:
            match word[-1]:
                case ':':    
                    tags[word[:-1]] = len(code)
                    matcher(list(*args))
    

while (text := sys.stdin.readline()):
    words = text.split()
    matcher(words)

match len(Approved_tags) != len(set(Approved_tags)):
    case True:
        exit()
match len(tags.keys()) != len(set(tags.keys())):
    case True:
        exit()
match set(Approved_tags) != set(tags.keys()):
    case True:
        exit()

variables = {}
i = 0
while i < len(code):
    match code[i].split():
        case ['store', value, name]:
            variables[name] = float(value)
        case ['add' | 'sub' | 'mul' | 'div' as OP, src, operand, dst]:
            variables[src] = variables.setdefault(src, 0)
            variables[operand] = variables.setdefault(operand, 0)
            variables[dst] = variables.setdefault(dst, 0)
            match OP:
                case 'add':
                    try:
                        variables[dst] = variables[src] + variables[operand]
                    except Exception:
                        variables[dst] = inf

                case 'sub':
                    try:
                        variables[dst] = variables[src] - variables[operand]
                    except Exception:
                        variables[dst] = inf
                case 'mul':
                    try:
                        variables[dst] = variables[src] * variables[operand]
                    except Exception:
                        variables[dst] = inf
                case 'div':
                    try:
                        variables[dst] = variables[src] / variables[operand]
                    except Exception:
                        variables[dst] = inf

                    
        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle' as CMP,\
                src, operand, tag]:
            variables[src] = variables.setdefault(src, 0)
            variables[operand] = variables.setdefault(operand, 0)
            match CMP:
                case 'ifeq':
                    match variables[src] == variables[operand]:
                        case True:
                            i = tags[tag] - 1
                case 'ifne':
                    match variables[src] != variables[operand]:
                        case True:
                            i = tags[tag] - 1
                case 'ifgt':
                    match variables[src] > variables[operand]:
                        case True:
                            i = tags[tag] - 1
                case 'ifge':
                    match variables[src] >= variables[operand]:
                        case True:
                            i = tags[tag] - 1
                case 'iflt':
                    match variables[src] < variables[operand]:
                        case True:
                            i = tags[tag] - 1
                case 'ifle':
                    match variables[src] <= variables[operand]:
                        case True:
                            i = tags[tag] - 1

        case ['out', var]:
            variables[var] = variables.setdefault(var, 0)
            print(variables[var])
        case ['stop']:
            exit()

    i += 1