def maxmin(arr):
    mx=float("-inf")
    mn=float("inf")
    for i in arr:
        if i>mx:
            mx=i
    for i in arr:
        if i<mn:
            mn=i
    return mx+mn
arr=list(map(int,input().split()))
print(maxmin(arr))