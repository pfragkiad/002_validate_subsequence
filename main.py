# Validate subsequence

# Subsequence some elements of the original array, with some or no deleted elements in-between
# O(n²) | O(1) space
def is_valid_subsequence(array, subsequence):
    la = len(array) ; ls = len(subsequence)
    if ls>la:
        return False
    
    L = 0 #pointer of current subsequence element in the array
    for i in range(0,ls): #i is a counter for the subsequence
        if la-L < ls-i:
            return False

        found = False
        for j in range(L,la):
            if subsequence[i] == array[j]:
                L=j+1
                found = True
                break  #proceed with next i
        if not found:
            return False
    return True

#THAT is order n!
# O(n) time | O(1) space
def is_valid_subsequence_while(a,s):
    ai=0;si=0 # indices
    while ai<len(a) and si<len(s): #αρκεί το ένα από τα 2
        if a[ai] == s[si]:
            si+=1
        ai+=1
    return si==len(s)

# O(n) time | O(1) space
def is_valid_subsequence_for2(a,s):
    si=0
    for ai in range(0,len(a)):
        if a[ai] == s[si]:
            si+=1
            if si == len(s): #καλύτερο από το να έχουμε από πριν
                return True #immediately return True no need to break

    return False

# both arrays are said to be non-empty
a = [5,1,22,25,6,-1,8,10]
s = [1,6,-1,10]
s=[1]
s=[5,8,10]
#s=[5,8,11]

print(is_valid_subsequence(a,s))
print(is_valid_subsequence_while(a,s))
print(is_valid_subsequence_for2(a,s))



