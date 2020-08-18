print('reloading...')
from c3 import basic
a = input()
jiami_str = ''
def getkey(dic,value):
    for k in dic.keys():
        if dic[k] == value:
            return k            
for i in list(a):
    s = getkey(basic,i)
    if s:
        jiami_str += ' '+s
    else:
        jiami_str += ' '+'■'
jiami_str_ac = ''
for i in list(jiami_str):
    jiami_str_ac += str(ord(i))+' '
print(jiami_str_ac)     
input('exit')       