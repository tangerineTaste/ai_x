i = Number('');
console.log('i=1',i);
i = parseInt('')
console.log('i=', NaN, '- 타입=', typeof(i));
f = 10/3;
console.log(f);
a = 10/0
console.log(a, typeof(a));

console.log(isNaN(i));
console.log(isNaN(f));
console.log(isFinite(f));
console.log(isFinite(a));