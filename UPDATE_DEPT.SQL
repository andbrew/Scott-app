CREATE OR REPLACE PROCEDURE update_dept (deptnonew dept.deptno%TYPE,
                                     dnamenew dept.dname%TYPE, locnew dept.loc%TYPE)
IS
BEGIN
  UPDATE dept
         SET dname = dnamenew,
         loc = locnew
         WHERE deptno = deptnonew;
         commit;

  IF SQL%ROWCOUNT = 0 THEN
    DBMS_OUTPUT.PUT_LINE('No se ha actualizado nada');
  END IF;
END;
/
