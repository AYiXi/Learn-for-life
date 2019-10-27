var numbers = [1, 2, 3, 4, 5];
var length = numbers.length;
for (var i = 0; i < length; i++) {
  numbers[i] *= 2;
}

numbers.forEach((value, index, item) => {
    if (index>3){
        numbers.length = 3
    }
})

console.table(numbers)
console.table([1,3,4,'fdsf', ['1','ffdasfdsf']])
