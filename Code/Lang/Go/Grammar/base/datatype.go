package main

import "fmt"

func main() {
	/*
	1. Basic data types
		Bool type
			bool
		Numeric type
			integer
				int8/16/32/64
				uint8/16/32/64
				byte: uint8
				rune: int32
				int -> int64 : err
			floating point
				float32
				float64v
			plural
		String
			string
	2. Compound data type
		array, slice, map, function, pointer, struct, interface, channel ...
	 */

	//b1 := true
	var b1 bool
	b1 = true

	fmt.Printf("%T, %t\n", b1, b1)

}
