CREATE OR REPLACE PROCEDURE Add_emp(
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
    emp_primaria EXCEPTION;
    PRAGMA exception_init (emp_primaria, -00001);
BEGIN
    IF deptno_emp is null 
    THEN
        RAISE emp_foranea;
    END IF;
    INSERT INTO emp VALUES(no_emp, name_emp, job_emp, mgr_emp, hiredate_emp, sal_emp, comm_emp, deptno_emp);
    COMMIT;
EXCEPTION
    WHEN emp_primaria THEN
        dbms_output.put_line('Error: Numero de empleado no puede ser nulo ni repetido');
    WHEN emp_foranea THEN
        dbms_output.put_line('Error: Numero de departamento no puede ser nulo');
END;