import csv
import subprocess as subp


with open('./Requires/test-01.csv','r') as file_pointer:
    cr = csv.reader(file_pointer)
    next(cr)
    next(cr)
    next(cr)
    next(cr)
    next(cr)
    l1 = []
    try:
        for line in cr:
            # print(line[13]+","+line[0])
            l1.append(line[0])

                   


    except Exception as e:
        pass
    with open('./Requires/network2.csv','a') as f2:
        f2.truncate(0)
        for item in l1:
            f2.write(item+"\n")
