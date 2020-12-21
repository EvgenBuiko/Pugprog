-- -----------------------------------------------------
-- Table `mydb`.`Experts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Experts` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`Experts` (
  `id` INT UNSIGNED NOT NULL auto_increment,
  `DogsOwnerID` INT UNSIGNED NOT NULL,
  `ExpertBreed` INT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_DogsOwnerID`
    FOREIGN KEY (`DogsOwnerID`)
    REFERENCES `mydb`.`DogsOwner` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `FK_DogsOwnerID_idx` ON `mydb`.`Experts` (`DogsOwnerID` ASC) VISIBLE;

SHOW WARNINGS;
CREATE UNIQUE INDEX `DogsOwnerID_UNIQUE` ON `mydb`.`Experts` (`DogsOwnerID` ASC) VISIBLE;

SHOW WARNINGS;
