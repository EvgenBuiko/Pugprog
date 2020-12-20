-- -----------------------------------------------------
-- Table `mydb`.`ExibitionExperts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`ExibitionExperts` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`ExibitionExperts` (
  `id` INT UNSIGNED NOT NULL,
  `ExpertID` INT UNSIGNED NOT NULL,
  `RingID` INT UNSIGNED NOT NULL,
  `ExibitionID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_ExpertID`
    FOREIGN KEY (`ExpertID`)
    REFERENCES `mydb`.`Experts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_RingID`
    FOREIGN KEY (`RingID`)
    REFERENCES `mydb`.`Ring` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_ExibitionID`
    FOREIGN KEY (`ExibitionID`)
    REFERENCES `mydb`.`Exhibition` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `FK_ExpertID_idx` ON `mydb`.`ExibitionExperts` (`ExpertID` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `FK_RingID_idx` ON `mydb`.`ExibitionExperts` (`RingID` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `FK_ExibitionID_idx` ON `mydb`.`ExibitionExperts` (`ExibitionID` ASC) VISIBLE;

SHOW WARNINGS;
