from dataclasses import dataclass


@dataclass
class Req:
    letter: str
    first_value: int
    second_value: int

    def __str__(self):
        return f"{self.first_value}-{self.second_value} {self.letter}"


class RangeValidator:
    def validate(self, req: Req, password: str):
        return req.first_value <= password.count(
            req.letter) <= req.second_value


class PostionValidator:
    def validate(self, req: Req, password: str):
        first_letter = password[req.first_value - 1]
        second_letter = password[req.second_value - 1]
        return (first_letter == req.letter) != (second_letter == req.letter)


def parse_requirement(s: str):
    [count_range, letter] = s.split(" ")
    [min_val, max_val] = count_range.split("-")
    return Req(letter.strip(), int(min_val), int(max_val))


def parse_lines(lines: list[str]):
    for line in lines:
        [req, password] = line.split(":")
        req = parse_requirement(req)
        yield (req, password.strip())


def count_valid_passwords(lines, validator):
    count = 0
    for (req, password) in parse_lines(lines):
        if validator.validate(req, password):
            count += 1
    return count


lines = []
with open('input.txt') as f:
    lines = f.readlines()

count = count_valid_passwords(lines, RangeValidator())
print("Part 2")
print(f"Number of valid passwords: {count}")

count = count_valid_passwords(lines, PostionValidator())
print("Part 2")
print(f"Number of valid passwords: {count}")