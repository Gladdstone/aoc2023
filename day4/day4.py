

def read_file(filename: str) -> int:
  score = 0
  with open(filename) as file:
    play_store = []
    for line in file:
      game_values = line.split(": ")[1] # remove card id
      play_values = game_values.split("|")  # split winning and play values
      play_values[1] = play_values[1].strip("\n")
      play_store.append(play_values)

      # score += solve_part_1(play_values=play_values)

  score = solve_part_2(play_store)

  return score

def solve_part_1(play_values: list) -> int:
  score = calculate_score(play_values)

  if score > 0:
    return 2**(score-1)
  else:
    return score

def solve_part_2(play_store: list) -> int:
  reprocess = []
  corrective = 0
  for i, play_values in enumerate(play_store):
    score = calculate_score(play_values)
    if score > 0:
      corrective += 1 # this is so fucking stupid don't be like me kids stay in school
      reprocess.append([i, score])

  for value in reprocess:
    starting_index = value[0] + 1
    ending_index = starting_index + value[1]
    for i in range(starting_index, ending_index):
      if i > len(play_store):
        break
      score = calculate_score(play_store[i])
      reprocess.append([i, score])

  return len(reprocess) + len(play_store) - corrective

def find_winning_numbers(play_values: list) -> dict:
  winning_numbers = {}
  win_arr = play_values[0].split(" ")
  for value in win_arr:
    if value not in winning_numbers and value.isdigit():
      winning_numbers[value] = 0

  return winning_numbers

def calculate_score(play_values: list) -> int:
  winning_numbers = find_winning_numbers(play_values=play_values)
  play_arr = play_values[1].split(" ")

  score = 0
  for value in play_arr:
    if value in winning_numbers and value.isdigit():
      winning_numbers[value] = 1
      score += 1

  return score

def main():
  input = "/Users/josephfarrell/git/aoc2023/day4/input"

  print(read_file(input))

main()
