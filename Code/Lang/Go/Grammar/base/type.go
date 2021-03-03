package main

import (
	"fmt"
	"strconv"
)

func main() {
	/*
	type: 用于定义类型和类型别名
		1. 定义类型: type 类型名 Type
		2. 定义别名: type 类型名 = Type
	 */
	var i1 myint
	var i2 mystr
	i1 = 123
	i2 = "str"

	fmt.Println(i1, i2)
	fmt.Printf("i1: %T\ni2: %T\n", i1, i2)

	res1 := fun1()
	fmt.Println(res1(10, 20))
}

// 定义类型
type myint int
type mystr string
type myint2 = int  // myint2 == int 类型

// 定义函数类型
type myfun func(int, int) string

// 返回值就不用写那么复杂了, 只需要写 myfun
func fun1() myfun {
	fun := func(a, b int) string {
		s := strconv.Itoa(a) + strconv.Itoa(b)
		return s
	}

	return fun
}