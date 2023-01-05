''' Remove Minimum Number of Elements Such That no Common Element Exist in both Array
A[]={ 1, 2, 1, 1}

B[]= {1, 1}

Output: 3 
'''

def minElements(a,b):

    countA = dict((i,a.count(i)) for i in a)
    countB = dict((i,b.count(i)) for i in b)
    
    lenA = len(countA)
    lenB = len(countB)
    
    if lenA < lenB :
        countB,countA = countA,countB


    found = { num:countB[num] for num in countA if num in countB }
    
    return list(found)[0]



a=[2, 3, 2, 2, 0, 4]
b=[4, 4, 2, 20,4,4,4,4] 
print(minElements(a,b))
