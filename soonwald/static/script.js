
const background = document.getElementById("background")

var lastCircleHeight = 0
var color = true
var i;
for (i = 0; i < 10; i++) {
    lastCircleHeight = lastCircleHeight + Math.floor(Math.random() * 20)
    var circle = document.createElement("div")
    circle.style.backgroundColor = color ? "#ACBA99" : "#6B9C7F"
    var size = Math.floor(Math.random() * 40)
    circle.style.zIndex = "-2"
    circle.style.height = `${size}vw`
    circle.style.width = `${size}vw`
    circle.style.top = `${lastCircleHeight}vh`
    circle.style.left = `${Math.floor(Math.random() * 80)}vw`
    circle.classList.add("background-circle","rellax")
    circle.setAttribute("data-rellax-speed", `${Math.floor(Math.random() * 10)}`)
    background.appendChild(circle)

    color = !color

}

