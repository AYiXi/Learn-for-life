package main

import (
	"fmt"
)

func main() {
	s1 := "hello"
	s2 := `world`

	fmt.Println(s1)
	fmt.Println(s1)

	fmt.Println(len(s1))
	fmt.Println(len(s2))

	fmt.Println(s1[0]) // 104

	a := 'h'
	b := 104
	fmt.Printf("%c, %c, %c \n", s1[0], a, b)

	sl1 := []byte{65, 66,67, 68, 69}
	s3 := string(sl1)

	sl2 := []byte(s3)
	fmt.Println(s3, sl1, sl2)
}
