from string import ascii_lowercase

wovel = set('eyuioa')
consonant = set(ascii_lowercase) - wovel

string = input()

print(len(set(string) & wovel), len(set(string) & consonant))