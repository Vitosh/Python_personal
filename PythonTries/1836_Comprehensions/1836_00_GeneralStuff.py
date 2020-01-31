def main():

    #list not in list
    vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
    text = "https://vitoshacademy.com is my blog."
    no_vowels = ''.join([x for x in text if x not in vowels])
    print(no_vowels)

    #list in list
    only_vowels = ''.join([x for x in text if x  in vowels])
    print(only_vowels)

    #dictionary from a string
    letters = list(text)
    occurrences = {char: letters.count(char) for char in letters}
    print(occurrences)

    char_dict = {char: ord(char) for char in letters}
    print(char_dict)

    #creation of 1D matrix:
    matrix1D = [j for j in range(100,105)]
    print(matrix1D)

    #creation of a 2D matrix:
    matrix2D = [[j for j in range(4)] for i in range(10)]
    print(matrix2D)

    #creation of a 3D matrix:    
    matrix3D = [[[j for j in range(10,12)] for i in range(2)] for z in range(2)]
    print(matrix3D)

    #flattenning a 2D matrix:
    flattened = [num for sublist in matrix2D for num in sublist]
    print(flattened)

    #numbers, divisable by a set of other numbers
    numbers = [num for num in range(100, 150)]
    set_of_other_numbers = [num for num in range(2, 20)]
    divisable = [num for num in numbers if any([num % x == 0 for x in set_of_other_numbers])]
    print("divisable: {0}\n".format(divisable))
    
    #non-divisable method 1
    non_divisable =  [num for num in numbers if all([num % x != 0 for x in set_of_other_numbers])]
    print(non_divisable)
    
    #non-divisable method 2
    non_divisable = [num for num in numbers if num not in divisable]
    print(non_divisable)



if __name__ == "__main__":
    main()