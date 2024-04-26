function Main(input) {
    const data = input.split(" ");

    console.log(input);
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
