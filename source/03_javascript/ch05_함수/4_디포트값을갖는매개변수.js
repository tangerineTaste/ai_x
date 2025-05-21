function pow(x=1,y=2){
    // x의 y제곱을 return
    result = 1;
    for(i=0; i<y; i++){
        result *= x;
    }
    return result;
}
console.log(pow(3,2));
