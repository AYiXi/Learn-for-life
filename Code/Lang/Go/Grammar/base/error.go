package main

import (
	"fmt"
	"math"
)

func main() {
	radius := -3.0
	a, err := circleArea(radius)
	if err != nil {
		fmt.Printf("error: %s\n", err)
		if err, ok := err.(*areaError); ok {
			fmt.Printf("r:%.2f\n", err.radius)
		}

	} else {
		fmt.Printf("a: %.2f\n", a)
	}

	w := -2.0
	h := 2.0

	a2, err := rectArea(w, h)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(a2)
	}
	//fmt.Println(a2)
}

// 定义一个结构体, 表示错误类型
type areaError struct {
	msg    string
	radius float64
}

// 实现 error 接口, 就是实现 Error() 方法
func (e *areaError) Error() string {
	return fmt.Sprintf("error: r=%.2f, %s", e.radius, e.msg)
}

func circleArea(radius float64) (float64, error) {
	if radius < 0 {
		return 0, &areaError{"r < 0", radius}
	}
	return math.Pi * radius * radius, nil
}

type rectangleAreaError struct {
	msg    string
	length float64
	width  float64
}

func (e *rectangleAreaError) Error() string {
	return e.msg
}

func (e *rectangleAreaError) lengthNegative() bool {
	return e.length < 0
}

func (e *rectangleAreaError) widthNegative() bool {
	return e.width < 0
}

func rectArea(length, width float64) (float64, error) {
	msg := ""
	if length < 0 {
		msg = "length < 0"
	}

	if width < 0 {
		if msg == "" {
			msg = "width < 0"
		} else {
			msg += ", width < 0"
		}
	}

	if msg != "" {
		return 0, &rectangleAreaError{msg, length, width}
	} else {
		return width * length, nil
	}
}
