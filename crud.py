from datetime import datetime

def error(err):
    print('error')

def getEmpDepto(conn, empId):
    try:
        cur = conn.cursor()
    except Exception as err: error(err)

    else:
        return cur.callfunc('NOEMP_DEPTO', int, [empId])

    finally:
        cur.close()

def createEmp(conn, no_emp, name_emp, job_emp, mgr_emp, hiredate_emp, sal_emp,
comm_emp, deptno_emp):
    try:
        cur = conn.cursor()
    except Exception as err: error(err)

    else:
        data = [no_emp, name_emp, job_emp, mgr_emp, hiredate_emp, sal_emp, comm_emp, deptno_emp]
        return cur.callproc('ADD_EMP', data)

    finally:
        cur.close()

def updateEmp(conn, no_emp, name_emp, job_emp, mgr_emp, hiredate_emp, sal_emp,
comm_emp, deptno_emp):
    try:
        cur = conn.cursor()
    except Exception as err: error(err)

    else:
        data = [no_emp, name_emp, job_emp, mgr_emp, hiredate_emp, sal_emp, comm_emp, deptno_emp]
        return cur.callproc('UPDATE_EMP', data)

    finally:
        cur.close()

def deleteEmp(conn, empId):
    try:
        cur = conn.cursor()
    except Exception as err: error(err)

    else:
        return cur.callproc('DELETE_EMP', [empId])

    finally:
        cur.close()

def createDepto(conn, no_dept, name_dept, loc_dept):
    try:
        cur = conn.cursor()
    except Exception as err: error(err)

    else:
        return cur.callproc('ADD_DEPT', [no_dept, name_dept, loc_dept])

    finally:
        cur.close()

def updateDepto(conn, no_dept, name_dept, loc_dept):
    try:
        cur = conn.cursor()
    except Exception as err: error(err)

    else:
        return cur.callproc('UPDATE_DEPT', [no_dept, name_dept, loc_dept])

    finally:
        cur.close()

def deleteDepto(conn, no_dept):
    try:
        cur = conn.cursor()
    except Exception as err: error(err)

    else:
        return cur.callproc('DELETE_DEPTNO', [no_dept])

    finally:
        cur.close()
