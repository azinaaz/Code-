file = open("problem.txt" , "r")
content = file.readlines()
print(content)
cal = []
for x in content:
    cal_num = []
    for i in range(len(x)):
        if x[i].isnumeric():
            cal_num.append(x[i])
    cal.append(int(cal_num[0] + cal_num[-1]))
print(sum(cal))
    

    
file.close()



