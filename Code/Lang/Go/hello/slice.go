package main

import "fmt"

func main() {
	s1 := []int{1, 2, 3}
	f(s1)

	s1 = append(s1, 4, 5)
	f(s1)

	s1 = append(s1, 6, 7, 8)
	f(s1)

	s1 = append(s1, 9, 10)
	f(s1)

	fmt.Println("=============")

	// 数组, 值传递
	l1 := [4]int{1, 2, 3, 4}
	l2 := l1
	fmt.Println(l1, l2)
	l1[0] = 100
	fmt.Println(l1, l2)

	// 切片, 引用类型
	l3 := []int{1, 2, 3, 4}
	l4 := l3
	fmt.Println(l3, l4)
	l1[0] = 100
	fmt.Println(l3, l4)

	fmt.Printf("addr: %p \n", l3) // l3 引用的地址
	fmt.Printf("addr: %p \n", l4)
	fmt.Printf("addr: %p \n", &l3) // l3 本身的地址
	fmt.Printf("addr: %p \n", &l4)

	l5 := []int{1, 2, 3}
	l6 := make([]int, 3)
	copy(l6, l5)
	fmt.Println(l5, l6)
}

func f(a []int) {
	// 扩容时， 数组的容量会成倍增长， 地址会发生变化
	fmt.Println(a)
	fmt.Printf("len: %d, cap: %d \n", len(a), cap(a))
	fmt.Printf("addr: %p\n", a)
	fmt.Println()
}
