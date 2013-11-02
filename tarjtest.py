graph = {
    'a':['b'],
    'b':['c'],
    'c':['d'],
    'd':['e'],
    'e':['f'],
    'f':['j','g'],
    'g':['h'],
    'h':['i'],
    'i':['a'],
    'j':['a']
    }

maxim = 0
mem = 0

def tarjan(graph):
    result = []
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
            result.append(component)
            for item in component:
                low[item] = len(graph)
            
    for node in graph:
        visit(node)
    return result

print tarjan(graph)
print maxim, mem
