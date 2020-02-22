package main

import (
	"fmt"
)

func main() {
	// x := 10
	// const hello string = "312"
	// fmt.Print("fds", x, hello, "\n")

	// var y complex64 = 6 + 2i
	// fmt.Print(y * y)

	// var t [3]int
	// t[0] = 1
	// t[1] = 3
	// fmt.Print(t)

	// z := [3]int{1, 2, 3}
	// fmt.Print(len(z))

	// q := z[1:2]
	// fmt.Print(q)

	// var fslice []int
	// s := make([]int, 10, 20)
	// s = append(s, 1, 3)
	// fmt.Print(len(fslice))
	// fmt.Print(s)

	// students := make(map[string]float32)
	// students["zhangsan"] = 123.123
	// students["zhangsa1n"] = 123.123
	// fmt.Print(students["zhangsan"])

	// sum := 0
	// for x := 0; x <= 100; x++ {
	// 	sum += x
	// }
	// fmt.Print(sum)

	// x := 1
	// switch x {
	// case 1:
	// 	fmt.Print(1)
	// case 2:
	// 	fmt.Print(2)
	// 	fallthrough // no break
	// default:
	// 	fmt.Print("defalut")
	// }

	x := [5]int{1, 2, 3, 4, 5}
	for _, v := range x{
		fmt.Println(v)
	}
}
