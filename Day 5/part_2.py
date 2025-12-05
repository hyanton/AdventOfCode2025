def main():
    def add_interval(low: int, high: int):
        i = 0
        added = False
        while i < len(intervals):
            if intervals[i][0] > low:
                intervals.insert(i, [low, high])
                added = True
                break

            i += 1

        if not added:
            intervals.append([low, high])

    def merge_intervals():
        intervals_index = 1

        while intervals_index < len(intervals):
            interval = intervals[intervals_index]

            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(interval[1], merged_intervals[-1][1])
            else:
                merged_intervals.append(interval)

            intervals_index += 1


    with open('data.txt') as f:
        intervals = []
        read_intervals = True

        for line in f.readlines():
            if line == '\n':
                read_intervals = False
                continue

            line = line.replace('\n', '')
            if read_intervals:
                line = line.split('-')
                low = int(line[0])
                high = int(line[1])
                # Add interval in growing order of their left border
                add_interval(low, high)

        merged_intervals = [intervals[0]]
        merge_intervals()

        fresh_ingredients = 0
        for interval in merged_intervals:
            fresh_ingredients += interval[1] - interval[0] + 1

        print(f'Solution: {fresh_ingredients}')
if __name__ == '__main__':
    main()