const menu=['Home', 'Works', 'About'];

const pages = [];
for (const i of menu) {
    const bt=document.createElement('div');
    bt.textContent=i;

    const page=document.createElement('div');
    pages.push(page);

    bt.style.cssText=`
    width:100px;
    height:100px;
    background-color: red;
    position :absolute;
    top: 0;
    left: ${20 + menu.indexOf(i) * 120}px;
    z-index: 10;
    `;

    page.style.cssText=`
    width:100vw;
    height:100vh;
    background-color: #f9cdcd;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 5;
    display: none;
    `;

    document.body.append(bt);
    document.body.append(page);

    bt.addEventListener('click', ()=>{
        //page.style.display='block';//
        pages.forEach((p) => {
            p.style.display='none';
        });   
        page.style.display='block';    
        
    });
}