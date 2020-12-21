insert into `mydb`.`users` ( `id`, `Login`, `Password`, `IsAdmin` ) values ( 1, 'Admin', 'admin', 1 );
alter table `mydb`.`Users` auto_increment = 100;
commit;