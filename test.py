num = input()
if num == '':
    num = 10
else:
    num = int(num)
lst = [1]
for number in range(2, num ** 2): 
    for i in range(2, number): 
        if(number % i) == 0: 
            break 
    else: 
        lst.append(number)
print(*lst[:num])