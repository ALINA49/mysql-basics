#database
#................
#collection of tables


#banking project
#create database
#rows, cols
#id,name,design,location,salary



#create database
#>mysql queries

#create database databasename;
>create database mycompany:

#query for listing all databases;
>show databases;

#query for using specific database;
>use mycompany;

#query to create a table;
#>create table table_name(column_name type,column_name datatype...);
>create table empployee(eid varchar(23),ename varchar(25),design varchar(25),sal int,exp int, loc varchar(25));

#listing all tables;
>show tables;

#display structure if table;
>desc employee;

#inserting records
#insert into table_name(col1,col2,...)values(val1,val2);
>insert into employee(eid,ename,design,salary,exp,location)values("1000",'ajay','dveloper',25000,2,'ekm');

#fetching all records from tables
>select * from employee;

#fetching names only;
>select ename from employee;

#fetch employe details whose salary>22000?
>select * from employee where salary>22000;

#fetch emp details who work in ekm
>select * from employee where location='ekm';

#delete records from database table
>delete from employee where eid='1000';

#add records
>insert into employee(eid,ename,design,salary,exp,location) values(..............),(.................),(...........);

#agreegate functions()
sum(),avg(),count(),max()

#total sum of employee salary......
>select sum(salary) from employee;

#highest salary
>select max(salary) from employee;

#select name of employee taking highest salary......
>select ename from employee where salary=(select max(salary) from empoyee);

#select 2nd highest salary from employee......
>select max(salary) from employee where salary<>(select max(salary)from employee);

#select name of employee who is taking 2nd highest salary from employee....
>select ename from employee where salary in(select max(salary) from employee where salary<> (select max(salary) from employee));

#dev=3 qa =2 mrk=1
#grouping=
>select design,count(8) from employee group by design;

#display designation name where number of employee <2nd
>select design from employee group by design having count(*) <2;

#display highest salary design wise and name of employee who is taking that sal
>select design,ename,salary from employee group by design having (select max(salary));