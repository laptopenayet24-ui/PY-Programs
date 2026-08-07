def lcm(a,b):
    c=2
    while True:
        if c%a==0 and c%b==0:
            return c
        c+=1
        if c==80099999:
            return a*b
#--------------------------------------------------------------
def hcf(a,b):
    c=2
    while True:
        if a%c==0 and b%c==0:
            return c
        c+=1
        if c==80099999:
            return 1
#---------------------------------------------------------------------
a=int(input("Enter 1st number\n"))
b=int(input("enter 2nd number\n"))
print(f"The HCF of {a} and {b} is {hcf(a,b)}")
print(f"The LCM of {a} and {b} is {lcm(a,b)}")
