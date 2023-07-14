def equilibrium_index(arr):
    pref_arr=[]
    pref_arr.append(arr[0])
    for i in range (1,len(arr)):
        pref_arr.append(pref_arr[i-1]+arr[i])
    n=len(arr)
    for i in range (0,n):
        if pref_arr[i-1]==pref_arr[n-1]-pref_arr[i]:
            return i
    return -1
            
print(equilibrium_index(list(map(int,input().split()))))