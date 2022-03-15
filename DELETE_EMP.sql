CREATE OR REPLACE PROCEDURE Delete_emp(
    no_emp NUMBER)
IS
    error_emp EXCEPTION;
BEGIN
    DELETE FROM emp
    WHERE empno = no_emp;
    IF SQL%NOTFOUND THEN
        RAISE error_emp;
    ELSE
        COMMIT;
    END IF;   
EXCEPTION
    WHEN error_emp THEN
        dbms_output.put_line('Error: Empleado Inexistente');
END;
