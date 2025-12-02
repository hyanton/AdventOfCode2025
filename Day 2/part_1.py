import sys


invalid_ids_sum = 0

for line in sys.stdin:
    ranges = line.split(',')

    for id_range in ranges:
        ids = id_range.split('-')
        first_id = int(ids[0])
        second_id = int(ids[1])

        for i in range(first_id, second_id+1):
            i_str = str(i)
            n = len(i_str)

            if n % 2 == 0 and i_str[:n//2] == i_str[n//2:]:
                invalid_ids_sum += i

    print(f'Solution: {invalid_ids_sum}')
