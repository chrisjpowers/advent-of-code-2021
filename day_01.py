def find_increases(nums):
    increase_sum = 0
    for x, y in list(zip(nums, nums[1:])):
        if y > x:
            increase_sum += 1
    return increase_sum


def triple_sums(nums):
    return [x + y + z for x, y, z in list(zip(nums, nums[1:], nums[2:]))]


def test_find_increases():
    assert find_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7


def test_find_triple_sum_increases():
    nums = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert find_increases(triple_sums(nums)) == 5


if __name__ == '__main__':
    with open('input/01_input.txt', 'r') as f:
        input = [int(x.strip()) for x in f.readlines()]
        print(f'1A: {find_increases(input)}')
        print(f'1B: {find_increases(triple_sums(input))}')
