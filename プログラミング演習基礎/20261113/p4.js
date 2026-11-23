let div=document.getElementById("div");
div.style.cssText=`
    background-color:red;
    width:120px;
    height:150px;
`;
document.body.appendChild(div);

div.addEventListener("click", ()=>{
    div.remove();
});
