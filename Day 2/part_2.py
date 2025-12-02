import sys


invalid_ids_sum = 0

for line in sys.stdin:
    ranges = line.split(',')


    for id_range in ranges:
        ids = id_range.split('-')
        first_id = int(ids[0])
        second_id = int(ids[1])

        for num in range(first_id, second_id+1):
            num_str = str(num)
            n = len(num_str)

            for i in range(1, n//2 + 1):
                num_part = num_str[:i]
                if num_part*(n//i) == num_str:
                    invalid_ids_sum += num
                    break

    print(f'Solution: {invalid_ids_sum}')
