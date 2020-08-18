from . import c3 
basic = c3.basic
def jiema(jiami_ac):
    jiami_zz = ''
    for i in jiami_ac.split():
        jiami_zz +=chr(int(i))
    jiemi_str = ''
    for i in jiami_zz.split():    
        j = basic.get(i)
        if j:
            jiemi_str += j
        else:
            jiemi_str += '■'
    return jiemi_str
