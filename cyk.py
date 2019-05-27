def read_input():
    file = open("input.txt","r") 
    x = []
    x = file.readlines()
    x = x[0]
    x = x[:-1] # ommiting '\n'
    file.close()
    return x



def read_grammer():
    file = open("Grammer.txt","r") 
    x = []
    x = file.readlines()
    for i in range(len(x)): # ommiting '\n'
        y = x[i]
        x[i] = y[:-1]

    file.close()
    
    return x


def parse_grammer(grammer):
    bigs = []
    littles = []
    for rules in grammer :
        left, rights = rules.split('->', 1)
        left = left.strip()
        rights = rights.strip()
        right_split = rights.split('|')
        for right in right_split:
            right = right.strip()
            if right.isupper():
                bigs.append([left, right])
            else:
                littles.append([left, right])
    return bigs, littles



def CYK_Algorithm(bigs, littles, n):

    matrix = [[set() for x in range(n)] for y in range(n)] 
    
    for i in range(n):
        char = inp[i]
        for x in littles:
            if char == x[1]:
                matrix[0][i].add(x[0])


    for j in range(1, n): 
        for k in range(n-j):  
            for l in range(j):
                B = matrix[l][k]
                C = matrix[j-l-1][k+l+1]
                X = set()
                for x in B:
                    for y in C:
                        X.add(x + y)

                for element in X:
                    for x in bigs:
                        if element == x[1]:
                            matrix[j][k].add(x[0])

    return matrix



inp = read_input()
grammer = read_grammer()
bigs, littles = parse_grammer(grammer)
matrix = CYK_Algorithm(bigs, littles, len(inp))


if(matrix[len(inp)-1][0].__contains__('S') == True):
    print("The input can be produced by the given grammer.")
else:
    print("The input cannot be produced by the given grammer!")

# for i in range(n):
#     print(matrix[i])

