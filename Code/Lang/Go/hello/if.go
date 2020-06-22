package main

import "fmt"

func main() {
	num := 16
	if num > 10 {
		fmt.Println("11")
	}

	if n := 4; n > 2 {
		fmt.Printf("%d\n", n)
	}

	num = 3
	switch num {
	case 1:
		fmt.Println(num)
	case 2:
		fmt.Println(num)
	case 3:
		fmt.Println(num)
	default:
		fmt.Println(num)
	}


	// 模拟计算器
	num1, num2 := 0, 0
	oper := ""
	fmt.Println("Int1:")
	fmt.Scanln(&num1)
	fmt.Println("Int2:")
	fmt.Scanln(&num2)
	fmt.Println("Oper:")
	fmt.Scanln(&oper)
	
	// case 后面可以跟数值和判断
	// case 10, 20, 30:
	// case score >= 10 && score <= 30:
	switch oper {
	case "+":
		fmt.Printf("%d + %d = %d\n", num1, num2, num1 + num2)
	case "-":
		fmt.Printf("%d - %d = %d\n", num1, num2, num1 - num2)
	case "*":
		fmt.Printf("%d * %d = %d\n", num1, num2, num1 * num2)
		fallthrough
	case "/":
		fmt.Printf("%d / %d = %d\n", num1, num2, num1 / num2)
	}
}