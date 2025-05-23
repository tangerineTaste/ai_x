Date.prototype.getIntervalDay = function(otherday){
    // this와 otherday 사이의 날짜 수를 return 
    // now.getIntervalDAy(openday) : this가 now, otherday가 openday
    // openday.getIntervalDay(now) : this가 openday, otherday가 now
    // this>otherday?
    //     this.getTime() - otherday.getTime():
    //     otherday.getTime() - this.getTime();

    return Math.trunc(Math.abs(this.getTime() - otherday.getTime())/ (1000*60*60*24));
};
