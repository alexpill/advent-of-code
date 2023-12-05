from functools import reduce

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

class Range:
    def __init__(self, range_start, source_range_start, range_length):
        self.range_start = range_start
        self.source_range_start = source_range_start
        self.range_length = range_length
    def is_in_range(self, number):
        return number >= self.source_range_start and number < self.source_range_start + self.range_length
    def map_in_range(self, number):
        if not self.is_in_range(number): raise ValueError
        return number + (self.range_start - self.source_range_start)
    def __repr__(self) -> str:
        return f"{self.range_start, self.source_range_start, self.range_length}"

class Mapper:
    def __init__(self, ranges: list[Range]):
        self.ranges = ranges
    def convert_value(self, number):
        for range_ in self.ranges:
            if range_.is_in_range(number): return range_.map_in_range(number)
        return number
    def __repr__(self) -> str:
        return f"{self.ranges}"


def get_input(file):
    with open(file) as f:
        return [[[int(k) for k in j.split()] for j in i.split(':')[1].splitlines() if j] for i in f.read().split('\n\n')]

def get_lowest_location(seeds, mappers):
    lowest_location = -1
    visited = {}
    for seed in seeds:
        if seed in visited: continue
        location = seed
        for mapper in mappers:
            location = mapper.convert_value(location)
        visited[seed] = location
        if lowest_location == -1 or lowest_location > location:
            lowest_location = location
    return lowest_location

def get_lowest_location_with_ranges(seeds, mappers):
    for mapper in mappers:
        new = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for range_ in mapper.ranges:
                overlap_start = max(start, range_.source_range_start)
                overlap_end = min(end, range_.source_range_start + range_.range_length)
                if overlap_start < overlap_end:
                    new.append((overlap_start - range_.source_range_start + range_.range_start, overlap_end - range_.source_range_start + range_.range_start ))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new.append((start, end))
        seeds = new
    return min(seeds)[0]


def get_mappers(values):
    mappers = []
    for value in values:
        ranges = [Range(*i) for i in value]
        mappers.append(Mapper(ranges))
    return mappers

def part1(values):
    seeds = values[0][0]
    print(f"First part: {get_lowest_location(seeds, get_mappers(values[1:]))}")

def part2(values):
    raw_seeds = values[0][0]
    seeds = []
    for i in range(0, len(raw_seeds), 2):
        seeds.append((raw_seeds[i], raw_seeds[i] + raw_seeds[i+1]))
    print(f"Second part: {get_lowest_location_with_ranges(seeds, get_mappers(values[1:]))}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 289863851
    part2(values) # Second part:

if __name__ == "__main__":
    main()

# The helpful video : https://www.youtube.com/watch?v=NmxHw_bHhGM