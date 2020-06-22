package main

import (
	"fmt"
)

func main() {
	var arr1 [4] int
	arr1[0] = 1
	arr1[1] = 1
	arr1[2] = 1
	arr1[3] = 1

	fmt.Println(len(arr1), cap(arr1))
	fmt.Println(arr1)

	var a [4] int
	fmt.Println(a) 

	var b = [4] int {1,2,3,4}
	fmt.Println(b)

	var c = [5] int {1:1,3:3}
	fmt.Println(c)

	d := [...] int {1,2,3,4,5}
	fmt.Println(d)
}