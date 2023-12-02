package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type Game struct {
	id      int
	red     int
	green   int
	blue    int
	gameStr string
}

func readFile(fileName string, red int, green int, blue int, part int) (int, error) {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatalf("unable to read file %w", err)
	}
	defer file.Close()

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	sum := 0
	for fileScanner.Scan() {
		game := parseGame(fileScanner.Text())

		if part == 1 {
			sum += part1(game, red, green, blue)
		} else {
			sum += part2(game)
		}
	}

	return sum, nil
}

func parseGame(line string) *Game {
	game := strings.Split(line, ":")
	gameId_str := strings.Split(game[0], " ")[1]
	gameId, _ := strconv.ParseInt(gameId_str, 0, 0)

	rounds := strings.Split(game[1], ";")

	red := 0
	green := 0
	blue := 0
	for _, round := range rounds {
		values := strings.Split(round, ", ")

		for _, value := range values {
			value = strings.TrimSpace(value)
			counts := strings.Split(value, " ")
			counts_int, _ := strconv.ParseInt(counts[0], 0, 0)

			if counts[1] == "red" && int(counts_int) > red {
				red = int(counts_int)
			} else if counts[1] == "green" && int(counts_int) > green {
				green = int(counts_int)
			} else if counts[1] == "blue" && int(counts_int) > blue {
				blue = int(counts_int)
			}
		}
	}

	parsedGame := &Game{
		id:      int(gameId),
		red:     red,
		green:   green,
		blue:    blue,
		gameStr: line,
	}

	return parsedGame
}

func part1(game *Game, red int, green int, blue int) int {
	if game.red > red || game.green > green || game.blue > blue {
		return 0
	} else {
		return game.id
	}
}

func part2(game *Game) int {
	return game.red * game.green * game.blue
}

func main() {
	red := 12
	green := 13
	blue := 14
	input := "input"
	println(readFile(input, red, green, blue, 1))
}
