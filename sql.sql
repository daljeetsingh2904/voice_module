show databases;
 create database MLOOPS_MIT;
 use MLOOPS_MIT;
create table MIT_STUD (
stud_id int,
stud_name varchar(25),
domain varchar(25),
age int,
city varchar(25),
fees int );
show tables;
insert into MIT_STUD values
(101, "Sneha", "CS", 19, "Edinburgh", 20000),
(102, "Manreet", "AI", 19, "New jersey", 50000),
(103, "Deepesh", "CS", 22, "Kota", 200000),
(104, "Radhika", "AI", 19, "New York", 10000),
(105, "Rishika", "CS", 17, "Los Angeles", 50000);
select*from MIT_STUD;
select stud_name , city from MIT_STUD;
select*from MIT_STUD where city= "Kota";
select*from MIT_STUD where age = age<22 and age >18;
select*from MIT_STUD order by stud_name;
select*from MIT_STUD where city = "Kota" and age>18;
select*from MIT_STUD where stud_name="Sneha";