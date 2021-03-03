package main

import (
	"fmt"
	"reflect"
	"sort"
	"strconv"
)

func main() {
	var map1 map[int]string // 没有初始化, nil
	var map2 = make(map[int]string)
	var map3 = map[string]int{"go": 90, "python": 80, "java": 60}
	mapSlice := make([]map[string]string, 0, 3)
	fmt.Printf("%T \n", mapSlice)

	fmt.Println(map1)
	fmt.Println(map2)
	fmt.Println(map3)

	fmt.Println(map1 == nil)

	if map1 == nil {
		map1 = make(map[int]string)
		fmt.Println(map1 == nil)
	}

	map1[1] = "hello"
	fmt.Println(map1, reflect.TypeOf(map1))

	v1, ok := map1[40]
	fmt.Println(v1, ok)

	for k, v := range map3 {
		fmt.Println(k, v)
	}

	k := []int{1, 3, 2, 5, 4}
	sort.Ints(k)
	fmt.Println(k)

	delete(map3, "go")
	fmt.Println(map3)


	fmt.Println("============")

	str1 := "true"
	b1, err := strconv.ParseBool(str1)
	if err == nil {
		fmt.Printf("%T, %t \n", b1, b1)
	}
	str2 := strconv.FormatBool(b1)
	fmt.Printf("%T, %s \n", str2, str2)

	str3 := "100"
	i2, _ := strconv.ParseInt(str3, 10, 64)
	str4 := strconv.FormatInt(i2, 10)

	fmt.Println(str4)

	i3, _ := strconv.Atoi("-42")
	str5 := strconv.Itoa(i3)

	fmt.Println(str5)
}
