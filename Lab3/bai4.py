def skip_header(reader):
    
    # Read the description line and then the comment lines.
    line = reader.readline()    
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline() 
    # Now line contains the first real piece of data.
    return line

def process_file(reader):
    # Find the first piece of data.
    line = skip_header(reader).strip()
    print(line)
    # Read the rest of the data.
    for line in reader:
        line = line.strip()
        print(line)

input_file = open('D:\\kkk.txt', 'r')
process_file(input_file)
input_file.close()
