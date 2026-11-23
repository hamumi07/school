const page1=document.createElement("div");
page1.style.cssText = `
    width: 100vw;
    height: 100vh;
    background-color: #cff5ff;
`;
page1.animate([
    {opacity:0},
    {opacity:1}
],{
    duration:1500,
    fill:'forwards'
});
document.body.appendChild(page1);