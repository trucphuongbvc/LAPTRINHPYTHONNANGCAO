alkaline_metals = []
for line in open('D:\\alkaline_metals.txt'):
    alkaline_metals.append(line.strip().split(' '))
print(alkaline_metals)
