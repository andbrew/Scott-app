import cx_Oracle

user = 'HR'
psswd = 'vanilla'
host = 'localhost:1521'
SID = 'XE'
try:
    conn = cx_Oracle.connect(f'{user}/{psswd}@{host}/{SID}')
except Exception as err: print(err)

else:
    try:
        cur = conn.cursor()
    except Exception as err: print(err)

    else:
        print(cur.callfunc('NOEMP_DEPTO', int, [7900]))

    finally:
        cur.close()

finally:
    conn.close()
