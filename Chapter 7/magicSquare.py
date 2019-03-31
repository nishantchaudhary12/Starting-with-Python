# Lo Shu Magic Square


def check_magic(input_data):
    check_sum = input_data[0][0] + input_data[1][1] + input_data[2][2]
    if check_sum == input_data[2][0] + input_data[1][1] + input_data[0][2]:
        sum = 0

        #check rows
        for x in range(3):
            sum = input_data[x][0]
            for y in range(1, 3):
                sum = sum + input_data[x][y]
            if sum != check_sum:
                print('This is not a magic square.')
                break

        #check columns
        if sum == check_sum:
            for x in range(3):
                sum = input_data[0][x]
                for y in range(1, 3):
                    sum = sum + input_data[y][x]
                if sum != check_sum:
                    print('This is not a magic square.')
                    break

        if sum == check_sum:
            print('This is a magic square!!!')
    else:
        print('This is not a magic square.')


def main():
    input_data = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    check_magic(input_data)


main()