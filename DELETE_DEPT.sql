CREATE OR REPLACE PROCEDURE Delete_deptno(
    no_dept NUMBER)
IS
    error_dept EXCEPTION;
BEGIN
    DELETE FROM dept
    WHERE deptno = no_dept;
    IF SQL%NOTFOUND THEN
        RAISE error_dept;
    ELSE
        COMMIT;
    END IF;   
EXCEPTION
    WHEN error_dept THEN
        dbms_output.put_line('Error: Dept inexistente');
END;