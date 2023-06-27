# stack = []
# stack.append(10)
# stack.append(20)
# print(stack)
# print(stack.pop())
# print(len(stack)==0)
st=[]
limit=int(input("enter limit of stack"))
def push():
    if len(st)==limit:
        print("list is full")
    else:
        ele=input("enter element:")
        st.append(ele)
        print(st)
def pop():
    if not st:#empty()
        print("stack is empty")
    else:
         st.pop()
         print(st)
while True:
    print("select 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter correct operation")