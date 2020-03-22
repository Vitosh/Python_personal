def get_repeating_DNA(test):
    for i in range(0, len(test)-10):
        print (test[i:i+10])

test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)