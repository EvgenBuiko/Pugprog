-- -----------------------------------------------------
-- Table `mydb`.`DogsOwnerExhibitions`
-- -----------------------------------------------------
drop table if exists `mydb`.`DogsOwnerExhibitions`;

create table if not exists `mydb`.`DogsOwnerExhibitions` (
	`id` int unsigned not null,
    `DogsOwnerID` int unsigned not null,
    `ExhibitionID` int unsigned not null,
    primary key ( `id` ),
    constraint `FK_ParticipaterID`
		foreign key (`DogsOwnerID`)
        references `mydb`.`DogsOwner` ( `id` )
        on delete no action
        on update no action,
    constraint `FK_DogsOwnerInExhibitionID`
		foreign key (`ExhibitionID`)
        references `mydb`.`Exhibition` ( `id` )
        on delete no action
        on update no action)
engine = InnoDB;

create index `FK_ParticipaterID_idx` on	`mydb`.`DogsOwnerExhibitions` ( `DogsOwnerID` asc) visible;

create index `FK_DogsOwnerInExhibitionID_idx` on `mydb`.`DogsOwnerExhibitions` ( `ExhibitionID` asc) visible;
 

