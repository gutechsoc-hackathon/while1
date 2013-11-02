def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

count = 0
mem = 0
f = open("data.txt", 'r')
g = open("output2.txt", 'w')

for line in f:
    count = count + 1
    splitline = line.split()
    print splitline
    if splitline:
        if is_number(splitline[0]):
            mem = splitline[0]
        else:
            if splitline[0] != '{' or splitline[0] != '}':
                try:
                    g.write(mem + '\t' + splitline[0] + '\t' + splitline[1])
                except:
                    continue
                g.write('\n')
    if count % 1000000 == 0:
        print count

f.close()
g.close()

