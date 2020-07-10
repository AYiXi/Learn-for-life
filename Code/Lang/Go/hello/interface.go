package main

import "fmt"

func main() {
	mouse := Mouse{name: "red"}
	disk := FlashDisk{name: "sandi"}

	testInterface(mouse)
	testInterface(disk)
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

func testInterface(usb USB)  {
	usb.start()
	usb.end()
}