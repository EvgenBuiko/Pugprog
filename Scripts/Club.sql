-- -----------------------------------------------------
-- Table `mydb`.`Club`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Club` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`Club` (
  `id` INT UNSIGNED NOT NULL auto_increment,
  `ClubName` VARCHAR(45) NULL,
  `ClubBreed` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SHOW WARNINGS;