s=input()
max_length=0
stack=[-1]
cnt=1
for i ,ch in enumerate(s):
    if ch=='(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            length=i - stack[-1]
            if length > max_length:
                max_length=length
                cnt =1
            elif length==max_length:
                cnt+=1
        
    
if max_length ==0:
    print("0 1")
else:
    print(max_length , cnt)