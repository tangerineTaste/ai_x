class Student{
    constructor(name, kor, mat, eng, sci){
        this.name = name;
        this.kor = kor;
        this.mat = mat;
        this.eng = eng;
        this.sci = sci;
    }
    getSum(){
        return this.kor + this.mat + this.eng + this.sci;
    }
    getAvg(){
        return this.getSum() / 4;
    }
    toString(){
        return 'name' + this.name +
                'kor' + this.kor + 
                'mat' + this.mat + 
                'eng' + this.eng + 
                'sci' + this.sci + 
                '합' + this.getSum() +
                '평균' + this.getAvg();
    }
} // class
var hong = new Student("홍", 100, 100 ,99, 100);
console.log(hong.getAvg());