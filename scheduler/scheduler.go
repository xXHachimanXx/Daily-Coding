package main

import (
	"fmt"
	"time"
)

type f func()

func scheduler(function f, n int) {
	time_to_sleep := fmt.Sprintf("%dms", n)
	milliseconds, error := time.ParseDuration(time_to_sleep)

	if error != nil {
		fmt.Errorf("Fail: ", error)
	}

	time.Sleep(milliseconds)
	function()
}

func any_function() {
	fmt.Println("Hello world!!!")
}

func main() {
	fmt.Println(time.Now())
	scheduler(any_function, 2000)
	fmt.Println(time.Now())
}
