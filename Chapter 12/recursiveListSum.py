def sum_list(item_list, start):
    if start == len(item_list):
        return 0
    else:
        return item_list[start] + sum_list(item_list, start + 1)


def main():
    item_list = [11, 4, 3, 9, 11, 223, 2, 165]
    print(sum_list(item_list, 0))


main()