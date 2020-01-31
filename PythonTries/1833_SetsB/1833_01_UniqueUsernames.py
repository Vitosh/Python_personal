def main():    
    size = int(input())
    names = set()
    for _ in range(size):
        names.add(input())
    
    for name in names:
        print(name)

if __name__ == "__main__":
    main()