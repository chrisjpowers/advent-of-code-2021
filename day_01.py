from functools import reduce


def find_increases(nums):
    increase_sum = 0
    for x, y in list(zip(nums, nums[1:])):
        if y > x:
            increase_sum += 1
    return increase_sum


def test_find_increases():
    assert find_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7


if __name__ == '__main__':
    with open('input/01_input.txt', 'r') as f:
        input = [int(x.strip()) for x in f.readlines()]
        answer = find_increases(input)
        print(f'1A: {answer}')
