-- -----------------------------------------------------
-- Table `mydb`.`ExhibitionUsedRings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`ExhibitionUsedRings` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`ExhibitionUsedRings` (
  `id` INT UNSIGNED NOT NULL auto_increment,
  `RingID` INT UNSIGNED NOT NULL,
  `ExhibitionID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_UsedRingID`
    FOREIGN KEY (`RingID`)
    REFERENCES `mydb`.`Ring` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_ExhibitionID`
    FOREIGN KEY (`ExhibitionID`)
    REFERENCES `mydb`.`Exhibition` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `FK_RingID_idx` ON `mydb`.`ExhibitionUsedRings` (`RingID` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `FK_ExhibitionID_idx` ON `mydb`.`ExhibitionUsedRings` (`ExhibitionID` ASC) VISIBLE;

SHOW WARNINGS;
