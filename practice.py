#列表增加元素
#append()在末尾追加一个元素   list.append(追加的元素)
#insert()在指定位置追加元素   list.insert(下标位置，具体值)
#extend()在末尾追加多个元素   list.extend([多个值])

#定义一个列表
a=[1,2,3,4,'a1','a2']
#a.append(5)
#a.insert(5,9)
a.extend(['hello'])
print(a)
#列表删除元素
# a.pop()删除最后一个元素
# a.pop(4)删除指定下标第四个元素
# a.remove(4)删除4这个元素
# def a[4]删除指定下标第四个元素