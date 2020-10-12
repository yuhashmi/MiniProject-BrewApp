-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `brewapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `brewapp`;

DROP TABLE IF EXISTS `Drinks`;
CREATE TABLE `Drinks` (
  `DrinkID` int NOT NULL AUTO_INCREMENT,
  `Drink` varchar(100) DEFAULT NULL,
  `Price` decimal(4,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`DrinkID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Drinks` (`DrinkID`, `Drink`, `Price`) VALUES
(1,	'Water',	0.80);

DROP TABLE IF EXISTS `FavouriteDrinks`;
CREATE TABLE `FavouriteDrinks` (
  `DrinkID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) DEFAULT NULL,
  `FavouriteDrink` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`DrinkID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `People`;
CREATE TABLE `People` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Age` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- 2020-10-08 10:36:10