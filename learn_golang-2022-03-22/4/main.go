package main
import (
	"fmt"
	"math/rand"
)


func main(){
	// fmt.Println("Hello World")
	// name := "rafiq";
	// fmt.Println(name)
	// for i:=0; i<=10;i++{
	// 	fmt.Println(i)	
	// }

	for {
		num := rand.Intn(100)
		fmt.Print(num,',')
		if num == 50 {
			fmt.Print("Loop Is Brack")
			break
		}
	}

}