import cx_Oracle, crud, os
from datetime import datetime

user = 'HR'
psswd = 'vanilla'
host = 'localhost:1521'
SID = 'XE'
try:
    conn = cx_Oracle.connect(f'{user}/{psswd}@{host}/{SID}')
except Exception as err: print(err)

else:
    while True:
        os.system('clear')
        print('.: Scott CRUD app :.')

        menu = [['Create', ['Department', 'Employee']],
        ['Read', ['Employee department']],
        ['Update', ['Department', 'Employee']],
        ['Delete', ['Department', 'Employee']]]

        for i in range(len(menu)):
            print(f'{i+1}. {menu[i][0]}', end = '    ')
        op = int(input('\n\n>> '))-1

        for i in range(len(menu[op][1])):
            print(f'{op+1}.{i+1} {menu[op][1][i]}', end = '    ')
        sub_op = int(input(f'\n\n>> {op+1}.'))-1

        command = f'{op+1}.{sub_op+1}'

        if(command == '2.1'):
            empId = int(input('Employee (ID): '))
            print(f'Employee {empId} belongs to department \
{crud.getEmpDepto(conn, empId)}')

        if(command == '1.2'):
            no_emp = int(input('Employee (ID): '))
            name_emp = input('Employee name: ')
            job_emp = input('Employee job: ')
            mgr_emp = int(input('Employee manager (ID): '))
            hiredate_emp = datetime.now()
            sal_emp = int(input('Employee salary: '))
            comm_emp = int(input('Employee commission: '))
            deptno_emp = int(input('Employee department (ID): '))
            crud.createEmp(conn, no_emp, name_emp, job_emp, mgr_emp,
            hiredate_emp, sal_emp, comm_emp, deptno_emp)
            print(f'Employee {no_emp} was succesfully inserted')

        if(command == '3.2'):
            no_emp = int(input('Employee (ID): '))
            name_emp = input('Employee name: ')
            job_emp = input('Employee job: ')
            mgr_emp = int(input('Employee manager (ID): '))
            hiredate_emp = datetime.now()
            sal_emp = int(input('Employee salary: '))
            comm_emp = int(input('Employee commission: '))
            deptno_emp = int(input('Employee department (ID): '))
            crud.updateEmp(conn, no_emp, name_emp, job_emp, mgr_emp,
            hiredate_emp, sal_emp, comm_emp, deptno_emp)
            print(f'Employee {no_emp} was succesfully updated')

        if(command == '4.2'):
            empId = int(input('Employee (ID): '))
            crud.deleteEmp(conn, empId)
            print(f'Employee {empId} was succesfully deleted')

        if(command == '1.1'):
            no_dept = int(input('Department (ID): '))
            name_dept = input('Department name: ')
            loc_dept = input('Department location: ')
            crud.createDepto(conn, no_dept, name_dept, loc_dept)
            print(f'Department {no_dept} was succesfully created')

        if(command == '3.1'):
            no_dept = int(input('Department (ID): '))
            name_dept = input('Department name: ')
            loc_dept = input('Department location: ')
            crud.updateDepto(conn, no_dept, name_dept, loc_dept)
            print(f'Department {no_dept} was succesfully updated')

        if(command == '4.1'):
            no_dept = int(input('Department (ID): '))
            crud.deleteEmp(conn, no_dept)
            print(f'Department {no_dept} was succesfully deleted')

        input()

finally:
    conn.close()
