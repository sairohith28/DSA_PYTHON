cap=int(input("enter the capacity of knapsack:"))
m=int(input("enter no of objects:"))
pro,wt,p=[],[],0
print("enter the weights:")
for j in range (m):
    wt.append(int(input()))
print("enter the profits:")
for i in range (m):
    pro.append(int(input()))
def knap(values,weights,cap):
    p=0
    def pw(i) :return values[i]/weights[i]
    items=sorted(range(m),key=pw,reverse=True)
    for i in items:
        if(cap>0 and wt[i]<=cap):
            cap=cap-wt[i]
            p=p+pro[i]
        else:break
    if(cap>0):
        pi=pro[i]*(cap/wt[i])
        p=p+pi
    print("the maximum profit obtained is :",p)
knap(pro,wt,cap)






