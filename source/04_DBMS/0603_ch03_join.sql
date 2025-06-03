--	뉴욕에서 근무하는 사원의 이름과 급여를 출력하시오
select ENAME, SAL  
    from emp, dept 
        where emp.deptno=dept.deptno AND LOC='NEW YORK';

--	ACCOUNTING 부서 소속 사원의 이름과 입사일을 출력하시오
SELECT ENAME, HIREDATE
    FROM EMP E, DEPT D
        WHERE E.DEPTNO = D.DEPTNO AND DNAME = 'ACCOUNTING';
--	직급이 MANAGER인 사원의 이름, 부서명을 출력하시오
SELECT ENAME, DNAME
    FROM EMP E, DEPT D
        WHERE E.DEPTNO = D.DEPTNO AND JOB='MANAGER';
--	Comm이 null이 아닌 사원의 이름, 급여, 부서코드, 근무지를 출력하시오.
SELECT ENAME,SAL,E.DEPTNO,LOC 
    FROM EMP E, DEPT D
        WHERE E.DEPTNO = D.DEPTNO AND COMM IS NOT NULL;
        
-- 4. NON-EQUI JOIN
SELECT * FROM EMP WHERE ENAME='SCOTT'; -- 직원정보
SELECT * FROM SALGRADE;
SELECT * FROM EMP, SALGRADE
    WHERE ENAME='SCOTT' AND SAL BETWEEN LOSAL AND HISAL;
    -- EX. 모든 사원의 사번, 이름 ,JOB, 상사사번, 급여, 급여등급(1등급, 2등급,..)
    SELECT EMPNO, ENAME, JOB, MGR, SAL, GRADE||'등급' GRADE
        FROM EMP, SALGRADE
            WHERE SAL BETWEEN LOSAL AND HISAL;
    -- EX. 모든 사원의 사번, 이름 ,JOB, 상사사번, 급여, 급여등급(1등급, 2등급,..), 부서명
    SELECT EMPNO, ENAME, JOB, MGR, SAL, GRADE||'등급' GRADE, DNAME
        FROM EMP, SALGRADE, DEPT D
            WHERE SAL BETWEEN LOSAL AND HISAL;
    
    --	Comm이 null이 아닌 사원의 이름, 급여, 등급, 부서번호, 부서이름, 근무지를 출력하시오.
    SELECT ENAME, SAL,GRADE, E.DEPTNO, D.DNAME, LOC
        FROM EMP E, DEPT D, SALGRADE
            WHERE COMM IS NOT NULL AND SAL BETWEEN LOSAL AND HISAL AND E.DEPTNO = D.DEPTNO ;
    --	이름, 급여, 급여등급, 연봉, 부서명을 부서명순으로 정렬하여 출력. 부서가 같으면 연봉순. 연봉=(sal+comm)*12 comm이 null이면 0
    SELECT ENAME, SAL, GRADE, SAL*12+NVL(COMM,0) 연봉, DNAME
        FROM EMP E, DEPT D, SALGRADE
            WHERE SAL BETWEEN LOSAL AND HISAL AND E.DEPTNO = D.DEPTNO
                ORDER BY DNAME, 연봉 DESC;
    --	이름, 업무, 급여, 등급, 부서코드, 부서명 출력. 급여가 1000~3000사이. 정렬조건 : 부서별, 부서같으면 업무별, 업무같으면 급여 큰순
    SELECT ENAME, JOB, SAL, GRADE, E.DEPTNO, DNAME
        FROM EMP E, DEPT D, SALGRADE  
            WHERE SAL BETWEEN 1000 AND 3000 AND SAL BETWEEN LOSAL AND HISAL AND E.DEPTNO = D.DEPTNO 
            ORDER BY DNAME, JOB, SAL DESC;
    --	이름, 급여, 등급, 입사일, 근무지. 81년에 입사한 사람. 등급 큰순
    SELECT ENAME, SAL, GRADE, HIREDATE, LOC
        FROM EMP E, DEPT D, SALGRADE
            WHERE SAL BETWEEN LOSAL AND HISAL AND E.DEPTNO = D.DEPTNO AND TO_CHAR(HIREDATE,'YY')= 81
                ORDER BY GRADE DESC;
    
-- 연습문제 PART1
    
--1. 모든 사원에 대한 이름, 부서번호, 부서명을 출력하는 SELECT 문장을 작성하여라.
SELECT ENAME, D.DEPTNO, DNAME
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO;
--2. NEW YORK에서 근무하고 있는 사원에 대하여 이름, 업무, 급여, 부서명을 출력
SELECT ENAME,JOB,SAL, DNAME
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND LOC='NEW YORK';
--3. 보너스를 받는 사원에 대하여 이름,부서명,위치를 출력
SELECT ENAME, DNAME, LOC
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND COMM IS NOT NULL;
--4. 이름 중 L자가 있는 사원에 대하여 이름,업무,부서명,위치를 출력
SELECT ENAME,JOB, DNAME, LOC
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND ENAME LIKE '%L%';
--5. 사번, 사원명, 부서코드, 부서명을 검색하라(단, 사원명기준으로 오름차순 정렬)
SELECT EMPNO,ENAME,D.DEPTNO, DNAME
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO
    ORDER BY ENAME;
--6. 사번, 사원명, 급여, 부서명을 검색하라. 
    --단 급여가 2000이상인 사원에 대하여 급여를 기준으로 내림차순으로 정렬하시오
SELECT EMPNO, ENAME,SAL, DNAME
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND SAL>=2000
    ORDER BY SAL DESC;
--7. 사번, 사원명, 업무, 급여, 부서명을 검색하시오. 단 업무가 MANAGER이며 급여가 2500이상인
-- 사원에 대하여 사번을 기준으로 오름차순으로 정렬하시오.
SELECT EMPNO,ENAME,JOB,SAL, DNAME
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND JOB='MANAGER' AND SAL>=2500
    ORDER BY EMPNO ;
--8. 사번, 사원명, 업무, 급여, 등급을 검색하시오(단, 급여기준 내림차순으로 정렬)
SELECT EMPNO, ENAME,JOB,SAL,GRADE
    FROM EMP , SALGRADE
    WHERE SAL BETWEEN LOSAL AND HISAL
    ORDER BY SAL DESC;
    
-- 3. SELF JOIN
SELECT * FROM EMP WHERE ENAME = 'SMITH';
SELECT WORKER.EMPNO, WORKER.ENAME, WORKER.MGR, MANAGER.EMPNO 상관번호, MANAGER.ENAME 상관이름
    FROM EMP WORKER, EMP MANAGER 
    WHERE WORKER.MGR=MANAGER.EMPNO AND WORKER.ENAME='SMITH';
    -- EX. 모든 사원의 사번, 이름, 상사의 사번, 상사이름
    SELECT W.EMPNO, W.ENAME, W.MGR, M.ENAME 상사이름
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO;
    -- EX. 'SMITH의 상사는 JONES이다.'포맷으로 출력
    SELECT W.ENAME ||'의 상사는' || M.ENAME || '이다' MESSAGE
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO;
    -- 탄탄1 : 매니저가 KING인 사원들의 이름과 직급을 출력하시오.
    SELECT W.ENAME, W.JOB
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO AND M.ENAME = 'KING';
    
    SELECT ENAME, JOB
        FROM EMP
        WHERE MGR = (SELECT EMPNO FROM EMP WHERE ENAME='KING');
    -- 탄탄2 : SCOTT과 동일한 부서번호에서 근무하는 사원의 이름을 출력하시오
    SELECT W.ENAME
        FROM EMP W, EMP SCOTT
        WHERE W.DEPTNO=SCOTT.DEPTNO AND SCOTT.ENAME = 'SCOTT' AND W.ENAME!='SCOTT';
        
    SELECT ENAME
        FROM EMP    
        WHERE DEPTNO=(SELECT DEPTNO FROM EMP WHERE ENAME='SCOTT')AND ENAME!='SCOTT';
-- 4. OUTER JOIN
-- 배제된 행을 결과에 포함시킬 경우 +기호를 정보가 부족한 컬럼이름 뒤에 덧붙인다.
    SELECT W.EMPNO, W.ENAME,W.MGR, M.EMPNO, M.ENAME
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+);
        -- EX. 모든 사원에 대해 'SMITH의 상사는 FORD다'... 'KING의 상사는 다'
        SELECT W.ENAME || '의 상사는 ' || NVL(M.ENAME,'없') || '다' MESSAGE
            FROM EMP W, EMP M
            WHERE W.MGR = M.EMPNO(+);
        -- 말단 직원
        SELECT W.ENAME, M.ENAME
        FROM EMP W, EMP M
            WHERE W.MGR(+) = M.EMPNO AND W.ENAME IS NULL;
            
-- (2) EQUI JOIN에서의 OUTER JOIN
SELECT * FROM DEPT; -- 10,20,30,40
SELECT * FROM EMP; -- 10,20,30 
SELECT ENAME, E.DEPTNO, DNAME
    FROM EMP E, DEPT D
    WHERE E.DEPTNO(+)=D.DEPTNO;
    
--1. 이름, 직속상사명
SELECT W.ENAME,M.ENAME 직속상사
    FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO;
--2. 이름, 급여, 업무, 직속상사명
SELECT W.ENAME,W.SAL,W.JOB,M.ENAME 직속상사
    FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO;
--3. 이름, 급여, 업무, 직속상사명 . (상사가 없는 직원까지 전체 직원 다 출력.
    --상사가 없을 시 '없음'으로 출력)
SELECT W.ENAME,W.SAL,W.JOB,NVL(M.ENAME,'없음') 직속상사
    FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+);
--4. 이름, 급여, 부서명, 직속상사명
SELECT W.ENAME,W.SAL,DNAME,M.ENAME 직속상사
    FROM EMP W, EMP M, DEPT D
        WHERE W.MGR = M.EMPNO AND W.DEPTNO=D.DEPTNO;
--5. 상사가 없는 직원과 상사가 있는 직원 모두에 대해 이름, 급여, 부서코드, 부서명, 근무지, 직속상사명을 출력하시오(단, 직속상사가 없을 경우 직속상사명에는 ‘없음’으로 대신 출력하시오)
SELECT W.ENAME,W.SAL,W.DEPTNO,DNAME,LOC,NVL(M.ENAME,'없음') 직속상사
    FROM EMP W, EMP M, DEPT D
        WHERE W.MGR = M.EMPNO(+) AND W.DEPTNO=D.DEPTNO;
--6. 이름, 급여, 등급, 부서명, 직속상사명. 급여가 2000이상인 사람
SELECT W.ENAME,W.SAL,GRADE,DNAME,M.ENAME 직속상사
    FROM EMP W, EMP M, DEPT D, SALGRADE
        WHERE W.MGR = M.EMPNO AND W.DEPTNO=D.DEPTNO AND W.SAL BETWEEN LOSAL AND HISAL;
--7. 이름, 급여, 등급, 부서명, 직속상사명, (직속상사가 없는 직원까지 전체직원 부서명 순 정렬)
SELECT W.ENAME,W.SAL,GRADE,DNAME,M.ENAME 직속상사
    FROM EMP W, EMP M, DEPT D, SALGRADE
        WHERE W.MGR = M.EMPNO(+) AND W.DEPTNO=D.DEPTNO AND W.SAL BETWEEN LOSAL AND HISAL
        ORDER BY DNAME;
--8. 이름, 급여, 등급, 부서명, 연봉, 직속상사명. 연봉=(급여+comm)*12으로 계산
SELECT W.ENAME,W.SAL,W.SAL*12 + NVL(W.COMM,0) 연봉,DNAME,M.ENAME 직속상사
    FROM EMP W, EMP M, DEPT D, SALGRADE
        WHERE W.MGR = M.EMPNO(+) AND W.DEPTNO=D.DEPTNO AND W.SAL BETWEEN LOSAL AND HISAL;
--9. 8번을 부서명 순 부서가 같으면 급여가 큰 순 정렬
SELECT W.ENAME,W.SAL,W.SAL*12 + NVL(W.COMM,0) 연봉,DNAME,M.ENAME 직속상사
    FROM EMP W, EMP M, DEPT D, SALGRADE
        WHERE W.MGR = M.EMPNO(+) AND W.DEPTNO=D.DEPTNO AND W.SAL BETWEEN LOSAL AND HISAL
        ORDER BY DNAME, W.SAL DESC;
--10. 사원테이블에서 사원명, 사원의 상사를 검색하시오(상사가 없는 직원까지 전체).
SELECT W.ENAME,M.ENAME 직속상사
    FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+);
--11. 사원명, 상사명, 상사의 상사명을 검색하시오(self join)
SELECT W.ENAME,M.ENAME 직속상사, MM.ENAME 상사의상사
    FROM EMP W, EMP M, EMP MM
        WHERE W.MGR = M.EMPNO(+) AND M.MGR = MM.EMPNO ;
--12. 위의 결과에서 상위 상사가 없는 모든 직원의 이름도 출력되도록 수정하시오(outer join)
SELECT W.ENAME,M.ENAME 직속상사, MM.ENAME 상사의상사
    FROM EMP W, EMP M, EMP MM
        WHERE W.MGR = M.EMPNO(+) AND M.MGR = MM.EMPNO(+) ;