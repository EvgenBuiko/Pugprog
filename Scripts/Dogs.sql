-- -----------------------------------------------------
-- Table `mydb`.`Dog`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Dog` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`Dog` (
  `id` INT UNSIGNED NOT NULL,
  `OwnerID` INT UNSIGNED NULL,
  `Name` VARCHAR(45) NULL,
  `Age` INT NULL,
  `Breed` INT NULL,
  `FatherBreed` INT NULL,
  `MotherBreed` INT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_DogsOwner`
    FOREIGN KEY (`OwnerID`)
    REFERENCES `mydb`.`DogsOwner` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `FK_DogsOwner_idx` ON `mydb`.`Dog` (`OwnerID` ASC) VISIBLE;

SHOW WARNINGS;