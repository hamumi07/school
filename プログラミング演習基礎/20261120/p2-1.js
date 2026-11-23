const bt1   = document.createElement('div');
const box1 = document.createElement('div');
bt1.style.cssText = `
    width: 100px;
    height: 100px;
    background-color: red;
    position: absolute;
    top: 20px;
    left: 20px;
    z-index: 10;
    `;
box1.style.cssText = `
    width: 100vw;
    height: 100vh;
    background-color: #959595;
    position: absolute;
    top: 0;
    left: 0;
    display: none;
    `;

bt1.addEventListener('click', ()=> {
    box1.style.display = 'block';
}); 

document.body.append(bt1);
document.body.append(box1);