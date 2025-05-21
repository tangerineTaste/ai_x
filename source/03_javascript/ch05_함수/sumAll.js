function sumAll(){
    sum = 0;
    if(arguments.length>0){
        for(data of arguments){
            sum += data;
        }
    } 
    else{
        sum = -999;
    }
    return sum;
}
// test 
// console.log(sumAll());
// console.log(sumAll(0));
// console.log(sumAll(1,2));
// console.log(sumAll(1,2,3,4,5));