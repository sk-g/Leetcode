## Given a time HH:MM in 24hr format
## output the earliest time possible
## with the permutation of the input time

## Eg: 11:00 --> 00:11
## Eg: 23:59 --> 23:59 : because no valid
## earliest permutation

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import permutations
#from operator import 
def solution(S):
    # write your code in Python 3.6
    s = (''.join([i for i in list(S) if i != ':'])) #string
    orgh,orgm=s[:2],s[2:]
    perms2 = [''.join(p) for p in permutations(s)]
    perms = []
    for el in perms2:
        if el not in perms:
            perms.append(el)
    lot=[]
    for j in range(len(perms)):
        word=perms[j]
        if word!=s:
            permh,permm=word[:2],word[2:]
            timediff=difftime(orgh,orgm,permh,permm)
            lot.append((word,timediff))
        else:
            continue;
    lot.sort(key = lambda tup:tup[1])
    #print("lot",lot)   
    
    first = lot[0]
    firsttime = first[0]
    if int(firsttime[2:])>60:
        return S
    else:
        
        res = list(str(firsttime))
        res.insert(2,':')
        #return(''.join([i for i in list(str(s))]))
        return(''.join([i for i in res]))
        #return (list(firsttime).insert(2,':'))
    
        
    
def geth(ss):
    # returns hours
    return int(ss[:2])
    
def getm(ss):
    # returns minutes
    return int(ss[2:])

    t1h,t1m=geth(t1),getm(t1) 
    t2h,t2m=geth(t2),getm(t2)


def difftime(t1h,t1m,t2h,t2m):
    # function that computes
    # difference between two times
    if int(t1h)>int(t2h):
        return difftime(t1h,t1m,int(t2h)+24,t2m)
    if int(t1m)>int(t2m):
        return difftime(t1h,t1m,int(t2h)-1,int(t2m)+60)
    return (int(t2h)-int(t1h))*60+(int(t2m)-int(t1m))
        

    pass