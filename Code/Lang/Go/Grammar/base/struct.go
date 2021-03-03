package main

import "fmt"

func main() {
	// struct is value type

	var p Person
	fmt.Println("p:", p)

	p.name = "bob"
	p.age = 18
	p.sex = "male"
	p.address = "NY"

	fmt.Println("p:", p)

	p2 := Person{
		name:    "li",
		age:     20,
		sex:     "female",
		address: "BJ",
	}

	fmt.Println("p2:", p2)

	// struct pointer
	var pp *Person
	pp = &p
	fmt.Println("pp:", pp)
	pp.age = 40
	fmt.Println("*pp:", *pp)
	fmt.Println("p:", p)

	pp2 := new(Person)
	fmt.Println("pp2:", pp2)

	s := struct {
		name string
		age  int
	}{
		name: "li",
		age: 13,
	}

	fmt.Println("s:", s)
}

type Person struct {
	name    string
	age     int
	sex     string
	address string
}

type Worker struct {
	string
	int
}
