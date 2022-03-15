import cx_Oracle

user = 'HR'
psswd = 'vanilla'
host = 'localhost:1521'
SID = 'XE'
try:
    conn = cx_Oracle.connect(f'{user}/{psswd}@{host}/{SID}')
except Exception as err: print(err)

print('I am in')
