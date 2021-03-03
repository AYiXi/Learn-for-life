package main

import (
	"time"
	"math/rand"
	"fmt"
)

func main() {
	for i:=1; i<10; i++{
		if i == 9 {
			goto breakHere
		}
		fmt.Println(i)
	}

	return

	breakHere:
		fmt.Println("here")

	fmt.Println(rand.Int())

	rand.Seed(1000)
	num := rand.Intn(10)
	fmt.Println(num)

	t1 := time.Now()
	fmt.Println(t1)
	fmt.Printf("%T\n", t1)

	timeStamp1 := t1.Unix()
	fmt.Println(timeStamp1)

	timeStamp2 := t1.UnixNano()
	fmt.Println(timeStamp2)

	rand.Seed(time.Now().UnixNano())
	for i:=1; i<10; i++{
		// fmt.Println(rand.Intn(100))
		fmt.Println(rand.Intn(40) + 3) // 3->42
	}
}