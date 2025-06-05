-- DCL(계정생성, 권한부여, 권한박탈, 계정삭제, 트랜젝션 명령어)
-- DDL(테이블생성, 테이블삭제, 제약조건, 시퀀스없음)
-- DML(INSERT, UPDATE, DELETE, SELECT)
	-- OUTER JOIN, AND=&&, OR=||, CONCAT함수를 이용하여 연결연산자 대치

show databases; -- database들 리스트
use world;
show tables;
select * from city;

-- ---------- --
--  ※ DCL ※  --
-- ---------- --
create user user01 identified by 'password'; -- 계정생성 아이디:userid, 비번:password
grant all privileges on *.* to user01; -- dba 권한부여
revoke all privileges on *.* from user01; -- 권한 박탈
drop user user01; -- 계정삭제

-- ---------- --
--  ※ DDL ※  --
-- ---------- --
/* MySQL 타입 : numeric(n, d), varchar(n), date
정수 : tinyint(1byte), smallint(2byte), mediumint(3byte),
	  int/integer(4byte), bigint(8byte)
실수 : float(n, d; 4byte), double(n,d;8byte)
문자 : char(n), text, mediumtext(16MB), longtext(4GB) 
날짜 : date, datetime, time, year, tiemstamp
*/

show databases;
create database devdb; -- 데이터베이스 생성
use devdb;
select database(); -- 현제 들어와 있는 데이터베이스

drop table if exists emp;
create table emp(
	empno numeric(4) primary key,
    ename varchar(6) not null,
    nickname varchar(6) unique,
    sal numeric(7,2) check(sal>0),
    comm numeric(7,2) default 0
);

insert into emp (empno, ename, nickname, sal) values(1,'홍길동동동동','여섯글자닉넴',-1);
insert into emp (empno, ename, nickname, sal) values(1,'홍길동동동동','여섯글자닉넴',1000);
select * from emp;

-- MySQL에서는 시퀀스가 없음
-- MySQL 10, 20, 30, ... 을 인위적인 primary key
set @@auto_increment_increment = 10; -- default 1
set @@auto_increment_offset=10; 	 -- defualt 1
drop table if exists major;
create table major(
	mcode int primary key auto_increment,
    mname varchar(30),
    moffice varchar(30)
);
insert into major(mname,moffice) values('컴공','m102호');
insert into major(mname,moffice) values('ai','m103호');
insert into major(mname,moffice) values('정보통신','m104호');
select * from major;

drop table if exists student;
create table student(
	sno   numeric(4) ,
    sname varchar(30) not null,
    mcode int, 
    primary key(sno),
    foreign key (mcode) references major(mcode)
);
insert into student values(101, '홍길동',1);
insert into student values(102, '신길동',2);
insert into student values(103, '신길동',3);
insert into student values(104, '유길동',4);

select sno,sname, m.mcode,mname,moffice
	from student s, major m
    where s.mcode=m.mcode; -- equi, non-equi, self join 은 사용법 동일

delete from student where mcode=3;

select sno,sname,m.mcode,mname,moffice
	from student s right outer join major m
    on s.mcode=m.mcode; -- outer join
    
-- ---------- --
--  ※ DML ※  --
-- ---------- --
drop table if exists division;
create table division(
	DNO int not null primary key,
    dname varchar(20),
    phone varchar(20),
    position varchar(20)
);

drop table if exists personal;
create table personal (
	pno int primary key,
	pname varchar(10) not null,
    job varchar(15) not null,
    manager int,
    startdate date,
    pay int, 
    bonus int,
	dno int ,
    foreign key(dno) references division(dno)
);
insert into division values (10, 'finance','02-777-7777','종로');
insert into division values (20, 'research','041-888-7777','대전');
insert into division values (30, 'sales','02-999-7777','인천');
insert into division values (40, 'marketing','02-555-7777','강남');
select * from division;

insert into personal values (1111,'smith','manager', 1001, '1990-12-17', 1000, null, 10);
insert into personal values (1112,'ally','salesman',1116,'1991-02-20',1600,500,30);
insert into personal values (1113,'word','salesman',1116,'1992-02-24',1450,300,30);
insert into personal values (1114,'james','manager',1001,'1990-04-12',3975,null,20);
insert into personal values (1001,'bill','president',null,'1989-01-10',7000,null,10);
insert into personal values (1116,'johnson','manager',1001,'1991-05-01',3550,null,30);
insert into personal values (1118,'martin','analyst',1111,'1991-09-09',3450,null,10);
insert into personal values (1121,'kim','clerk',1114,'1990-12-08',4000,null,20);
insert into personal values (1123,'lee','salesman',1116,'1991-09-23',1200,0,30);
insert into personal values (1226,'park','analyst',1111,'1990-01-03',2500,null,10);

select * from division;
select * from personal;

-- 1. 사번, 이름, 급여를 출력
select pno, pname, pay from personal;
-- 2. 급여가 2000~5000 사이 모든 직원의 모든 필드
select * 
	from personal 
	where pay between 2000 and 5000;
-- 3. 부서번호가 10또는 20인 사원의 사번, 이름, 부서번호
select pno, pname, dno 
	from personal 
    where dno in (10,20);
-- 4. 보너스가 null인 사원의 사번, 이름, 급여 급여 큰 순정렬
select pno,pname, pay 
	from personal 
	where bonus is null 
    order by pay desc;
-- 5. 사번, 이름, 부서번호, 급여. 부서코드 순 정렬 같으면 PAY 큰순
select pno, pname, dno, pay
	from personal
    order by dno, pay desc;
-- 6. 사번, 이름, 부서명
select pno, pname, dname
	from personal p, division d
    where p.dno = d.dno;
-- 7. 사번, 이름, 상사이름
select p.pno, p.pname, m.pname
	from personal p, personal m
    where p.manager = m.pno;
-- 8. 사번, 이름, 상사이름(상사가 없는 사람도 출력하되 상사가 없는 경우 ★CEO★로 출력) 
select p.pno, p.pname, ifnull(m.pname ,'★CEO★') "상사"
	from personal p left outer join personal m
    on p.manager = m.pno ;
-- 8-1 사번, 이름, 상사사번(상사가 없으면 ceo로 출력. ifnull함수의 매개변수의 타입이 상이해도 상관없음)
select p.pno, p.pname, ifnull(m.pno ,'ceo') "상사"
	from personal p left outer join personal m
    on p.manager = m.pno ;
-- 8-2. 사번, 이름, 상사이름, 부서명(상사가 없는 사람도 출력) – 같이 합시다
select p.pno, p.pname, m.pno "상사이름", d.dname
	from division d, personal p left outer join personal m
    on p.manager = m.pno
    where p.dno = d.dno;
-- 9. 이름이 s로 시작하는 사원 이름 (like 이용, substr함수이용, instr함수 이용등 다양하게 사용 가능)
select pname
	from personal
    where pname like 's%';
-- 10. 사번, 이름, 급여, 부서명, 상사이름
select p.pno, p.pname, m.pname "상사이름" , d.dname 
	from division d, personal p, personal m
    where p.manager = m.pno and p.dno = d.dno;



-- oracle과 다른 함수들
select pname||'는'||job from personal; -- || : or연산자
select concat(pname, '는', job) message from personal;

select sysdate();
-- date_format(날짜, 포맷) => 날짜형을 문자로;
-- date_format(문자, 포맷) => 문자형을 날짜형로;
	-- %Y(년도 4자리), %y(년도 2자리), %m(월 01,02..12), %c(1,2,...31)
    -- %d(일 01,02,00), %e(1,2,...) %H(24시간), %h(12시간), %p(오후,오전), %i(분), %s(초)
select date_format(sysdate(), '%y-%m-%d') now;

-- nvl() => if()나 ifnull() 함수 사용
select * from personal;
select pname, pay, ifnull(bonus,0) bonus from personal;
select pname, pay, if(bonus is null,0,bonus) bonus from personal;
select pname, pay, if(pay>=3000, '부자','평범') pay2 from personal;