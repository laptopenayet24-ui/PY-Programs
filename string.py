def func():
    s=input("Enter a string: ")
    rs=''
    for i in s:
        if i in 'AEIOUaeiou':
            rs+="*"
        else:
            rs+=i
    return rs
print(func())