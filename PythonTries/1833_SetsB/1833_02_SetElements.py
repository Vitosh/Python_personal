def main():    
    first_line = input().split()
    size_a = int(first_line[0])
    size_b = int(first_line[1])

    names_a = set()
    names_b = set()

    for _ in range(size_a):
        names_a.add(input())

    for _ in range(size_b):
        names_b.add(input())

    for name in names_a:
        if name in names_b:
            print(name)

if __name__ == "__main__":
    main()