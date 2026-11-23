let div=document.createElementById("div");
div.style.width="120px";
div.style.height="150px";
div.style.backgroundColor="red";
document.body.appendChild(div);

div.addEventListener("click", ()=>{
    div.remove();
});

