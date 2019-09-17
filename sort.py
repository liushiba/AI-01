'''
sort.py 冒泡排序
'''
def sprt(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    return L

l = [9,8,6,5,8,1,4,9,4]
print(sprt(l))
print(l)
