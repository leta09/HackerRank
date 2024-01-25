def split_and_join(line):
    # write your code here
    list_line = line.split(" ")
    list_line = "-".join(list_line)
    return list_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)