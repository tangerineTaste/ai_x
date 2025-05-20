// var : 변수 선언시 사용. 변수 재선언 가능. 전역변수로 주로 사용
// let : 변수 선언시 사용. 변수 재선언 불가능. 블록{} 레벨 범위에서만 적용
//const : 상수 선언시 사용. 
var v = 10; 
var v = 20;
v++;
++v;
v--;
--v;
console.log('v=' + v);
let l;
l = 10;
const C = [10,20,30]; //배열선언
C[0] = 99;
console.log(C);