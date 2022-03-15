CREATE OR REPLACE PROCEDURE Update_emp(
    no_emp NUMBER,
    name_emp VARCHAR2,
    job_emp VARCHAR2,
    mgr_emp NUMBER,
    hiredate_emp DATE,
    sal_emp NUMBER,
    comm_emp NUMBER,
    deptno_emp NUMBER)
IS
    emp_foranea EXCEPTION;
BEGIN
    IF deptno_emp is null
    THEN
        RAISE emp_foranea;
    END IF;
    UPDATE emp
    SET
      ename = name_emp,
      job = job_emp,
      mgr = mgr_emp,
      hiredate = hiredate_emp,
      sal = sal_emp,
      comm = comm_emp,
      deptno = deptno_emp
    WHERE empno = no_emp;
    COMMIT;
EXCEPTION
    WHEN emp_foranea THEN
        dbms_output.put_line('Error: Numero de departamento no puede ser nulo');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END;
