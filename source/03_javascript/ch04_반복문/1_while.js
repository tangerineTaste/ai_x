/*
i=0;
while(i<100){
    i++;
    console.log(i);
}
i =0;
do{
    i++;
    console.log(i);
}while(i<0); 
*/

var startTime = new Date().getTime();
//console.log(startTime);
cnt = 0
do{
    cnt++;
}while(new Date().getTime() < startTime + 1000)
console.log(cnt);