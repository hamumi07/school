const page1=document.createElement("div");
page1.style.cssText = `
    width: 100vw;
    height: 100vh;
    background-color: #cff5ff;
`;
page1.animate([
    {opacity:0.4,transform:'translateY(-100%)'},
    {opacity:1,transform:'translateY(0)'}
],{
    duration:1500,
    fill:'forwards',
    easing:'ease-in-out'
});
document.body.appendChild(page1);