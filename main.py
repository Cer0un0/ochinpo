import random as ra

def main(keyword='おちんぽ'):
    slist = list(keyword)
    slen = len(slist)
    
    o = ''
    is_orgasm = False
    while is_orgasm == False:
        o += ra.choice(slist)
        if o[-slen:] == ''.join(slist):
            print (f'{o}\nイグゥゥゥ\nあなたは{len(o)}回目でイキました')
            is_orgasm = True

if __name__ == '__main__':
    try:
        main(input())
    except IndexError:
        main()
