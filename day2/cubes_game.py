from dataclasses import dataclass
from functools import reduce
from operator import mul

from test_params import read_task


@dataclass
class Shuffle:
    red: int = 0
    green: int = 0
    blue: int = 0

    @staticmethod
    def from_str(shuffle: str):
        res = shuffle.strip().split(', ')
        res = [l.split(' ')[::-1] for l in res]
        return Shuffle(**dict(res))

    @property
    def as_dict(self):
        return self.__dict__


@dataclass
class Game:
    id: int
    shuffles: list[Shuffle]

    @property
    def limits(self):
        return {
            'red': 12,
            'green': 13,
            'blue': 14
        }

    @staticmethod
    def from_str(game: str) -> 'Game':
        game_id, content = game.strip().split(':')
        *_, id_ = game_id.split(' ')

        shuffles = [
            Shuffle.from_str(shuffle)
            for shuffle in content.strip().split('; ')
        ]

        return Game(int(id_), shuffles)

    def is_possible(self) -> bool:
        for shuffle in self.shuffles:
            for color, count in shuffle.as_dict.items():
                if int(count) > self.limits[color]:
                    return False
        return True

    def fewest_cubes_needed(self) -> list[int]:
        red = max(int(shuffle.red) for shuffle in self.shuffles)
        green = max(int(shuffle.green) for shuffle in self.shuffles)
        blue = max(int(shuffle.blue) for shuffle in self.shuffles)

        return [red, green, blue]

    def set_power(self):
        return reduce(mul, self.fewest_cubes_needed())


def main(arr: list[str]) -> int:
    res = []
    for line in arr:
        game = Game.from_str(line)
        if game.is_possible():
            res.append(game.id)

    return sum(res)


# second star
def main2(arr: list[str]) -> int:
    return sum(
        Game.from_str(line).set_power()
        for line in arr
    )


if __name__ == '__main__':
    input = read_task('day2/input.txt')
    print(main(input))
    print(main2(input))
