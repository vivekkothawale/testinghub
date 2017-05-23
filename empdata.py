fh=open("C:/test/emp.dat.txt","a+")

empno=input("enter the empno:")
sal=input("enter the salary:")
empname=input("enter the empname:")
desig=input("enter the designation:")
x=str(empno+":"+empname+":"+sal+":"+desig+"\n")
print(x)

fh.write(x)
fh.close()

