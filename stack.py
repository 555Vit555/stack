class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    
def is_balance(lines):
    stack = Stack()
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for c in lines:
        if c == '(' or c=='[' or c=='{':
            stack.push(c)
        elif c == ')' or c==']' or c=='}':
            if stack.is_empty():
                return False
            st = stack.pop()
            if pairs[c] != st:
                return False
                
    return stack.is_empty()
def printed_is_balance(lines):
    if is_balance(lines):
        return('Сбалансировано')
    else:
        return('Несбалансировано')
## Сбалансированные последовательности скобок    
line_1= '(((([{}]))))'
print(printed_is_balance(line_1))
print('--------------------------------------------------')
line_2= '[([])((([[[]]])))]{()}'
print(printed_is_balance(line_2))
print('--------------------------------------------------')
line_3= '{{[()]}}'
print(printed_is_balance(line_3))
print('--------------------------------------------------')

## Несбалансированные последовательности скобок   
line_4= '}{}'
print(printed_is_balance(line_4))
print('--------------------------------------------------')
line_5= '{{[(])]}}'
print(printed_is_balance(line_5))
print('--------------------------------------------------')
line_6= '[[{())}]'
print(printed_is_balance(line_6))
print('--------------------------------------------------')
