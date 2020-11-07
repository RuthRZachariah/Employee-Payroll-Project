'''
--------------------------------------------------------------------------------------------------------
                                        COMPUTER SCIENCE PROJECT
--------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------------
                                            PAYROLL MANAGEMENT
--------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------------
                                                    BY:
                                          RUTH RACHEL ZACHARIAH
                                                    &
                                            HRIDHYA SUDEEPTHI

                                                CLASS 12-A
--------------------------------------------------------------------------------------------------------
'''                                      

def add_emp_rec():
    
    fw=open('EMPLOYEE.TXT','a')
    n=int(input('Number of Records to add?'))

    for x in range(n):
            eno=int(input('Employee Number?[4 didgits]'))
            ename=input('Name?')
            sex=input('Sex?[M/F]')
            dob=input('Date Of Birth? [DD/MM/YYYY]')
            doj=input('Date Of Joining? [DD/MM/YYYY]')
            desig=input('Desination?')
            bsal=float(input('Basic Salary?'))
            epho=int(input('Phone Number?[8 Characters]'))
            emob=int(input('Mobile Number?[8 Characters]'))
            email=input('E-mail Address?')
            ename=ename.upper()
            sex=sex.upper()
            desig=desig.upper()
            
            data=str(eno)+','+ename+','+sex+','+dob+','+doj+','+desig+','+str(bsal)+','+str(epho)+','+str(emob)+','+email+'\n'        
            fw.write(data)
            
    fw.close()

from os import remove, rename
    
def edit_emp_rec():
    
    no=int(input('Employee Number to edit?'))
    fr=open('EMPLOYEE.TXT')
    fw=open('EMPLOYEE.TEMP','w')
    found=0   

    for data in fr:
        data=data.strip()
        arr=data.split(',')
        
        if no==int(arr[0]):
            while True:
                print('EMPLOYEE DETAILS FIELDS:')
                print('1.Date of Birth')
                print('2.Date of Joining')
                print('3.Designation')
                print('4.Basic Salary')
                print('5.Phone Number')
                print('6.Mobile Number')
                print('7.Email Address')
                print('0.Exit')

                ch=input('Field to edit?')
                if ch=='1':
                    arr[3]=input('Date of Birth?')
                    
                elif ch=='2':
                        arr[4]=input('Date of Joining?')
                    
                elif ch=='3':
                        arr[5]=input('Designation?')
                    
                elif ch=='4':
                        arr[6]=float(input('Basic Salary?'))
                
                elif ch=='5':
                        arr[7]=int(input('Phone Number? [10 Characters]'))
                    
                elif ch=='6':
                        arr[8]=int(input('Mobile Number?'))
                    
                elif ch=='7':
                        arr[9]=input('E-mail?')

                elif ch=='0':
                        break
                    
            found=1                            
        data=str(arr[0])+','+str(arr[1])+','+str(arr[2])+','+str(arr[3])+','+str(arr[4])+','+str(arr[5].upper())+','+str(arr[6])+','+str(arr[7])+','+str(arr[8])+','+str(arr[9])+'\n'
        fw.write(data)
        
    fr.close()
    fw.close()

    if found==1:
        print('Employee Details Updated')
    else:
        print(no,'Not found in the file')
        
    remove('EMPLOYEE.TXT')
    rename('EMPLOYEE.TEMP','EMPLOYEE.TXT')
            

def search_emp_name():
    
    na=input('Name to search?')
    found=0
    fr=open('EMPLOYEE.TXT')
    
    for data in fr:
        data=data.strip()
        arr=data.split(',')
        
        if arr[1]==na.upper():
            print(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9])
            found=1
            
    fr.close()

    if found==0:
        print(na,': Not found in the file')
        

def search_emp_number():
    
    no=int(input('Employee Number to search?'))
    found=0
    fr=open('EMPLOYEE.TXT')
    
    for line in fr:
        data=line.strip()
        arr=data.split(',')
        
        if int(arr[0])==no:
            print(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9])
            found=1
            
    fr.close()
    
    if found==0:
        print(no,': Not found in the file')
        

def calc_emp_sal():
    
    fin=open('EMPLOYEEPAY.TXT','a')
    n=int(input('No. of Records?'))
    
    for x in range(n):
        nu=int(input('Employee Number?[4 digits]'))
        na=input('Employee Name?')
        nod=int(input('No. of Days worked?'))
        bsal=float(input('Monthly Basic Salary?[8 digits(MAX)]'))
        da=0.55*bsal
        hra=0.35*bsal
        con=0.15*bsal
        gro=bsal+da+hra+con
        itx=0.04*bsal
        loan=0.1*bsal
        salad=0.25*bsal
        ded=itx+loan+salad
        net=gro-ded
        
        data=str(nu)+','+na.upper()+','+str(nod)+','+str(bsal)+','+str(da)+','+str(hra)+','+str(con)+','+str(gro)+','+str(itx)+','+str(loan)+','+str(salad)+','+str(ded)+','+str(net)+'\n'
        fin.write(data)
        
    fin.close()


def disp_emp_details():
    
    fin=open('EMPLOYEE.TXT')
    
    print('Displaying employee table')
    print('------------------------------------------------------------------------------------------------------')
    print('%-4s %-10s %-3s %-10s %-10s %-12s %-8s %-8s %-8s %-15s'%('ENo','EmpName','Sex','DOB','DOJ','Designation','BSal','EmpPhone','EmpMobile','Email'))
    print('------------------------------------------------------------------------------------------------------')

    for line in fin:
        
        data=line.strip()
        arr=data.split(',')
        print('%-4s %-10s %-3s %-10s %-10s %-12s %-8s %-8s %-8s %-15s'%(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9]))
        print('------------------------------------------------------------------------------------------------------')
        
    fin.close()
    
    
def emp_sal_statement():
    
    x=['January','February','March','April','May','June','July','August','September','October','November','December']
    mo=int(input('Month?(in the form of an integer)'))
    ye=int(input('Year?'))
    print('Salary statement for month of', x[mo-1],ye)
    
    print('---------------------------------------------------------------------------------------')
    print('%-6s %-20s %-15s %-8s %-8s %-15s %-5s'%('ENo','Name','Designation','Basic','Gross','Deductions','Net'))
    print('---------------------------------------------------------------------------------------')

    fout=open('EMPLOYEE.TXT')
    fin=open('EMPLOYEEPAY.TXT')
    
    for line in fin:
        data=line.strip()
        arr=data.split(',')
    for z in fout:
        rec=z.strip()
        recs=rec.split(',')
        
        print('%-6s %-20s %-15s %-8s %-8s %-15s %-5s'%(recs[0],recs[1],recs[5],arr[3],arr[7],arr[11],arr[12]))
        print('---------------------------------------------------------------------------------------')
   
    fin.close()        
    fout.close()
    
    
def emp_sal_slip():
    
    x=['January','February','March','April','May','June','July','August','September','October','November','December']
    mo=int(input('Month?(in the form of an integer)'))
    ye=int(input('Year?'))
    
    if mo>=1 and mo<=12:
        print('Salary slip for month of', x[mo-1],ye)
    else:
        print('Month Exceeding Limit')
        x=['January','February','March','April','May','June','July','August','September','October','November','December']
        mo=int(input('Month?(in the form of an integer)'))
        ye=int(input('Year?'))
            
    fin=open('EMPLOYEEPAY.TXT')
    nu=int(input('Employee Number?'))
    
    for line in fin:
        data=line.strip()
        arr=data.split(',')
        
        if nu==int(arr[0]):
            print('-------------------------------------------------------------------------------------------------')
            print('Employee Number=',nu,'\t\t\t\t\t','Employee Name=',arr[1])
            print('-------------------------------------------------------------------------------------------------')
            print('Basic'+'\t\t'+'='+'\t\t'+arr[3]+'\t\t\t'+'Deductions'+'\t'+'='+'\t'+arr[11])
            print('DA'+'\t\t'+'='+'\t\t'+arr[4])
            print('HRA'+'\t\t'+'='+'\t\t'+arr[5])
            print('Conveyance'+'\t'+'='+'\t\t'+arr[6])
            print('-------------------------------------------------------------------------------------------------') 
            print('Gross Pay=',arr[7],'\t\t\t\t\t','Net=',arr[12])
            print('-------------------------------------------------------------------------------------------------')
        

    fin.close()


def emp_del_eno():    

    fin=open('EMPLOYEE.TXT')    
    fout=open('TEMPORARY.TXT','a')    
    eno=int(input('Employee no. to be deleted='))    
    found=0    

    for data in fin:        
        arr=data.split(',')        
        if int(arr[0])==eno:            
            found=1        
        else:            
            fout.write(data)    

    fout.close()    
    fin.close()    

    if found==0:        
        print(eno,'not found in the file')    
    else:        
        print(eno,'deleted from the file')

    remove('EMPLOYEE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE.TXT')

def emp_del_name():    

    fin=open('EMPLOYEE.TXT')    
    fout=open('TEMPORARY.TXT','a')    
    na=input('Employee name to be deleted=')    
    found=0    

    for data in fin:        
        arr=data.split(',')        
        if arr[1]==na.upper():            
            found=1        
        else:            
            fout.write(data)    

    fout.close()    
    fin.close()    

    if found==0:        
        print(na,'not found in the file')    
    else:        
        print(na,'deleted from the file')
        
    remove('EMPLOYEE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE.TXT')

'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                        MAIN PROGRAMME
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

while True:
    print('PAYROLL MANAGEMENT')
    print('TASK MENU: ')
    print('1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"')
    print('2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"')
    print('3.SEARCH FOR EMPLOYEE USING NAME')
    print('4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER')
    print('5.ADD RECORD TO "MONTHLY PAY FILE"')
    print('6.DISPLAY EMPLOYEE DETAILS')
    print('7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH')
    print('8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE')
    print('9.SHOW DELETION MENU')
    print('0.EXIT')

    ch=input('SELECT OPERATION TO PERFORM : ')
    if ch=='1':
        add_emp_rec()
                    
    elif ch=='2':
        edit_emp_rec()
                    
    elif ch=='3':
        search_emp_name()
                        
    elif ch=='4':
        search_emp_number()
                            
    elif ch=='5':
        calc_emp_sal()

    elif ch=='6':
        disp_emp_details()
                                    
    elif ch=='7':
        emp_sal_statement()
                        
    elif ch=='8':
        emp_sal_slip()

    elif ch=='9':
        while True:    
            print('DELETION MENU')    
            print('1. DELETE USING EMPLOYEE NUMBER')    
            print('2. DELETE USING EMPLOYEE NAME')    
            print('0. EXIT DELETION MENU')    
            ch=input('SELECT OPERATION TO PERFORM :')    
            if ch=='1': 
                emp_del_eno()    

            elif ch=='2':
                emp_del_name()    

            elif ch=='0': 
                    break      
        
                        
    elif ch=='0':
            break





#SAMPLE INPUT AND OUTPUT

'''
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 1
Number of Records to add?10
Employee Number?[4 didgits]1001
Name?ahmed
Sex?[M/F]m
Date Of Birth? [DD/MM/YYYY]12/09/2002
Date Of Joining? [DD/MM/YYYY]12/07/2019
Desination?manager
Basic Salary?30000
Phone Number?[8 Characters]27382974
Mobile Number?[8 Characters]28738718
E-mail Address?ahmdkhn@gmail.com
Employee Number?[4 didgits]1002
Name?mishal
Sex?[M/F]m
Date Of Birth? [DD/MM/YYYY]17/03/1998
Date Of Joining? [DD/MM/YYYY]03/05/2012
Desination?consultant
Basic Salary?50000
Phone Number?[8 Characters]27637627
Mobile Number?[8 Characters]98726354
E-mail Address?mishmash@hotmail.com
Employee Number?[4 didgits]1003
Name?rupi
Sex?[M/F]f
Date Of Birth? [DD/MM/YYYY]05/03/1999
Date Of Joining? [DD/MM/YYYY]07/09/2019
Desination?typist
Basic Salary?20000
Phone Number?[8 Characters]27837665
Mobile Number?[8 Characters]998267352
E-mail Address?me_rupi@gmail.com
Employee Number?[4 didgits]1004
Name?chanda
Sex?[M/F]f
Date Of Birth? [DD/MM/YYYY]03/09/1995
Date Of Joining? [DD/MM/YYYY]19/06/2016
Desination?designer
Basic Salary?40000
Phone Number?[8 Characters]78736526
Mobile Number?[8 Characters]99826418
E-mail Address?chands@yahoo.com
Employee Number?[4 didgits]1005
Name?balu
Sex?[M/F]m
Date Of Birth? [DD/MM/YYYY]13/12/1996
Date Of Joining? [DD/MM/YYYY]14/09/2012
Desination?manager
Basic Salary?60000
Phone Number?[8 Characters]62837463
Mobile Number?[8 Characters]92836473
E-mail Address?baluuu@gmail.com
Employee Number?[4 didgits]1006
Name?tara
Sex?[M/F]f
Date Of Birth? [DD/MM/YYYY]05/06/1998
Date Of Joining? [DD/MM/YYYY]09/06/2013
Desination?editor
Basic Salary?70000
Phone Number?[8 Characters]27381736
Mobile Number?[8 Characters]62731653
E-mail Address?ttaarraa@gmail.com
Employee Number?[4 didgits]1007
Name?keshav
Sex?[M/F]m
Date Of Birth? [DD/MM/YYYY]16/08/1996
Date Of Joining? [DD/MM/YYYY]12/05/2018
Desination?consultant
Basic Salary?20000
Phone Number?[8 Characters]18374612
Mobile Number?[8 Characters]01928734
E-mail Address?k_shav@gmail.com
Employee Number?[4 didgits]1008
Name?upali
Sex?[M/F]f
Date Of Birth? [DD/MM/YYYY]15/02/1995
Date Of Joining? [DD/MM/YYYY]12/06/2016
Desination?typist
Basic Salary?30000
Phone Number?[8 Characters]17287283
Mobile Number?[8 Characters]81123745
E-mail Address?upli@hotmail.com
Employee Number?[4 didgits]1009
Name?jayant
Sex?[M/F]m
Date Of Birth? [DD/MM/YYYY]12/09/2002
Date Of Joining? [DD/MM/YYYY]10/03/2019
Desination?secretary
Basic Salary?10000
Phone Number?[8 Characters]17838765
Mobile Number?[8 Characters]93876152
E-mail Address?j_ant@gmail.com
Employee Number?[4 didgits]1010
Name?gertude
Sex?[M/F]f
Date Of Birth? [DD/MM/YYYY]12/09/2002
Date Of Joining? [DD/MM/YYYY]13/09/2019
Desination?editor
Basic Salary?40000
Phone Number?[8 Characters]27651253
Mobile Number?[8 Characters]99812352
E-mail Address?gertude_me@gmail.com
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 2
Employee Number to edit?1004
EMPLOYEE DETAILS FIELDS:
1.Date of Birth
2.Date of Joining
3.Designation
4.Basic Salary
5.Phone Number
6.Mobile Number
7.Email Address
0.Exit
Field to edit?1
Date of Birth?12/04/1995
EMPLOYEE DETAILS FIELDS:
1.Date of Birth
2.Date of Joining
3.Designation
4.Basic Salary
5.Phone Number
6.Mobile Number
7.Email Address
0.Exit
Field to edit?2
Date of Joining?13/09/2018
EMPLOYEE DETAILS FIELDS:
1.Date of Birth
2.Date of Joining
3.Designation
4.Basic Salary
5.Phone Number
6.Mobile Number
7.Email Address
0.Exit
Field to edit?0
Employee Details Updated
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 3
Name to search?tara
1006 TARA F 05/06/1998 09/06/2013 EDITOR 70000.0 27381736 62731653 ttaarraa@gmail.com
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 3
Name to search?ruth
ruth : Not found in the file
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 4
Employee Number to search?1006
1006 TARA F 05/06/1998 09/06/2013 EDITOR 70000.0 27381736 62731653 ttaarraa@gmail.com
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 4
Employee Number to search?1012
1012 : Not found in the file
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 5
No. of Records?10
Employee Number?[4 digits]1001
Employee Name?ahmed
No. of Days worked?15
Monthly Basic Salary?[8 digits(MAX)]30000
Employee Number?[4 digits]1002
Employee Name?mishal
No. of Days worked?19
Monthly Basic Salary?[8 digits(MAX)]50000
Employee Number?[4 digits]1003
Employee Name?rupi
No. of Days worked?20
Monthly Basic Salary?[8 digits(MAX)]20000
Employee Number?[4 digits]1004
Employee Name?chanda
No. of Days worked?17
Monthly Basic Salary?[8 digits(MAX)]40000
Employee Number?[4 digits]1005
Employee Name?balu
No. of Days worked?23
Monthly Basic Salary?[8 digits(MAX)]60000
Employee Number?[4 digits]1006
Employee Name?tara
No. of Days worked?26
Monthly Basic Salary?[8 digits(MAX)]70000
Employee Number?[4 digits]1007
Employee Name?keshav
No. of Days worked?20000
Monthly Basic Salary?[8 digits(MAX)]20000
Employee Number?[4 digits]1008
Employee Name?upali
No. of Days worked?21
Monthly Basic Salary?[8 digits(MAX)]30000
Employee Number?[4 digits]1009
Employee Name?jayant
No. of Days worked?23
Monthly Basic Salary?[8 digits(MAX)]10000
Employee Number?[4 digits]1010
Employee Name?gertude
No. of Days worked?24
Monthly Basic Salary?[8 digits(MAX)]40000
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 6
Displaying employee table
------------------------------------------------------------------------------------------------------
ENo  EmpName    Sex DOB        DOJ        Designation  BSal     EmpPhone EmpMobile Email          
------------------------------------------------------------------------------------------------------
1001 AHMED      M   12/09/2002 12/07/2019 MANAGER      30000.0  27382974 28738718 ahmdkhn@gmail.com
------------------------------------------------------------------------------------------------------
1002 MISHAL     M   17/03/1998 03/05/2012 CONSULTANT   50000.0  27637627 98726354 mishmash@hotmail.com
------------------------------------------------------------------------------------------------------
1003 RUPI       F   05/03/1999 07/09/2019 TYPIST       20000.0  27837665 998267352 me_rupi@gmail.com
------------------------------------------------------------------------------------------------------
1004 CHANDA     F   12/04/1995 13/09/2018 DESIGNER     40000.0  78736526 99826418 chands@yahoo.com
------------------------------------------------------------------------------------------------------
1005 BALU       M   13/12/1996 14/09/2012 MANAGER      60000.0  62837463 92836473 baluuu@gmail.com
------------------------------------------------------------------------------------------------------
1006 TARA       F   05/06/1998 09/06/2013 EDITOR       70000.0  27381736 62731653 ttaarraa@gmail.com
------------------------------------------------------------------------------------------------------
1007 KESHAV     M   16/08/1996 12/05/2018 CONSULTANT   20000.0  18374612 1928734  k_shav@gmail.com
------------------------------------------------------------------------------------------------------
1008 UPALI      F   15/02/1995 12/06/2016 TYPIST       30000.0  17287283 81123745 upli@hotmail.com
------------------------------------------------------------------------------------------------------
1009 JAYANT     M   12/09/2002 10/03/2019 SECRETARY    10000.0  17838765 93876152 j_ant@gmail.com
------------------------------------------------------------------------------------------------------
1010 GERTUDE    F   12/09/2002 13/09/2019 EDITOR       40000.0  27651253 99812352 gertude_me@gmail.com
------------------------------------------------------------------------------------------------------
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 7
Month?(in the form of an integer)03
Year?2018
Salary statement for month of March 2018
---------------------------------------------------------------------------------------
ENo    Name                 Designation     Basic    Gross    Deductions      Net  
---------------------------------------------------------------------------------------
1001   AHMED                MANAGER         40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
1002   MISHAL               CONSULTANT      40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
1003   RUPI                 TYPIST          40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
1004   CHANDA               DESIGNER        40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
1005   BALU                 MANAGER         40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
1006   TARA                 EDITOR          40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
1007   KESHAV               CONSULTANT      40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
1008   UPALI                TYPIST          40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
1009   JAYANT               SECRETARY       40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
1010   GERTUDE              EDITOR          40000.0  82000.0  15600.0         66400.0
---------------------------------------------------------------------------------------
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 8
Month?(in the form of an integer)11
Year?2012
Salary slip for month of November 2012
Employee Number?1003
-------------------------------------------------------------------------------------------------
Employee Number= 1003 					 Employee Name= RUPI
-------------------------------------------------------------------------------------------------
Basic		=		20000.0			Deductions	=	7800.0
DA		=		11000.0
HRA		=		7000.0
Conveyance	=		3000.0
-------------------------------------------------------------------------------------------------
Gross Pay= 41000.0 					 Net= 33200.0
-------------------------------------------------------------------------------------------------
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 9
DELETION MENU
1. DELETE USING EMPLOYEE NUMBER
2. DELETE USING EMPLOYEE NAME
0. EXIT DELETION MENU
SELECT OPERATION TO PERFORM :1
Employee no. to be deleted=1002
1002 deleted from the file
DELETION MENU
1. DELETE USING EMPLOYEE NUMBER
2. DELETE USING EMPLOYEE NAME
0. EXIT DELETION MENU
SELECT OPERATION TO PERFORM :2
Employee name to be deleted=upali
upali deleted from the file
DELETION MENU
1. DELETE USING EMPLOYEE NUMBER
2. DELETE USING EMPLOYEE NAME
0. EXIT DELETION MENU
SELECT OPERATION TO PERFORM :0
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 6
Displaying employee table
------------------------------------------------------------------------------------------------------
ENo  EmpName    Sex DOB        DOJ        Designation  BSal     EmpPhone EmpMobile Email          
------------------------------------------------------------------------------------------------------
1001 AHMED      M   12/09/2002 12/07/2019 MANAGER      30000.0  27382974 28738718 ahmdkhn@gmail.com
------------------------------------------------------------------------------------------------------
1003 RUPI       F   05/03/1999 07/09/2019 TYPIST       20000.0  27837665 998267352 me_rupi@gmail.com
------------------------------------------------------------------------------------------------------
1004 CHANDA     F   12/04/1995 13/09/2018 DESIGNER     40000.0  78736526 99826418 chands@yahoo.com
------------------------------------------------------------------------------------------------------
1005 BALU       M   13/12/1996 14/09/2012 MANAGER      60000.0  62837463 92836473 baluuu@gmail.com
------------------------------------------------------------------------------------------------------
1006 TARA       F   05/06/1998 09/06/2013 EDITOR       70000.0  27381736 62731653 ttaarraa@gmail.com
------------------------------------------------------------------------------------------------------
1007 KESHAV     M   16/08/1996 12/05/2018 CONSULTANT   20000.0  18374612 1928734  k_shav@gmail.com
------------------------------------------------------------------------------------------------------
1009 JAYANT     M   12/09/2002 10/03/2019 SECRETARY    10000.0  17838765 93876152 j_ant@gmail.com
------------------------------------------------------------------------------------------------------
1010 GERTUDE    F   12/09/2002 13/09/2019 EDITOR       40000.0  27651253 99812352 gertude_me@gmail.com
------------------------------------------------------------------------------------------------------
PAYROLL MANAGEMENT
TASK MENU: 
1.ADD EMPLOYEE RECORD TO "EMPLOYEE FILE"
2.EDIT EMPLOYEE RECORD IN "EMPLOYEE FILE"
3.SEARCH FOR EMPLOYEE USING NAME
4.SEARCH FOR EMPLOYEE USING EMPLOYEE NUMBER
5.ADD RECORD TO "MONTHLY PAY FILE"
6.DISPLAY EMPLOYEE DETAILS
7.DISPLAY SALARY STATEMENT FOR A PARTICULAR MONTH
8.DISPLAY SALARY SLIP FOR INDIVIDUAL EMPLOYEE
9.SHOW DELETION MENU
0.EXIT
SELECT OPERATION TO PERFORM : 0
>>>
'''

