import argparse

parser = argparse.ArgumentParser(description='Just a little rome->arab->rome converter')

parser.add_argument( "-tr", "--torome", help = "Just write number after that (0-9 format)" )

parser.add_argument( "-ta", "--toarab", help = "Just write number after that (IVXLCDM format)" )

args = parser.parse_args()

if args.toarab:
    
    rome = args.toarab
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
    print(args.toarab, 'is equals',arab)

elif args.torome:
    
    arab = int(args.torome)
    r_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    r_dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    rome = ''
    for x in r_list:
        if (arab - x*3) >= 0:
            arab = arab - x*3
            rome += (r_dict[x])*3
        elif (arab - x*2) >= 0:
            arab = arab - x*2
            rome += (r_dict[x])*2
        elif (arab - x) >= 0:
            arab = arab - x
            rome += (r_dict[x])
    print(args.torome,'pares esse',rome)
