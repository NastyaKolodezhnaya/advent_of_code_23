import os
from dataclasses import dataclass

from boltons.iterutils import first

from read_task import read_task

PATH = os.getcwd() + '/input.txt'


@dataclass
class Range:
    source_start: int
    destination_start: int
    range: int

    @property
    def source_range(self):
        return range(self.source_start, self.range + 1)

    @property
    def destination_range(self):
        return range(self.destination_start, self.range + 1)

    @property
    def source_dest_map(self):
        return dict(zip(self.source_range, self.destination_range))

    def find_destination(self, seed: int) -> int | None:
        return self.source_dest_map.get(seed)  # or seed


@dataclass
class Map:
    ranges: list[Range]
    next: 'Map' = None

    def find_destination(self, seed):
        from_ranges = [range_.find_destination(seed) for range_ in self.ranges]
        next_val = first(from_ranges) or seed
        if not self.next:
            return next_val
        return self.next.find_destination(next_val)


def generate_linked_maps(arr: list[str]) -> Map:
    pass


def main():
    input_ = read_task(PATH)
    # parse input in custom structures
    map = generate_linked_maps(input_)
    seeds: list[int]

    for seed in seeds:
        return map.find_destination(seed)


print(main())
