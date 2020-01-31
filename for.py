# #请用户输入五个数字，组成一个列表，再将列表中每个元素*2，计算这个列表中所有元素的值
# l=[]
# for i in range(5):
#     a=input(f"请输入第{i+1}个数字")
#     a=int(a)
#     l.append(a)
# print(l)
# for i in range(len(l)):
#     l[i]=l[i]*2
# print(f"各个元素组成的五个数*2是:{l}")
# sum=0
# for i in l:
#     sum=sum+i
# print(f"新列表中所有元素值的和为{sum}")
#找出100以内所有七的倍数和所有含七的数
l=[]
for i in range(100):
    a=i%10
    b=i//10%10
    if i%7==0 or (a==7 or b==7):
        l.append(i)
print(f"100以内所有七的倍数和所有含七的数:{l}")
