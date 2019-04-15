#File Encryption and Decryption


def decrypt(outfile, codes):
    infile = open("uncoded_data.txt", "w")
    reverse_code = {value: key for key, value in codes.items()}
    data = outfile.read()
    for each in data:
        if each in reverse_code:
            infile.write(reverse_code[each])
        else:
            infile.write(each)
    infile.close()


def encrypt(file, codes):
    outfile = open("coded_data.txt", "w")
    data = file.read()
    for each in data:
        if each in codes:
            outfile.write(codes[each])
        else:
            outfile.write(each)
    outfile.close()


def main():
    codes = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*', 'I': '(', 'J': ')'}
    file = open("Names.txt", "r")
    encrypt(file, codes)
    file.close()
    outfile = open("coded_data.txt", "r")
    decrypt(outfile, codes)
    outfile.close()


main()