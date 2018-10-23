import csv

def f():
    file = open('Test.csv')
    data = csv.reader(file)

    rlist = []
    i = 0
    enames = ['id','year','rain']
    for line in data:
        rlist.append({})
        for j in range(len(line)):
            if j == 0:
                rlist[i][enames[j]] = int(line[j])
            else:
                if float(line[j])%1 == 0:
                    rlist[i][enames[j]] = int(line[j])
                else:
                    rlist[i][enames[j]] = float(line[j])

        i = i + 1

    return rlist

def g(start=0,end=0):
    full_data = f()

    if start:
        if end:
            subdata = []
            for i in range(len(full_data)):
                if full_data[i]['year'] >= int(start) and full_data[i]['year'] <= int(end):
                    subdata.append(full_data[i])
        else:
            subdata = []
            for i in range(len(full_data)):
                if full_data[i]['year'] >= int(start):
                    subdata.append(full_data[i])
    else:
        if end:
            subdata = []
            for i in range(len(full_data)):
                if full_data[i]['year'] <= int(end):
                    subdata.append(full_data[i])
        else:
            subdata = full_data

    return subdata

def h(limit=len(f()),offset=0):
    full_data = f()

    subdata = []
    if limit:
        if offset:
            subdata = full_data[int(offset):int(offset) + max(min(int(limit),len(full_data)),0)]
        else:
            subdata = full_data[0:max(min(int(limit),len(full_data)),0)]
    else:
        if offset:
            subdata = full_data[int(offset):]
        else:
            subdata = full_data
    return subdata



func = input('Which function would you like to run? (a for f(), b for g(), c for h())?\n')

if func == 'a' or func == 'a)' or func == 'f':
    print(f())

elif func == 'b' or func == 'b)' or func == 'g':
    s = input('What start date would you like to use?\n')
    e = input('What end date would you like to use?\n')

    print(g(s,e))

elif func == 'c' or func == 'c)' or func == 'h':
    l = input('What would you like the limit to be?\n')
    ofs = input('What would you like the offset to be?\n')

    print(h(l,ofs))

else:
    print('Please try using one of the specified functions.\n')
