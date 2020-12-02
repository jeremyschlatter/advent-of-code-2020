package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	b, err := ioutil.ReadFile("1.txt")
	check(err)
	var data []int
	for _, s := range strings.Fields(string(b)) {
		n, err := strconv.Atoi(s)
		check(err)
		data = append(data, n)
	}
	for i, a := range data {
		for j, b := range data {
			for k, c := range data {
				if i != j && j != k && a+b+c == 2020 {
					fmt.Println(a * b * c)
					return
				}
			}
		}
	}
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}
