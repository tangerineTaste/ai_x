/*  array 함수 : 가변인자함수(파이썬에선 튜플매개변수)
 * 매개변수가 0개 : length가 0인 배열 생성 return
 * 매개변수가 1개 : length가 매개변수 만큼의 크기인 배열 생성 return
 * 매개변수가 2개 이상 : 매개변수로 배열을 생성 return */
function array(){ 
    let result = [];
    if(arguments.length==1){
        for(cnt=1; cnt<=arguments[0]; cnt++){
            result.push(null);
        }
    }
    else if(arguments.length>=2){
        for(data of arguments){
            result.push(data);
        }
    }
    return result;
}


var arr1 = array();
var arr2 = array(2);
var arr3 = array(2, 3);
var arr4 = array(2, 3, '사');
console.log(arr1);
console.log(arr2);
console.log(arr3);
console.log(arr4);