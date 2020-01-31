def main():    
    size = int(input())
    elements = set()

    for _ in range(size):
        line_input = list(input().split())
        for element in line_input:
            elements.add(element)

    for element in elements:
        print(element)

if __name__ == "__main__":
    main() 