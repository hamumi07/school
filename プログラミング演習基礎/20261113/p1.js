let a=[];
a.push(1, 2, 3, 4, 5);
console.log(a);

for (let i of a) {
    if (i >= 4) {
        console.log("4以上です");
    }
}