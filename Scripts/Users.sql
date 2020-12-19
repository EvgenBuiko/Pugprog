-- -----------------------------------------------------
-- Table `mydb`.`Users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Users` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`Users` (
  `id` INT NOT NULL,
  `Login` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  `IsAdmin` TINYINT NOT NULL,
  `DogsOwnerID` INT UNSIGNED NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_DogsOwnerID`
    FOREIGN KEY (`DogsOwnerID`)
    REFERENCES `mydb`.`DogsOwner` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX `DogsOwnerID_UNIQUE` ON `mydb`.`Users` (`DogsOwnerID` ASC) VISIBLE;

SHOW WARNINGS;
