package main

import "fmt"

func main() {
	mouse := Mouse{name: "red"}
	disk := FlashDisk{name: "sandi"}

	testInterface(mouse)
	testInterface(disk)

	var a1 EmptyInterface = Cat{"red"}
	var a2 EmptyInterface = Person2{"li", 30}
	var a3 = "haha"
	var a4 = 123
	fmt.Println(a1, a2, a3, a4)

	emptyInterface(a1)
	emptyInterface(a2)

	emptyInterface2(a3)
	emptyInterface2(a4)

	// value 任意类型的 map
	map1 := make(map[string]interface{})
	// value 任意类型的 slice
	slice1 := make([]interface{}, 0, 10)
	fmt.Println(map1, slice1)

	mao := Mao{}
	mao.testa()
	mao.testb()
	mao.testc()
}

type USB interface {
	start()
	end()
}

type Mouse struct {
	name string
}

type FlashDisk struct {
	name string
}

func (mouse Mouse) start() {
	fmt.Println("start:", mouse.name)
}

func (mouse Mouse) end() {
	fmt.Println("end:", mouse.name)
}

func (disk FlashDisk) start() {
	fmt.Println("start:", disk.name)
}

func (disk FlashDisk) end() {
	fmt.Println("end:", disk.name)
}

func testInterface(usb USB) {
	usb.start()
	usb.end()
}

// empty interface
type EmptyInterface interface {
}

type Cat struct {
	color string
}

type Person2 struct {
	name string
	age  int
}

// 传入任何类型的参数
func emptyInterface(ei EmptyInterface)  {
	fmt.Println(ei)
}

func emptyInterface2(ei interface{})  {
	fmt.Println(ei)
}

type A interface {
	testa()
}

type B interface {
	testb()
}

type C interface {
	A
	B
	testc()
}

type Mao struct {

}

func (m Mao) testa() {
	fmt.Println("testa")
}

func (m Mao) testb() {
	fmt.Println("testb")
}

func (m Mao) testc() {
	fmt.Println("testc")
}