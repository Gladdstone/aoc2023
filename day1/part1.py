filename = "input"

def find_calibration() -> int:
  sum = 0
  with open(filename) as file:
    for line in file:
      num = None
      for i, value in enumerate(line):
        if value.isdigit():
          if num is None:
            num = value
          else:
            if len(num) > 1:
              num = num[0]
            num = str(num) + str(value)

      if num != None:
        if len(num) < 2:
          num = num[0] + num[0]
        sum += int(num)

  return sum

print(find_calibration())
