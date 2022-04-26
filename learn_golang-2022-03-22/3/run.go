package main

import "fmt"

type person struct {
	name    string
	age     int
	address string
	phone   string
}

func testFunc(x person ) {
	for k, v := range person { 
		fmt.Printf("key[%s] value[%s]\n", k, v)
	}
}
func main() {
	info := person{
		name:    "Niyaz",
		// age:     19,
		address: "Dhaka",
		phone:   "1234"}
	testFunc(info)
}
