l=[30,31]*5
l.pop(0)

l[1]=28

l.insert(7,31)
l.extend([30,31])
# print(l)
a=input("请输入一个1-12之间的数字")
a=int(a)
print(f'{a}月份有{l[a-1]}天')