def largest_item(item_list, start, end, largest):
    if end == len(item_list):
        return largest
    else:
        if item_list[start] > item_list[start+1]:
            if item_list[start] > largest:
                largest = item_list[start]
            return largest_item(item_list, start+1, start+2, largest)
        else:
            if item_list[start+1] > largest:
                largest = item_list[start+1]
            return largest_item(item_list, start + 1, start + 2, largest)


def main():
    item_list = [11, 4, 3, 9, 11, 223, 2, 165]
    print(largest_item(item_list, 0, 1, 0))


main()