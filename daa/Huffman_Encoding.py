
def huffman(char, freq):

    nodes = [[freq[i], [[char[i], ""]]] for i in range(len(char))]

    while len(nodes) > 1:

        nodes.sort(key=lambda x: x[0])

        
        left = nodes.pop(0)
        right = nodes.pop(0)

       
        for x in left[1]:
            x[1] = '0' + x[1]

        
        for x in right[1]:
            x[1] = '1' + x[1]

        new_node = [
            left[0] + right[0],
            left[1] + right[1]
        ]

        nodes.append(new_node)

    return nodes[0][1]


# Input
n = int(input("Enter number of characters: "))

char = []
freq = []

for i in range(n):
    c = input(f"Enter character {i+1}: ")
    f = int(input(f"Enter frequency of {c}: "))

    char.append(c)
    freq.append(f)

codes = huffman(char, freq)

print("\nHuffman Codes:")
for c, code in codes:
    print(c, ":", code)
