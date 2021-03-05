import argparse

parser = argparse.ArgumentParser(description='Just a little rome->arab converter')

parser.add_argument( "-n", "--number", help = "Just write number after that (IVXLCDM format)" )

args = parser.parse_args()

rome = args.number
arab = 0
r_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, 'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}
while rome:
    if len(rome) > 1:
        if rome[:2] in r_dict:
            arab += r_dict[rome[:2]]
            rome = rome[2:]
            continue
    if len(rome) > 0:
        if rome[0] in r_dict:
            arab += r_dict[rome[0]]
            rome = rome[1:]
print(arab)
