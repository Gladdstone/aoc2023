# I only realized how stupid this solution was after
# I was already committed. All well. Y'all ever seen DBZ Kai?
# Good stuff. The VAs take turns singing the theme.


class MapConstruct:
  seeds = []
  seed_to_soil = {}
  soil_to_fertilizer = {}
  fertilizer_to_water = {}
  water_to_light = {}
  light_to_temperature = {}
  temperature_to_humidity = {}
  humidity_to_location = {}

  def solve_part_1(self) -> int:
    lowest = None
    for seed in self.seeds:
      if seed in self.seed_to_soil:
        soil_map = self.seed_to_soil[int(seed)]
      else:
        soil_map = int(seed)
      if soil_map in self.soil_to_fertilizer:
        fertilizer_map = self.soil_to_fertilizer[soil_map]
      else:
        fertilizer_map = soil_map
      if fertilizer_map in self.fertilizer_to_water:
        water_map = self.fertilizer_to_water[fertilizer_map]
      else:
        water_map = fertilizer_map

      if water_map in self.water_to_light:
        light_map = self.water_to_light[water_map]
      else:
        light_map = water_map
      if light_map in self.light_to_temperature:
        temperature_map = self.light_to_temperature[light_map]
      else:
        temperature_map = light_map
      if temperature_map in self.temperature_to_humidity:
        humidity_map = self.temperature_to_humidity[temperature_map]
      else:
        humidity_map = temperature_map
      if humidity_map in self.humidity_to_location:
        location_map = self.humidity_to_location[humidity_map]
      else:
        location_map = humidity_map

      if lowest is None or lowest < location_map:
        lowest = location_map

    print(lowest)
    return lowest

def read_file(filename: str) -> MapConstruct:
  map_construct = MapConstruct()

  with open(filename) as file:
    for i, line in enumerate(file):
      delimited = line.strip("\n").split(" ")

      if delimited[0] == "seeds:":
        map_construct.seeds = delimited[1:]
      elif delimited[0] == "seed-to-soil":
        map_block = []
        line = next(file)
        while line != "\n" and line != "":
          map_block.append(line)
          line = next(file)
        map_construct.seed_to_soil = construct_map(map_block)
      elif delimited[0] == "soil-to-fertilizer":
        map_block = []
        line = next(file)
        while line != "\n" and line != "":
          map_block.append(line)
          line = next(file)
        map_construct.soil_to_fertilizer = construct_map(map_block)
      elif delimited[0] == "fertilizer-to-water":
        map_block = []
        line = next(file)
        while line != "\n" and line != "":
          map_block.append(line)
          line = next(file)
        map_construct.fertilizer_to_water = construct_map(map_block)
      elif delimited[0] == "water-to-light":
        map_block = []
        line = next(file)
        while line != "\n" and line != "":
          map_block.append(line)
          line = next(file)
        map_construct.water_to_light = construct_map(map_block)
      elif delimited[0] == "light-to-temperature":
        map_block = []
        line = next(file)
        while line != "\n" and line != "":
          map_block.append(line)
          line = next(file)
        map_construct.light_to_temperature = construct_map(map_block)
      elif delimited[0] == "temperature-to-humifity":
        map_block = []
        line = next(file)
        while line != "\n" and line != "":
          map_block.append(line)
          line = next(file)
        map_construct.temperature_to_humidity = construct_map(map_block)
      elif delimited[0] == "humidity-to-location":
        map_block = []
        line = next(file)
        while line != "\n" and line != "":
          map_block.append(line)
          try:
            line = next(file)
          except StopIteration:
            break
        map_construct.humidity_to_location = construct_map(map_block)

  return map_construct

def construct_map(map_block: list) -> dict:
  constructed_map = {}
  for map in map_block:
    map_delimited = map.split(" ")
    destination_range = int(map_delimited[0])
    source_range = int(map_delimited[1])
    length = int(map_delimited[2].strip("\n"))

    for i in range(length):
      constructed_map[source_range] = destination_range
      destination_range += 1
      source_range += 1

  return constructed_map

def main():
  filename = "/Users/josephfarrell/git/aoc2023/day5/input"

  map_construct = read_file(filename)
  print(map_construct)
  solution = map_construct.solve_part_1()
  print(solution)

main()
