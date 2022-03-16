CREATE OR REPLACE PROCEDURE Add_dept(
    no_dept NUMBER,
    name_dept VARCHAR2,
    loc_dept VARCHAR2)
IS
    dept_primaria EXCEPTION;
    PRAGMA exception_init (dept_primaria, -00001);
BEGIN
    INSERT INTO dept VALUES(no_dept, name_dept, loc_dept);
    COMMIT;
EXCEPTION
    WHEN dept_primaria THEN
        dbms_output.put_line('Error: Numero de dept no puede ser nulo ni repetido');
END;