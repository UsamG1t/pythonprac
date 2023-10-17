from math import *
func_dict = {}
defin_count = worked_strings = 0

while (s := input()):
    if s[0] == ':':
        name, *args, func = s[1:].split()
        func_dict[name] = f"lambda {', '.join(args)}: {func}"
        defin_count += 1
        worked_strings += 1
    else:
        name, *params = s.split()

        if name != 'quit':
            print(eval('(' + func_dict[name] + ')' + f"({', '.join(params)})" ))
            worked_strings += 1
        else:
            defin_count += 1
            worked_strings += 1
            params = ' '.join(params)
            
            for i in params[1:len(params) - 1]:
                if i == '{':
                    print(defin_count if defin_count != -1 else worked_strings, end = '')
                    defin_count = -1
                elif i != '}':
                    print(i, end = '')
            print()
            exit()