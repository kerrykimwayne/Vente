const charge = document.querySelector('.charges')
const charges = document.querySelector('div:first-child')
window.addEventListener('load', () => {
    charge.classList.add('chargefin')
})
charges.remove()


const dropbtn = document.querySelector('.dropbtn')
const dropdown = document.querySelector('.dropdown-contenu')
dropbtn.addEventListener('click', () => {
    dropdown.classList.toggle('hid')
})

const affichage = document.querySelectorAll('.bordu')
const article_info = document.querySelector('.article-info')
const art = document.querySelector('.libele')
let place = 0
let affiche = Array.from(affichage)
   

