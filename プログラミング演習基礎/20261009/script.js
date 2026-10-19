/*
最初の練習コード
ハローワールド

*/

//この行の説明・・・・
console.log("こんにちは");

let a=10;
console.log(a);
let b=20;
console.log(a+b);

const c=30;
const d=40;
console.log(c+d);

const e="わたしは";
const f="ハムです";
console.log(e+f);

let name ="鈴木";
let str =`こんにちは、${name}さん。今日も良い天気ですね！`;
console.log(str);

let data =["JavaScript","Python","PHP","Rudy","Perl"];
console.log(data[0]);
console.log(data[2]);

let data1=[
    ["JavaScript","js"],
    ["Python","py"],
    ["Rudy","rb"],
];
console.log(data1[1][0]);

let book={
    title:"JavaScript本格入門",
    price:2980,
    publisher: "技術評論社",
};
console.log(book.title);
console.log(book["title"]);

let x=15;
if(x>=10){
    console.log("変数xは10以上です。");
} else{
    console.log("変数xは10未満です。");
}

let rank="B";
switch(rank){
    case"A":
        console.log("Aランクです。");
        break;
    case"B":
        console.log("Bランクです。");
        break;
    case"C":
        console.log("Cランクです。");
        break;
    default:
        console.log("ランク外です。");
        break;
}

let i = 5;
while(i<10){
    console.log(`iの値は${i}"`);
    i++;
}

let ij = 5;
do{
    console.log(`ijの値は${ij}`);
    ij++;
}while(ij<10);

for (let i=5; i<10;i++){
    console.log(`iの値は${i}`)
}
