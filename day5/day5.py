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
      soil_map = self.calculate_mapping(int(seed), self.seed_to_soil)
      fertilizer_map = self.calculate_mapping(soil_map, self.soil_to_fertilizer)
      water_map = self.calculate_mapping(fertilizer_map, self.fertilizer_to_water)
      light_map = self.calculate_mapping(water_map, self.light_to_temperature)
      temperature_map = self.calculate_mapping(light_map, self.temperature_to_humidity)
      humidity_map = self.calculate_mapping(temperature_map, self.humidity_to_location)
      location_map = self.calculate_mapping(humidity_map, self.humidity_to_location)

      if lowest is None or lowest < location_map:
        lowest = location_map

    return lowest

  def calculate_mapping(self, value: int, map: dict):
    mapping = value
    for key in map:
      if value <= key + map[key][1]:
        diff = (key + map[key][1]) - value
        mapping = map[key][0] + diff

    return mapping


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
    
    constructed_map[source_range] = [destination_range, length]

  return constructed_map

def main():
  filename = "/Users/josephfarrell/git/aoc2023/day5/input"

  map_construct = read_file(filename)
  solution = map_construct.solve_part_1()
  print(solution)

main()
