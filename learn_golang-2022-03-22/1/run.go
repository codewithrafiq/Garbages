package main

import (
	"fmt"
	"time"
	"reflect"
)

func test() int {
	fmt.Println("test");

	name := "123"

	inttttt := int64(name)

	return inttttt
}

func main() {
	time := time.Now()
	fmt.Println(time)
	fmt.Println(reflect.TypeOf(time))
	test();
}
