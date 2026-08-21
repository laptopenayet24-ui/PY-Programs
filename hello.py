def check_even(n):
    if n%2==0:
        return True
    return False
def call():
    n=int(input("Enter the no:-"))
    if check_even(n):
        print("Even Number")
    else:
        print("Odd No")
call()
#----------------------------------------------------