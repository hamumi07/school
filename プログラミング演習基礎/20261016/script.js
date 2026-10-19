console.log('こんにちは');

const a=1;
const b=2;
console.log(a+b);

const c='わたしは';
const d='人間です';
console.log(c+d);

function ab(a,b){
    console.log(a+b);
}
ab(1,2);

function cd(c,d){
    console.log(c+d);
}
cd('わたしは','人間です');


let person={
    name:'田中',
    age:21,
}
person.height=176;

function showPerson(p) {
    console.log(p.name);
    console.log(p.age);
    console.log(`私は${p.name}で、${p.age}歳です。身長は${p.height}です。`);
}
showPerson(person);
