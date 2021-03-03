package main

import "fmt"

func main() {
	fmt.Println(getSum3(1, 2, 3, 4, 5))

	fmt.Println(getSum3([]int{1, 2, 3}...))

	fmt.Println(rectangle(1.123, 2.23))

	res := oper(1, 2, func(a, b int) int {
		return a + b
	})

	fmt.Println(res)

	// 外层函数 incre 有内层函数 f, f 会操作外层函数的局部变量 i(外层函数的参数, 或者直接定义的变量)
	// 会导致 incre 的局部变量生命周期发生改变
	// f 和 incre 的局部变量, 统称为 闭包结构
	inc := incre()
	i := inc()
	i2 := inc()
	fmt.Println("i, i2: ", i, i2)

}

func oper(a, b int, f func(int, int) int) int {
	return f(a, b)
}

func incre() func() int {
	i := 1
	f := func() int {
		i++
		return i
	}

	//return f := func() int {
	//	i++
	//	return i
	//}

	return f
}

func getSum(n int) (x int) {
	sum := 0
	for i := 1; i <= n; i++ {
		sum += i
	}

	return sum
}

func getSum2(a, b int, c string) (x int) {
	sum := 0
	for i := 1; i <= a+b; i++ {
		sum += i
	}

	fmt.Println(c)
	return sum
}

func getSum3(nums ...int) (sum int) {
	sum = 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
	}

	return
}

func rectangle(len, wid float64) (float64, float64) {
	perimeter := (len + wid) * 2
	area := len * wid
	return perimeter, area
}
