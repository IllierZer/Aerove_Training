def palindrome(n):
    rev=0
    k=n
    while(k!=0):
        rev=rev*10+(k%10)
        k=int(k/10)
    if(rev==n):
        return True
    else:
        return False
    

p=int(input("enter a palindrome: "))
x=p+1
if(palindrome(p)):
    while(1>0):
        if(palindrome(x)):
            break
        else:
            x=x+1
            continue
    print("next smallest palindrome is: ",x)
else:
    print("given number isnt a palindrome..")
        

