// false로 간주되는 값 : undefined, 0, NaN, '', null
// Boolean(값) : Boolean 으로 형변환
// String() : String ``
// Number() : Numer ``
var i;
console.log(Boolean(i));
console.log(Boolean(0));
console.log(Boolean(NaN));
console.log(Boolean(null));
console.log(Boolean(''));
console.log(Boolean(' '));

