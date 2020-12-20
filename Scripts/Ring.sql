-- -----------------------------------------------------
-- Table `mydb`.`Ring`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Ring` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `mydb`.`Ring` (
  `id` INT UNSIGNED NOT NULL,
  `RingName` varchar(45) not null,
  `Breed` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SHOW WARNINGS;
