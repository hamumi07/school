let menu=['Home', 'Works', 'About'];
let boxes = [];

for (const i of menu) {
    const bt   = document.createElement('div');
    bt.textContent = i;
    const box = document.createElement('div');
    bt.style.cssText = `
        width: 100px;
        height: 100px;
        background-color: red;
        position: absolute;
        top: 20px;
        left: ${20 + menu.indexOf(i) * 120}px;
        z-index: 10;
        `;
    box.style.cssText = `
        width: 100vw;
        height: 100vh;
        background-color: #959595;
        position: absolute;
        top: 0;
        left: 0;
        display: none;
        `;
    boxes.push(box);
    bt.addEventListener('click', ()=> {
            boxes.forEach(b => {
            b.style.display = 'none';
        });
        box.style.display = 'block';
        
    }); 
    document.body.append(bt);
    document.body.append(box);
    };
