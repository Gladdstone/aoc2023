filename = "input"

ref = {
  "z": [["ero"], [0]],
  "o": [["ne"], [1]],
  "t": [["wo", "hree"], [2,3]],
  "f": [["our", "ive"], [4,5]],
  "s": [["ix", "even"], [6,7]],
  "e": [["ight"], [8]],
  "n": [["ine"], [9]]
}

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
        else:
         if value in ref:
          for n, val in enumerate(ref.get(value)[0]):
            if i + len(val) < len(line):
              if val == line[i+1:i+len(val)+1]:
                if num is None:
                  num = str(ref.get(value)[1][n])
                else:
                  if len(num) > 1:
                    num = num[0]
                  num = str(num) + str(ref.get(value)[1][n])

      if num != None:
        if len(num) < 2:
          num = num[0] + num[0]
        sum += int(num)

    return sum


print(find_calibration())
