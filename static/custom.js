//select elements
let sidenav = document.querySelector(".sidenav")
let main = document.querySelector(".toggle")

open_nav = ()=>{
    sidenav.style.width = "280px"
    main.style.marginLeft = "280px"
}
close_nav = ()=>{
    sidenav.style.width = "0"
    main.style.marginLeft = "0"
}