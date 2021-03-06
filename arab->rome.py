import argparse

parser = argparse.ArgumentParser(description='Just a little arab->rome converter')

parser.add_argument( "-n", "--number", help = "Just write number after that (0-9 format)" )

args = parser.parse_args()

arab = int(args.number)
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
print(rome)
