package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type entry struct {
	lo, hi int
	c      byte
	pw     string
}

func parse(s string) entry {
	x := strings.Fields(s)
	loHi := strings.Split(x[0], "-")
	lo, err := strconv.Atoi(loHi[0])
	check(err)
	hi, err := strconv.Atoi(loHi[1])
	check(err)
	return entry{
		lo: lo,
		hi: hi,
		c:  x[1][0],
		pw: x[2],
	}
}

func valid(e entry) bool {
	n := strings.Count(e.pw, string(e.c))
	return e.lo <= n && n <= e.hi
}

func main() {
	f, err := os.Open("2.txt")
	check(err)
	scanner := bufio.NewScanner(f)
	sum := 0
	for scanner.Scan() {
		if valid(parse(scanner.Text())) {
			sum += 1
		}
	}
	check(scanner.Err())
	fmt.Println(sum)
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}
