let icon = document.querySelector('.dots');
let option = document.querySelector('.options');
let symbol = document.querySelector('.change')

icon.addEventListener('click', () => {
    let computedStyle = window.getComputedStyle(option);
    let display = computedStyle.getPropertyValue('display');

    if (display === "none") {
        option.style.display = "block";
        option.style.left = "62%";
        symbol.className = "fas fa-times dots change "
    } else {
        option.style.display = "none";
        symbol.className = "fas fa-ellipsis-v change"
    }
});
