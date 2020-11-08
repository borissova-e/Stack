class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def to_check_balance(sequence):
    sequence_close = Stack()
    pair = {'(': ')', '[': ']', '{': '}'}
    if (len(sequence) % 2) == 0:
        check = 0
        for element in sequence:
            if element in pair.keys():
                sequence_close.push(pair[element])
            elif element in pair.values():
                if sequence_close.isEmpty():
                    print('Несбалансированно')
                    check = 1
                    break
                else:
                    if element == sequence_close.peek():
                        sequence_close.pop()
                    else:
                        print('Несбалансированно')
                        check = 1
                        break
            else:
                print('Не является последвательностью скобок')
                check = 1
                break
        if check == 0:
            if sequence_close.isEmpty():
                print('Cбалансированно')
            else:
                print('Неcбалансированно')
    else:
        print('Небалансированно')


if __name__ == '__main__':
    sequence = input('Введите последовательность скобок: ')
    to_check_balance(sequence)
