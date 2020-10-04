package main

import (
	"fmt"
	"net/http"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(4)
	fmt.Println("GOMAXPROCS=", runtime.GOMAXPROCS(-1))
	fmt.Println("NumCPU=", runtime.NumCPU())
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "Hello World")
	})
	http.ListenAndServe(":8080", nil)
}