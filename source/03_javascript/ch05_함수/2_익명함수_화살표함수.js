let funVar = function(){
    console.log('1. 매개변수 없는 일반 함수 호출');
}
funVar();
funVar = ()=> console.log('2. 매개변수 없는 화살표 함수 호출');
funVar();
funVar = function(i){
    console.log('3. 매개변수가 하나 있는 일반 함수 호출');
    console.log('매개변수 값 = ', i);
}
funVar(20);
funVar = i=>{
    console.log('4. 매개변수가 하나 있는 화살표 함수 호출');
    console.log('매개변수 값 = ', i);
}
funVar(30);
funVar = function(i){
    console.log('5. 매개변수가 하나의 한줄짜리 일반 함수 호출', i);
}
funVar(20);
funVar = i=> console.log('6. 매개변수가 하나의 한줄짜리 화살표 함수 호출', i);
funVar(20);
funVar = function(x){
    return x*x;
}
console.log('7. return문 만 있는 일반함수 호출', funVar(10));
funVar = x => x*x;
console.log('8. return문 만 있는 화살표 함수 호출', funVar(10));
funVar = (x,y) => x*10 + y;
console.log('9 매개변수 2개짜리 return 문장의 화살표 함수 호출', funVar(5,3));

var arr=[10, '홍길동','신림동'];
arr.forEach(function(data,idx){
    console.log(idx + '번째 데이터는 : ' + data);
});
arr.forEach((data,idx)=>console.log(idx + '번째 데이터는 : ' + data));
arr.forEach(data => console.log(data));