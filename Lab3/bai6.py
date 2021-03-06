from bai4 import skip_header
def smallest_value_skip2(reader):
    line = skip_header(reader).strip()
    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    smallest = line

    for line in reader: 
        line = line.strip()
        if line == '-':
            continue
    value = line
    smallest = min(smallest, value)
    return smallest
input_file = open('D:\\alkaline_metals.txt', 'r')
print(smallest_value_skip2(input_file))
input_file.close()
