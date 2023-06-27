n=int(input("enter the no of elements:"))
weights=[]
values=[]
print("enter the weights:")
for i in range(n):
    weights.append(int(input()))
print("enter the values:")
for i in range(n):
    values.append(int(input()))
print("enter the capacity:")
capacity=int(input())
def profit(capacity,n):
    if (n==0 or capacity==0):
        return 0
    if(weights[n]<=capacity):
        return max(values[n]+profit(capacity-weights[n],n-1),profit(capacity,n-1))
    else: 
        return profit(capacity,n-1)
print("the maximum profit we can acheive is:",profit(capacity,n-1))