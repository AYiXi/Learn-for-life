package main

import "fmt"

func main() {
	X()
	defer myprint("main defer 1...")
	Y()
	defer myprint("main defer 2...")
	fmt.Println("main over...")
}

func myprint(s string) {
	fmt.Println(s)
}

func X() {
	fmt.Println("func X")
}

func Y() {
	defer func() {
		if msg := recover(); msg != nil {
			fmt.Println(msg, "Y recover...")
		}
	}()

	fmt.Println("func Y")
	defer myprint("Y defer 1...")
	for i:=1; i<=10; i++ {
		fmt.Println("i: ", i)
		if i == 5 {
			// break program
			panic("Y panic...\n")
		}
	}
	defer myprint("Y defer 2...")
}