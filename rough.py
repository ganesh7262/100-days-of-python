fruits=['apple','orange','pear']

def make_pie(index:int)->str:
    try:
        fruit=fruits[index]
        print(f'{fruit} pie')
    except IndexError as err:
        print('No such fruit exists')
    else:
        print(f'{fruit} pie')


make_pie(int(input('Enter the index: ')))