-- -----------------------------------------------------
-- Table `mydb`.`ExhibitionWinners`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`ExhibitionWinners` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`ExhibitionWinners` (
  `id` INT UNSIGNED NOT NULL auto_increment,
  `Breed` INT NULL,
  `Medal` INT NULL,
  `DogID` INT UNSIGNED NULL,
  `ExhibitionID` INT UNSIGNED NULL,
  `WinMessage` VARCHAR(1000) NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_DogID`
    FOREIGN KEY (`DogID`)
    REFERENCES `mydb`.`Dog` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_InExhibitionID`
    FOREIGN KEY (`ExhibitionID`)
    REFERENCES `mydb`.`Exhibition` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `FK_DogID_idx` ON `mydb`.`ExhibitionWinners` (`DogID` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `FK_ExhibitionID_idx` ON `mydb`.`ExhibitionWinners` (`ExhibitionID` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `IND_Breed` ON `mydb`.`ExhibitionWinners` (`Breed` ASC) VISIBLE;

SHOW WARNINGS;
