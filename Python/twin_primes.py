def prime(n):
    c=0
    for x in range(2,n):
        if (n%x==0):
            c=c+1
        else:
            continue
    if(c==0):
        return True
    else:
        return False


outfile=open("myFirstFile.txt","w")
d=int(input("enter the value of d: "))
for x in range(10**(d-1),10**d):
    if(x==1):
        continue
    if(prime(x) & prime(x+2)):
        outfile.write(str(x)+" "+str(x+2))
        outfile.write("\n")
outfile.close()
