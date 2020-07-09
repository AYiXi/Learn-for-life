package main

import "fmt"

func main() {
	a := 10
	fmt.Println("a:", a)
	fmt.Println("a(addr):", &a)

	// pointer
	var p *int
	fmt.Println("nil pointer:", p) // 空指针
	p = &a
	fmt.Println("p:", p)
	fmt.Printf("p addr: %p \n", &p)
	fmt.Println("a:", *p)

	// pointer's pointer
	var p2 **int
	fmt.Println("p2:", p2)
	p2 = &p
	fmt.Printf("a: %T, p: %T, p2: %T\n", a, p, p2)
	fmt.Printf("p2: %p, p2 addr: %p\n", p2, &p2)

	// array pointer
	arr1 := [4]int{1, 2, 3, 4}
	fmt.Println("arr1:", arr1)

	var p3 *[4]int
	p3 = &arr1
	fmt.Println("p3:", p3) // &[1 2 3 4]
	fmt.Printf("p3: %p\n", p3)
	fmt.Printf("p3: %p\n", &p3)

	(*p3)[0] = 100
	fmt.Println(arr1)
	p3[1] = 200
	fmt.Println(arr1)

	// pointer array
	a1 := 1
	b := 2
	c := 3
	d := 4

	arr2 := [4]int{a1, b, c, d}
	arr3 := [4]*int{&a1, &b, &c, &d}
	fmt.Println(arr2)
	fmt.Println(arr3)

	*[5]float64
}
