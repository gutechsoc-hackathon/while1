'''
1 1
1 2
1 3
1 4
1 5
2 1
2 3
3 4
3 5
3 6
4 1
4 2
5 3
5 4
5 6
6 4
6 5
6 6
8 8



graph = {
'1':['1','2','3','4','5'],
'2':['1','3'],
'3':['4','5','6'],
'4':['1','2'],
'5':['3','4','6'],
'6':['4','5','6'],
'8':['8']
    }
'''

graph = {}

maxim = 0
mem = 0

old = -1

f = open('input.txt', 'r')
for line in f:
	splitLine = line.split()
	if ( old != splitLine[0] ):
		graph[splitLine[0]] = []
		old = splitLine[0]
	graph[splitLine[0]] += splitLine[1]

f.close()

#print graph


def tarjan(graph):
    #result = []
    stack = []
    low = {}    
    def visit(node):
        if node in low:
            return
        num = len(low)
        low[node] = num
        stack_pos = len(stack)
        stack.append(node)

        for successor in graph[node]:
            visit(successor)
            low[node] = min(low[node], low[successor])
        
        if num == low[node]:
            component = tuple(stack[stack_pos:])

            global maxim
            if len(component) > maxim:
                maxim = len(component)
                global mem
                mem = component
                
            del stack[stack_pos:]
            #result.append(component)
            for item in component:
                low[item] = len(graph)
            
    for node in graph:
        visit(node)
    #return result

tarjan(graph)
print mem
