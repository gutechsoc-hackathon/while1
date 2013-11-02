def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

count = 0
f = open("relationships.txt", 'r')
g = open("output.txt", 'w')

for line in f:
    count = count + 1
    splitline = line.split()
    if splitline:
        if is_number(splitline[0]):
            g.write(splitline[0]+':')
        else:
            if len(splitline[0]) == 1:
                if splitline[0] == '{':
                    l = [[],[],[],[],[]]
                else:
                    for i in range(4):
                        for j in range(len(l[i])):
                            g.write(l[i][j])
                            if j != len(l[i])-1:
                                g.write(' ')
                        if i != 4:
                            g.write(':')
                    g.write('\n')
            else:
                if splitline[0] == "DISLIKES":
                    l[0].append(splitline[1])
                if splitline[0] == "FRIEND_OF":
                    l[1].append(splitline[1])
                if splitline[0] == "KNOWS":
                    l[2].append(splitline[1])
                if splitline[0] == "MARRIED_TO":
                    l[3].append(splitline[1])
                if splitline[0] == "HAS_DATED":
                    l[4].append(splitline[1])
    if count % 1000000 == 0:
        print count


f.close()
g.close()

