-- -----------------------------------------------------
-- Table `mydb`.`Exhibition`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Exhibition` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`Exhibition` (
  `id` INT UNSIGNED NOT NULL,
  `Date` DATE NULL,
  `Name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SHOW WARNINGS;
