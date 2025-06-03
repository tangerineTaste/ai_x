-- DCL
--  (사용자 계정 생성 CREATE USER, 권한부여 GRANT, 권한박탈 REVOKE, 사용자계정삭제 DROP USER
--  트랜젝션 명령어
-- DDL : 테이블 생성 CREATE TABLE, 테이블구조변경 ALTER TABLE, 테이블 삭제 DROP TABLE 
-- DML : INSERT, SELECT, UPADTE, DELETE - DML은 취소 가능

--------------
-- ★ DDL ★ --
--------------

-- 1. 테이블 생성(CREATE TABLE 테이블명..) : 테이블 구조를 정의
CREATE TABLE BOOK(
    BOOKID NUMBER(4), -- BOOKID는 숫자 4자리
    BOOKNAME VARCHAR(20), --BOOKNAME필드의 타입은 문자 20BYTE
    PUBLISHER VARCHAR(20),
    RDATE DATE,          -- RDATE 필드의 타입은 DATE형
    PRICE NUMBER(8,2),   -- PRICE 필드의 타입은 숫자전체8자리 중 소숫점2자리
    PRIMARY KEY(BOOKID) -- 제약조건 : BOOKID를 PRIMARY KEY 필드로(NOT NULL, UNUQUE)
);
SELECT * FROM BOOK;
DESC BOOK;

DROP TABLE BOOK; -- 2. 테이블삭제
CREATE TABLE BOOK(
    BOOKID NUMBER(4) PRIMARY KEY, 
    BOOKNAME VARCHAR(20), 
    PUBLISHER VARCHAR(20),
    RDATE DATE,          
    PRICE NUMBER(8) 
);
-- EX. DEPT01 : DEPTNO(숫지2; PK), DNAME(문자14), LOC(문자13)
CREATE TABLE DEPT01(
    DEPTNO NUMBER(2) PRIMARY KEY,
    DNAME VARCHAR(14),
    LOC VARCHAR(13)
);