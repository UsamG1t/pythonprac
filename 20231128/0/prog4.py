while s := input():
    match s.split():
        case ["mov", r1, r2]:
            print(f'moving {r2} to {r1}')
        case['push'|'pop' as cmd, *var]:
            print(f'{cmd}ing', *var)
        case [cmd, r1]:
            print(f'making {cmd} with {r1}')
        case _:
            print('Parse Error')
