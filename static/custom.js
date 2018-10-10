// Select the element
let home = document.querySelector("#home")
let profile = document.querySelector("#profile")
let info = document.querySelector("#info")
let logout = document.querySelector("#logout")
//add eventlisteners to home
home.addEventListener("mouseover", ()=>{
    home.style.background = "#65849e"
})
home.addEventListener("mouseout", ()=>{
    home.style.background = "white"
})
//add eventlisteners to profile
profile.addEventListener("mouseover", ()=>{
    profile.style.background = "#65849e"
})
profile.addEventListener("mouseout", ()=>{
    profile.style.background = "white"
})
//add eventlisteners to info
info.addEventListener("mouseover", ()=>{
    info.style.background = "#65849e"
})
info.addEventListener("mouseout", ()=>{
    info.style.background = "white"
})
//add eventlisteners to logout
logout.addEventListener("mouseover", ()=>{
    logout.style.background = "#65849e"
})
logout.addEventListener("mouseout", ()=>{
    logout.style.background = "white"
})
// JS for homepage side navbar
let sidenav = document.querySelector(".sidenav")
let toggle = document.querySelector(".toggle")
openNav = ()=>{
    sidenav.style.width = "300px"
    toggle.style.marginLeft = "300px"
}
closeNav = ()=>{
    sidenav.style.width = "0"
    toggle.style.marginLeft = "0"
}