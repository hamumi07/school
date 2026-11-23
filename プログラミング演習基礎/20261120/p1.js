const box1 = document.createElement('div');
box1.style.width="150px";
box1.style.height="150px";
box1.style.backgroundColor="red";
document.body.appendChild(box1);

box1.addEventListener("click", ()=>{
    box1.style.display="none";
});