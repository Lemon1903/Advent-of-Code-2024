import sys


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def main(input_file):
    lines = read_input_file(input_file)
    right_list, left_list = [], []

    for line in lines:
        right, left = map(int, line.split())
        right_list.append(right)
        left_list.append(left)

    right_list.sort()
    left_list.sort()

    sum, similarity = 0, 0
    for right, left in zip(right_list, left_list):
        # Part 1
        sum += abs(right - left)

        # Part 2
        for l in left_list:
            if right == l:
                similarity += right

    print(sum, similarity)


if __name__ == "__main__":
    input_file = sys.argv[1]
    main(input_file)
