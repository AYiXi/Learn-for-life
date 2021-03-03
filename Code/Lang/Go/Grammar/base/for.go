package main

import (
	"math"
	"fmt"
)

func main() {
	for i:=1; i<=5; i++ {
		fmt.Println(i)
		continue
	}

	i := 1
	for i <= 5 {
		fmt.Println(i)
		i++
	}

	fmt.Println(math.Pow(2, 3))
}