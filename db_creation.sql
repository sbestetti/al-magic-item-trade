-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema magic_item_trade
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `magic_item_trade` ;

-- -----------------------------------------------------
-- Schema magic_item_trade
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `magic_item_trade` DEFAULT CHARACTER SET utf8 ;
USE `magic_item_trade` ;

-- -----------------------------------------------------
-- Table `magic_item_trade`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `magic_item_trade`.`users` ;

CREATE TABLE IF NOT EXISTS `magic_item_trade`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(80) NOT NULL,
  `email` VARCHAR(80) NOT NULL,
  `dci` VARCHAR(45) NOT NULL,
  `active` TINYINT NULL,
  `verified` TINYINT NULL,
  `last_login` DATETIME NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `dci_UNIQUE` (`dci` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `magic_item_trade`.`characters`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `magic_item_trade`.`characters` ;

CREATE TABLE IF NOT EXISTS `magic_item_trade`.`characters` (
  `character_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL,
  `name` VARCHAR(80) NOT NULL,
  `race` VARCHAR(45) NOT NULL,
  `barbarian` INT NULL,
  `bard` INT NULL,
  `cleric` INT NULL,
  `druid` INT NULL,
  `fighter` INT NULL,
  `monk` INT NULL,
  `paladin` INT NULL,
  `ranger` INT NULL,
  `rogue` INT NULL,
  `sorcerer` INT NULL,
  `warlock` INT NULL,
  `wizard` INT NULL,
  `artificer` INT NULL,
  `blood_hunter` INT NULL,
  PRIMARY KEY (`character_id`),
  INDEX `id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `magic_item_trade`.`users` (`user_id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `magic_item_trade`.`items`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `magic_item_trade`.`items` ;

CREATE TABLE IF NOT EXISTS `magic_item_trade`.`items` (
  `item_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `type` VARCHAR(100) NOT NULL,
  `rarity` VARCHAR(250) NOT NULL,
  `attuned` TINYINT NOT NULL,
  `notes` VARCHAR(250) NULL,
  `source` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`item_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `magic_item_trade`.`inventory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `magic_item_trade`.`inventory` ;

CREATE TABLE IF NOT EXISTS `magic_item_trade`.`inventory` (
  `inventory_id` INT NOT NULL AUTO_INCREMENT,
  `character_id` INT NULL,
  `item_id` INT NULL,
  `available` TINYINT NULL,
  PRIMARY KEY (`inventory_id`),
  INDEX `id_idx` (`character_id` ASC) VISIBLE,
  INDEX `id_idx1` (`item_id` ASC) VISIBLE,
  CONSTRAINT `character_id`
    FOREIGN KEY (`character_id`)
    REFERENCES `magic_item_trade`.`characters` (`character_id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `item_id`
    FOREIGN KEY (`item_id`)
    REFERENCES `magic_item_trade`.`items` (`item_id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `magic_item_trade`.`offers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `magic_item_trade`.`offers` ;

CREATE TABLE IF NOT EXISTS `magic_item_trade`.`offers` (
  `offer_id` INT NOT NULL AUTO_INCREMENT,
  `offered_item` INT NOT NULL,
  `wanted_item` INT NOT NULL,
  `date_created` DATETIME NOT NULL,
  `rejected` TINYINT NULL,
  `accepted` TINYINT NULL,
  PRIMARY KEY (`offer_id`),
  INDEX `id_idx` (`offered_item` ASC) VISIBLE,
  INDEX `id_idx1` (`wanted_item` ASC) VISIBLE,
  CONSTRAINT `offered_inventory_id`
    FOREIGN KEY (`offered_item`)
    REFERENCES `magic_item_trade`.`inventory` (`inventory_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `wanted_inventory_id`
    FOREIGN KEY (`wanted_item`)
    REFERENCES `magic_item_trade`.`inventory` (`inventory_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
