//select elements
let sidenav = document.querySelector(".sidenav")
let main = document.querySelector("main")

open_nav = ()=>{
    sidenav.style.width = "200px"
    main.style.marginLeft = "230px"
}
close_nav = ()=>{
    sidenav.style.width = "0"
    main.style.marginLeft = "0"
}
confirm = ()=>{
    alert(`Save changes?!`)
}