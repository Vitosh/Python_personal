def main():    
    my_input = list(input())
    size = len(my_input)
    my_dict = {}

    for i in range(size):
        my_char = my_input[i]
        if my_char in my_dict.keys():
            my_dict[my_char] += 1
        else:
            my_dict.update({my_char:1})

    for i in sorted(my_dict.keys()) :
        print("{}: {} time/s".format(i, my_dict[i]))

if __name__ == "__main__":
    main() 