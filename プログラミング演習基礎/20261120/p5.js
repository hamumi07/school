const page1=document.createElement("div");
page1.style.cssText = `
    width: 100vw;
    height: 100vh;
    background-color: #cff5ff;
`;
page1.animate([
    {opacity:0.4,transform:'translate(-100%,0)'},
    {opacity:1,transform:'translate(0,0)'}
],{
    duration:1500,
    fill:'forwards',
    easing:'cubic-bezier(.28,1.56,.87,-0.81)'
});
document.body.appendChild(page1);