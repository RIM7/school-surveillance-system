select * from cakemusers;

create database surv_sys;
use surv_sys;

create table surv_sys(
	student_name varchar(100),
    parent_name varchar(100),
    dir_no varchar(5),
    phone_no varchar(10)    
);

select * from surv_sys;
insert into surv_sys(student_name, parent_name, dir_no, phone_no) values('RiM', 'SoM', '1', '7076405713');
-- delete from surv_sys where parent_name='SoM'; 
-- delete from surv_sys where parent_name='RaM';
-- delete from surv_sys where phone_no = 'abcdefgh';


-- ==================================================================== 
-- ==================================================================== 
-- ==================================================================== 
-- ==================================================================== 


-- create table currently_present_children(
-- 	student_name varchar(100),
--     student_s_no varchar(5),
--     phone_no varchar(10)    
-- );
select * from currently_present_children;
-- insert into currently_present_children(student_name, student_s_no, phone_no) values('RiM', 's1', '7076405713');




-- ==================================================================== 
-- ==================================================================== 
-- ==================================================================== 
-- ==================================================================== 



-- create table currently_present_parent(
-- 	parent_name varchar(100),
--     parent_p_no varchar(5),
--     phone_no varchar(10)    
-- );

select * from currently_present_parent;
-- insert into currently_present_parent(parent_name, parent_p_no, phone_no) values('SoM', 'p1', '7076405713');
-- delete from currently_present_parent where parent_name='SoM';



