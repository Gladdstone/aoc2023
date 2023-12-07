package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func readFile(filename string) [][]string {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("unable to open file: %w", err)
	}
	defer file.Close()

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	graph := []([]string){}
	for fileScanner.Scan() {
		line := fileScanner.Text()
		lineArr := []string{}
		for _, slice := range strings.Split(line, "") {
			lineArr = append(lineArr, slice)
		}
		graph = append(graph, lineArr)
	}

	return graph
}

func solve(graph []([]string)) {
	for i, line := range graph {
		numString := ""
		for n := 0; n < len(line); n++ {
			if isDigit(line[n]) {
				// validate value then continue forward to validate remaining digits in the number,
				// return positively or negatively with a skip index
			}
		}
	}
}

func validateNumber(x int, y int, line []string, graph []([]string)) (int, int) {
	for isDigit(graph[x][y]) {
		if x-1 > 0 {

		}
		if y-1 > 0 {

		}
		if x+1 < len(graph) {

		}
		if y+1 < len(graph[x]) {

		}
	}

	return 0, 0
}

func isDigit(value string) bool {
	if _, err := strconv.Atoi(value); err == nil {
		return true
	}
	return false
}

func main() {
	input := "/Users/josephfarrell/git/aoc2023/day3/input"
	graph := readFile(input)
	solve(graph)
}
