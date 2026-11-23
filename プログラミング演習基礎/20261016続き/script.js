let photo={
    file:'aaa.jpg',
    text:'aaaの説明'
}
console.log(photo.file);
console.log(photo.text);

const img =document.createElement('img');
img.src=photo.file;
img.alt=photo.text;
img.width=300;
document.body.append(img);