-- -----------------------------------------------------
-- Table `mydb`.`ClubParticipation`
-- -----------------------------------------------------
drop table if exists `mydb`.`ClubParticipation`;

create table if not exists `mydb`.`ClubParticipation` (
	`id` int unsigned not null,
    `ClubID` int unsigned not null,
    `ExhibitionID` int unsigned not null,
    `MinParticipateNumber` int unsigned not null,
    `MaxParticipateNumber` int unsigned not null,
    primary key ( `id` ),
    constraint `FK_ParticipaterClubID`
		foreign key (`ClubID`)
        references `mydb`.`Club` ( `id` )
        on delete no action
        on update no action,
    constraint `FK_ClubInExhibitionID`
		foreign key (`ExhibitionID`)
        references `mydb`.`Exhibition` ( `id` )
        on delete no action
        on update no action)
engine = InnoDB;

create index `FK_ParticipaterClubID_idx` on	`mydb`.`ClubParticipation` ( `ClubID` asc) visible;

create index `FK_ClubInExhibitionID_idx` on	`mydb`.`ClubParticipation` ( `ExhibitionID` asc) visible;
