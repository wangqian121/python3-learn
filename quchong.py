


def isOrderNumeric(num):
    order=[]
    for index in range(len(num)):
        if index+1 < len(num):
            if(num[index+1]-num[index])==1:
                order.append(num[index])
            else:
               if 0!=index and num[index-1]-num[index]==1:
                  order.append(num[index])
        else:
           if num[index ] - num[index-1] == 1:
               order.append(num[index])
    return order;

if __name__ == '__main__':
    str = ("abcd123edf12345gg567")
    num = []
    for i in range(len(str)):
        if str[i].isdigit():
            num.append( int(str[i]))
    print(num)
    print(max(isOrderNumeric(num)))