-- -----------------------------------------------------
-- Table `mydb`.`DogsOwner`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`DogsOwner` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`DogsOwner` (
  `id` INT UNSIGNED NOT NULL auto_increment,
  `FirstName` VARCHAR(45) NULL,
  `LastName` VARCHAR(45) NULL,
  `ClubID` INT UNSIGNED NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_ClubID`
    FOREIGN KEY (`ClubID`)
    REFERENCES `mydb`.`Club` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `FK_ClubID_idx` ON `mydb`.`DogsOwner` (`ClubID` ASC) VISIBLE;

SHOW WARNINGS;
