let icon = document.querySelector('.dots');
let option = document.querySelector('.options');
let symbol = document.querySelector('.change');
let border = document.querySelector('.page');
let cancel = document.querySelector('.cancel');
let msg = document.querySelector('.msg');

icon.addEventListener('click', () => {
    let computedStyle = window.getComputedStyle(option);
    let display = computedStyle.getPropertyValue('display');

    if (display === "none") {
        option.style.display = "block";
        option.style.right = "0";
        border.style.width = "400px"
        symbol.className = "fas fa-times dots change "
    } else {
        option.style.display = "none";
        symbol.className = "fas fa-ellipsis-v change"
        border.style.width = ""
    }
});

cancel.addEventListener('click',()=>{
    msg.innerHTML = '';
})

