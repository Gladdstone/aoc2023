import re


def read_input(filename: str) -> list:
  with open(filename) as file:
    lines = file.readlines()

    times = lines[0].split(":")
    times = times[1].strip(" ").strip("\n")
    times = re.split(r' +', times)

    distance = lines[1].split(":")[1].strip(" ").strip("\n")
    distance = re.split(r' +', distance)

    return [times, distance]

def read_input_part_2(filename: str) -> list:
  with open(filename) as file:
    lines = file.readlines()

    times = lines[0].split(":")[1].replace(" ", "").strip("\n")

    distance = lines[1].split(":")[1].replace(" ", "").strip("\n")

    return [[times], [distance]]

def solve(races: list) -> int:
  solution = 1
  for i, race in enumerate(races[0]):
    time = int(races[0][i])
    target_distance = int(races[1][i])

    winning_value = 0
    for time_held in range(0, time):
      speed = time_held
      distance_traveled = speed * (time - time_held)
      if distance_traveled > target_distance:
        winning_value += 1

    solution *= winning_value

  return solution


def main():
  input = "/Users/josephfarrell/git/aoc2023/day6/input"

  # races = read_input(input)
  races = read_input_part_2(input)
  print(solve(races))

main()