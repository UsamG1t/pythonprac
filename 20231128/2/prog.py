from math import inf
import sys
text = sys.stdin.read().split()

tags = {}
Approved_tags = []
code = []

for i in range(len(text)):
    match text[i]:
        case 'store':
            code.append(' '.join(text[i:i+3]))
            i += 2

        case 'add' | 'sub' | 'mul' | 'div':
            code.append(' '.join(text[i:i+4]))
            i += 3

        case 'ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle':
            Approved_tags.append(text[i+3])
            code.append(' '.join(text[i:i+4]))
            i += 3

        case 'out':
            code.append(' '.join(text[i:i+2]))
            i += 1

        case 'stop':
            code.append(text[i])

        case word:
            match word[-1]:
                case ':':    
                    tags[text[i][:-1]] = len(code)
    i += 1


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