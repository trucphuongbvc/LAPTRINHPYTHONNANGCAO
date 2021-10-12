def read_molecule(reader):
    content = []
    for line in reader:
        if not line.startswith('CMNT'):
            if not line.isspace():
                content.append(line.strip())
    for line in content:
        print(line)
    
input_file = open('D:\\kkk.txt', 'r')
print(read_molecule(input_file))
input_file.close()
