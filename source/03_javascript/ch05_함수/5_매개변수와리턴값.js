console.log(pow(3,3));
// 선언된 매개변수보다 많은 매개변수로 호출
console.log(pow(5,3,3));
// 선언된 매개변수보다 적은 매개변수로 호출 절달되지 않은 파라미터는 undefined로 
console.log(pow(5));

function pow(x,y){
    // x의 y제곱을 return
    result = 1;
    for(i=0; i<y; i++){
        result *= x;
    }
    console.log(arguments.length);
    //return result;
}