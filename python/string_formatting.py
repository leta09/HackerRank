def print_formatted(number):
    # your code goes here
    res = ""
    b_len = len(bin(number)[2:])
    for i in range(1,number+1):
        res = res + str(i).rjust(b_len) + " " + oct(i)[2:].rjust(b_len) + " " + hex(i).upper()[2:].rjust(b_len) + " " + bin(i)[2:].rjust(b_len) + "\n"
    return res
if __name__ == '__main__':
    n = int(input())
    print(print_formatted(n))