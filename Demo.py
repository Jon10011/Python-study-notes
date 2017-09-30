from functools import reduce
def fn(x, y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2float(n):
    return reduce(fn, map(char2num,n.split('.')[0])) + reduce(fn, map(char2num,n.split('.')[1])) / pow(10,( len(n.split('.')[1])))

print('str2float(\'123.456\') =', str2float('123.456'))
dir = {'Range':100,'While':91,'For':79,'Int':65}
print(dir['Range'])
Set1 = set([12,23,32,54,1])
print(Set1[0])