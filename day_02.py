import re


def to_vector(line):
    m = re.match(r'(forward|up|down) (\d+)', line)
    return {
        'forward': lambda num: (num, 0),
        'up': lambda num: (0, -1 * num),
        'down': lambda num: (0, num),
    }.get(m[1])(int(m[2]))


def sum_vectors(vectors):
    out = list()
    # assumes all vectors have same length
    for n in range(0, len(vectors[0])):
        out.append(sum([v[n] for v in vectors]))
    return tuple(out)


def main():
    with open('input/02_input.txt', 'r') as f:
        vectors = [to_vector(line.strip()) for line in f.readlines()]
        final_vector = sum_vectors(vectors)
        print(f'2A: {final_vector[0] * final_vector[1]}')


def test_to_vector():
    assert to_vector('forward 3') == (3, 0)
    assert to_vector('up 3') == (0, -3)
    assert to_vector('down 3') == (0, 3)


def test_sum_vectors():
    assert sum_vectors([(1, 0, 1), (1, 1, 0), (2, 0, 1)]) == (4, 1, 2)

if __name__ == '__main__':
    main()
