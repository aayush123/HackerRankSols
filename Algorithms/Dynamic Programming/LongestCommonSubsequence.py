def lcs(s1,s2,n,m,dp_arr):
    #print(n,m)
    if(dp_arr[n][m] != ['-']):
        return dp_arr[n][m]
    else:
        if(n==0 or m==0):
            result = ['-']
        elif(s1[n-1] == s2[m-1]):
            res = lcs(s1,s2,n-1,m-1,dp_arr)
            if(res != ['-']):
                result = [s1[n-1]] + lcs(s1,s2,n-1,m-1,dp_arr)
            else:
                result = [s1[n-1]]
        else:
            res1 = lcs(s1,s2,n,m-1,dp_arr)
            res2 = lcs(s1,s2,n-1,m,dp_arr)
            if(len(res1) > len(res2)):
                result = res1
            else:
                result = res2
    dp_arr[n][m] = result
    return result

n,m = [int(x) for x in input().split()]
s1 = [int(x) for x in input().split()]
s2 = [int(x) for x in input().split()]
dp_arr = [[['-']]*(n+1)]*(m+1)

for n_temp in range(n):
    for m_temp in range(m):
        returns = lcs(s1,s2,n_temp,m_temp,dp_arr)
        print(returns)
#for each_row in dp_arr:
#    print(each_row)
