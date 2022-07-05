SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema DEPALS
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `DEPALS` ;

-- -----------------------------------------------------
-- Schema DEPALS
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `DEPALS` DEFAULT CHARACTER SET utf8 ;
USE `DEPALS` ;

-- -----------------------------------------------------
-- Table `DEPALS`.`Lebensmittel`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DEPALS`.`Lebensmittel` ;

CREATE TABLE IF NOT EXISTS `DEPALS`.`Lebensmittel` (
  `barcodeID` VARCHAR(50) NOT NULL,
  `bezeichnung` VARCHAR(50) NOT NULL,
  `img`Varchar(100) NULL,
  `kcal` INT NULL,
  `contains` VARCHAR(500) NULL,
  `fat` INT NULL,
  `carbohydrates` INT NULL,
  `protein` INT NULL,
  PRIMARY KEY (`barcodeID`),
  UNIQUE INDEX `barcodeID_UNIQUE` (`barcodeID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DEPALS`.`Tag`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DEPALS`.`Tag` ;

CREATE TABLE IF NOT EXISTS `DEPALS`.`Tag` (
  `tagID` INT NOT NULL,
  `beschreibung` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`tagID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DEPALS`.`Tag_has_Lebensmittel`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DEPALS`.`Tag_has_Lebensmittel` ;

CREATE TABLE IF NOT EXISTS `DEPALS`.`Tag_has_Lebensmittel` (
  `Tag_tagID` INT NOT NULL,
  `Lebensmittel_barcodeID` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`Tag_tagID`, `Lebensmittel_barcodeID`),
  INDEX `fk_Tag_has_Lebensmittel_Lebensmittel1_idx` (`Lebensmittel_barcodeID` ASC) VISIBLE,
  INDEX `fk_Tag_has_Lebensmittel_Tag_idx` (`Tag_tagID` ASC) VISIBLE,
  CONSTRAINT `fk_Tag_has_Lebensmittel_Tag`
    FOREIGN KEY (`Tag_tagID`)
    REFERENCES `DEPALS`.`Tag` (`tagID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tag_has_Lebensmittel_Lebensmittel1`
    FOREIGN KEY (`Lebensmittel_barcodeID`)
    REFERENCES `DEPALS`.`Lebensmittel` (`barcodeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DEPALS`.`Lebensmittel_has_Lebensmittel`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DEPALS`.`Lebensmittel_has_Lebensmittel` ;

CREATE TABLE IF NOT EXISTS `DEPALS`.`Lebensmittel_has_Lebensmittel` (
  `Lebensmittel_barcodeID` VARCHAR(50) NOT NULL,
  `Lebensmittel_barcodeID1` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`Lebensmittel_barcodeID`, `Lebensmittel_barcodeID1`),
  INDEX `fk_Lebensmittel_has_Lebensmittel_Lebensmittel2_idx` (`Lebensmittel_barcodeID1` ASC) VISIBLE,
  INDEX `fk_Lebensmittel_has_Lebensmittel_Lebensmittel1_idx` (`Lebensmittel_barcodeID` ASC) VISIBLE,
  CONSTRAINT `fk_Lebensmittel_has_Lebensmittel_Lebensmittel1`
    FOREIGN KEY (`Lebensmittel_barcodeID`)
    REFERENCES `DEPALS`.`Lebensmittel` (`barcodeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Lebensmittel_has_Lebensmittel_Lebensmittel2`
    FOREIGN KEY (`Lebensmittel_barcodeID1`)
    REFERENCES `DEPALS`.`Lebensmittel` (`barcodeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DEPALS`.`Nutzer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DEPALS`.`Nutzer` ;

CREATE TABLE IF NOT EXISTS `DEPALS`.`Nutzer` (
  `userName` VARCHAR(100) NOT NULL,
  `weight` DOUBLE NULL,
  `height` DOUBLE NULL,
  `hashedPassword` VARCHAR(450) NOT NULL,
  `authCookie` VARCHAR(100) NULL,
  PRIMARY KEY (`userName`),
  UNIQUE INDEX `userName_UNIQUE` (`userName` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DEPALS`.`Plan`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DEPALS`.`Plan` ;

CREATE TABLE IF NOT EXISTS `DEPALS`.`Plan` (
  `planID` INT NOT NULL AUTO_INCREMENT,
  `comment` VARCHAR(400) NULL,
  `stars` FLOAT NULL,
  `userName` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`planID`, `userName`),
  UNIQUE INDEX `planID_UNIQUE` (`planID` ASC) VISIBLE,
  INDEX `fk_Plan_Nutzer1_idx` (`userName` ASC) VISIBLE,
  CONSTRAINT `fk_Plan_Nutzer1`
    FOREIGN KEY (`userName`)
    REFERENCES `DEPALS`.`Nutzer` (`userName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DEPALS`.`Lebensmittel_has_Plan`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DEPALS`.`Lebensmittel_has_Plan` ;

CREATE TABLE IF NOT EXISTS `DEPALS`.`Lebensmittel_has_Plan` (
  `Lebensmittel_barcodeID` VARCHAR(50) NOT NULL,
  `Plan_planID` INT NOT NULL,
  `Plan_Nutzer` varchar(100) NOT NULL,
  PRIMARY KEY (`Lebensmittel_barcodeID`, `Plan_planID`, `Plan_Nutzer`),
  INDEX `fk_Lebensmittel_has_Plan_Plan1_idx` (`Plan_planID` ASC) VISIBLE,
  INDEX `fk_Lebensmittel_has_Plan_Plan_Nutzer1_idx` (`Plan_Nutzer` ASC) VISIBLE,
  INDEX `fk_Lebensmittel_has_Plan_Lebensmittel1_idx` (`Lebensmittel_barcodeID` ASC) VISIBLE,
  CONSTRAINT `fk_Lebensmittel_has_Plan_Lebensmittel1`
    FOREIGN KEY (`Lebensmittel_barcodeID`)
    REFERENCES `DEPALS`.`Lebensmittel` (`barcodeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Lebensmittel_has_Plan_Plan1`
    FOREIGN KEY (`Plan_planID`)
    REFERENCES `DEPALS`.`Plan` (`planID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Lebensmittel_has_Plan_PlanNutzer1`
    FOREIGN KEY (`Plan_Nutzer`)
    REFERENCES `DEPALS`.`Plan` (`userName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- INSERT DATA
-- -----------------------------------------------------
insert lebensmittel(barcodeID,bezeichnung,img,kcal,contains,fat,carbohydrates,protein) value 
('4316268365888','DEPALS-Schokokuchen', 'http://localhost/img/depals/schoko.jpg', 880,'Nuts',20,30,8),
('2910041002162','DEPALS-Apfel', 'http://localhost/img/depals/appel.jpg', 60,'',3,2,4),
('4009249019923','Toast', 'http://localhost/img/depals/toastcat.jpg', 313,'',56,4,3);

insert lebensmittel_has_lebensmittel(Lebensmittel_barcodeID,Lebensmittel_barcodeID1) value
('4316268365888','2910041002162 ');

insert nutzer(userName,weight,height,hashedPassword,authCookie) value 
('SimonUgar',80.1,180.5,'5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5',''); -- pw: 12345

insert plan(planID,comment,stars,userName) value
(1,'Bester Plan',3,'SimonUgar'),
(2,'mieser Plan',1,'SimonUgar');

insert tag(tagID,beschreibung) value
(1,'Kakao'),
(2,'Nuts');

insert lebensmittel_has_plan(Lebensmittel_barcodeID,Plan_planID, Plan_Nutzer) value
('4316268365888',1, 'SimonUgar'), 
('2910041002162 ',1, 'SimonUgar');

insert tag_has_lebensmittel(Tag_tagID,Lebensmittel_barcodeID) value
(1,4316268365888),
(2,4316268365888);
