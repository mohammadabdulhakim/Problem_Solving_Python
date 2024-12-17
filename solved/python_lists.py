# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    initial_list = []
    
    for n in range(N):
        command = input()
        command_parts = command.split()

        if command_parts[0] == "insert":
            initial_list.insert(int(command_parts[1]), int(command_parts[2]))
        elif command_parts[0] == "remove":
            initial_list.remove(int(command_parts[1]))
        elif command_parts[0] == "append":
            initial_list.append(int(command_parts[1]))
        elif command_parts[0] == "sort":
            initial_list.sort()
        elif command_parts[0] == "reverse":
            initial_list.reverse()
        elif command_parts[0] == "pop":
            initial_list.pop()
        elif command_parts[0] == "print":
            print(initial_list)
        else:
            print("Invalid command")
            
