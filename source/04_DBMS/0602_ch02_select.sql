-- [II] SELECT 문
-- 1. SELECT문 작성법
SHOW USER;
    -- 현재 계정(실행 : CTRL + ENTER)
SELECT * FROM TAB; --현 계정이 가지고 있는 테이블
SELECT * FROM EMP; -- EMP테이블의 모든 열, 모든 행
SELECT * FROM DEPT;
SELECT * FROM SALGRADE;

--2. 특정열만 출력
DESC EMP;
    -- EMP 테이블 구조를 나타내는 ORACLE 명령어
SELECT EMPNO, ENAME, SAL, JOB FROM EMP; -- EMPNO, ENAME, SAL, JOB열만 모든 행 검색
SELECT EMPNO AS "사 번", ENAME AS "이름", SAL AS "급여", JOB FROM EMP;
SELECT EMPNO "사 번", ENAME 이름, SAL 급여, JOB FROM EMP; -- AS를 삭제, 따옴표를 생략해도 된다. (공백이 있을 경우는 안됨)
SELECT EMPNO NO, ENAME ENAME, SAL SALARY FROM EMP;

-- 3. 특정 행 출력 : WHERE절(조건절) - 비교연산자 : 같다(=), 다르다 (!=), >,>=,<,<= 
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL=3000;
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL>3000;
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL!=3000;
    -- 비교연산자는 숫자, 문자, 날짜형 모두 가능
    -- EX1) 사원이름(ENAME)이 'A', 'B', 'C'로 시작하는 사원의 모든 필드
    -- A < AA < AAA < AAAA < B < C < D
    SELECT * FROM EMP WHERE ENAME < 'D';
    -- EX) 82년도 이전에 입사한 사원의 모든 필드
    SELECT * FROM EMP WHERE HIREDATE < '82/01/01';
    -- EX3) 부서번호(DEPTNO)가 10번인 사원의 모든 필드
    SELECT * FROM EMP WHERE DEPTNO=10;
    -- EX4) 이름(ENAME)이 FORD인 직원의 EMPNO, ENAME, MGR(상사의 사번)
    SELECT EMPNO, ENAME, MGR 
        FROM EMP 
            WHERE ENAME='FORD';
    
    -- SQL문은 대소문자 구별없음, 데이터는 대소문자 구별
    
-- 3. 특정 행 출력 : WHERE절(조건절) - 논리연산자 : AND, OR, NOT
    -- EX1. 급여(SAL)가 2000이상 3000이하인 직원의 모든 필드
    SELECT * 
        FROM EMP 
        WHERE SAL>2000 AND SAL<3000;
    -- EX2. 82년도에 입사한 사원의 모든 필드
    SELECT *
        FROM EMP
        WHERE HIREDATE >='82/01/01' AND HIREDATE <= '83/01/01';
-- 4. 날짜 표기법 세팅(현재 : YY/MM/DD 또는 RR/MM/DD)
    ALTER SESSION SET NLS_DATE_FORMAT = 'MM-DD-YYYY';
    ALTER SESSION SET NLS_DATE_FORMAT = 'RR-MM-DD';
    SELECT * FROM EMP;
    SELECT TO_CHAR(HIREDATE, 'YY/MM/DD') FROM EMP;
    SELECT * FROM EMP
        WHERE TO_CHAR(HIREDATE, 'YY/MM/DD') >= '82/01/01' AND
            TO_CHAR(HIREDATE, 'YY/MM/DD') <'83/01/01';
    -- EX3. 연봉이 2400 이상 직원의 ENAME, SAL, 연봉(SAL*12)을 출력
    SELECT ENAME, SAL, SAL*12 연봉   -- (3)
        FROM EMP                    -- (1)
            WHERE SAL*12 >= 24000;  -- (2) WHERE 절에는 필드의 별칭 사용 불가
    -- EX4. 연봉이 3000 이상 직원의 ENAME, SAL, 연봉을 연봉순으로 출력
    SELECT ENAME, SAL, SAL*12 연봉   -- (3)
        FROM EMP                    --(1)
        WHERE SAL*12>=30000         --(2)
        ORDER BY 연봉;               --(4)
    -- EX5. JOB이 MANAGER이거나 10번 부서(DEPTNO)외의 직원의 모든 필드
    SELECT * FROM EMP WHERE JOB='MANAGER' OR DEPTNO!=10;
            
-- 5. 산술연산자(SELECT절, 조건절, ORDER BY절)
    -- 모든 사원의 10% 인상된 월급과 사번(EMPNO), 이름(ENAME)을 출력
    SELECT EMPNO, ENAME, SAL*1.1 FROM EMP;
    -- 모든 사원의 이름(ENAME), 월급(SAL), 상여(COMM), 연봉(SAL*12+COMM)을 출력
    SELECT ENAME, SAL, COMM, SAL*12+COMM 연봉 FROM EMP;
    -- 산술연산의 NULL을 포함하면 결과도 NULL
    -- NVL(NULL일 수도 있는 필드명, NULL을 대체할 값)을 이용
    SELECT ENAME, SAL, NVL(COMM,0) 상여급, SAL*12+NVL(COMM,0) 연봉 FROM EMP;
    -- 모든 사원의 사번, 이름, 상사사번을 출력,상사의 사번(MGR)이 없는 직원의 MGR을 CEO로 출력
    SELECT EMPNO, ENAME, NVL(TO_CHAR(MGR),'CEO') 상사 FROM EMP;
    
-- 6. 연결연산자(||): 필드값이나 문자를 연결
SELECT ENAME || '은' || JOB EMPLOYEE FROM EMP;

--7. 중복제거(DISTINCT)
SELECT DISTINCT JOB FROM EMP;
SELECT DISTINCT DEPTNO FROM EMP;

--1. emp 테이블의 구조 출력
DESC EMP;

--2. emp 테이블의 모든 내용을 출력 
SELECT * FROM EMP;

--3. 현 scott 계정에서 사용가능한 테이블 출력
SELECT * FROM TAB;

--4. emp 테이블에서 사번, 이름, 급여, 업무, 입사일 출력
SELECT EMPNO, ENAME, SAL, JOB, HIREDATE FROM EMP;

--5. emp 테이블에서 급여가 2000미만인 사람의 사번, 이름, 급여 출력
SELECT EMPNO, ENAME, SAL
    FROM EMP
        WHERE SAL < 2000;

--6. 입사일이 81/02이후에 입사한 사람의 사번, 이름, 업무, 입사일 출력
SELECT EMPNO, ENAME, JOB, HIREDATE 
    FROM EMP
        WHERE HIREDATE >= '81/03/01';

--7. 업무가 SALESMAN인 사람들 모든 자료 출력
SELECT * 
    FROM EMP
        WHERE JOB ='SALESMAN';

--8. 업무가 CLERK이 아닌 사람들 모든 자료 출력
SELECT * 
    FROM EMP
        WHERE JOB !='CLERK';

--9. 급여가 1500이상이고 3000이하인 사람의 사번, 이름, 급여 출력
SELECT EMPNO, ENAME, SAL
    FROM EMP
        WHERE SAL>=1500 AND SAL<=3000;

--10. 부서코드가 10번이거나 30인 사람의 사번, 이름, 업무, 부서코드 출력
SELECT EMPNO, ENAME,JOB,DEPTNO
    FROM EMP
        WHERE DEPTNO = 30 OR DEPTNO = 10;

--11. 업무가 SALESMAN이거나 급여가 3000이상인 사람의 사번, 이름, 업무, 부서코드 출력
SELECT EMPNO, ENAME, JOB, DEPTNO
    FROM EMP
        WHERE JOB='SALESMAN' OR SAL>=3000;

--12. 급여가 2500이상이고 업무가 MANAGER인 사람의 사번, 이름, 업무, 급여 출력
SELECT EMPNO, ENAME, JOB, SAL
    FROM EMP
        WHERE SAL>=2500 AND JOB='MANAGER';
--13.	입사일이81년이고 업무가 'SALESMAN'이 아닌 직원의 사번, 사원명, 입사일, 
-- 업무, 급여를 검색하시오.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL
    FROM EMP
        WHERE HIREDATE>='81-01-01' AND HIREDATE < '82-01-01';

--14.	사번, 사원명, 입사일, 업무, 급여를 급여가 높은 순으로 정렬하고, 
-- 급여가 같으면 입사일이 빠른 사원으로 정렬하시오.
SELECT EMPNO, ENAME, HIREDATE, SAL  
    FROM EMP 
        ORDER BY SAL DESC, HIREDATE ASC;

--15.	사원명의 세 번째 알파벳이 'N'인 사원의 사번, 사원명을 검색하시오
SELECT EMPNO, ENAME
    FROM EMP
        WHERE ENAME LIKE '__N%';

--16.	사원명에 'A'가 들어간 사원의 사번, 사원명을 출력
SELECT EMPNO, ENAME
    FROM EMP
        WHERE ENAME LIKE '%A%';

--17.	연봉(SAL*12)이 35000 이상인 사번, 사원명, 연봉을 검색 하시오.
SELECT EMPNO, ENAME, SAL*12 연봉
    FROM EMP
        WHERE SAL*12>=35000;