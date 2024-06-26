/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50739 (5.7.39)
 Source Host           : localhost:3306
 Source Schema         : romdul_sport

 Target Server Type    : MySQL
 Target Server Version : 50739 (5.7.39)
 File Encoding         : 65001

 Date: 26/06/2024 20:33:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for booking
-- ----------------------------
DROP TABLE IF EXISTS `booking`;
CREATE TABLE `booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `pitch_id` int(11) NOT NULL,
  `discount_line_id` int(11) NOT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of booking
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for booking_product
-- ----------------------------
DROP TABLE IF EXISTS `booking_product`;
CREATE TABLE `booking_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `remark` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of booking_product
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for branch
-- ----------------------------
DROP TABLE IF EXISTS `branch`;
CREATE TABLE `branch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `logo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `privacy` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of branch
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of category
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `alt_phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `point` varchar(255) COLLATE utf8_unicode_ci DEFAULT '100',
  `branch_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of customer
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for discount_line
-- ----------------------------
DROP TABLE IF EXISTS `discount_line`;
CREATE TABLE `discount_line` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_time` time NOT NULL,
  `to_time` time NOT NULL,
  `discount_type` int(11) NOT NULL COMMENT '1: percentage, 2: fix_price',
  `discount_amount` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of discount_line
-- ----------------------------
BEGIN;
INSERT INTO `discount_line` (`id`, `from_time`, `to_time`, `discount_type`, `discount_amount`) VALUES (1, '07:00:00', '11:00:00', 1, 40);
INSERT INTO `discount_line` (`id`, `from_time`, `to_time`, `discount_type`, `discount_amount`) VALUES (2, '11:00:00', '15:00:00', 1, 50);
INSERT INTO `discount_line` (`id`, `from_time`, `to_time`, `discount_type`, `discount_amount`) VALUES (3, '15:03:03', '19:00:00', 1, 20);
INSERT INTO `discount_line` (`id`, `from_time`, `to_time`, `discount_type`, `discount_amount`) VALUES (4, '19:00:28', '23:00:00', 1, 0);
COMMIT;

-- ----------------------------
-- Table structure for pitch
-- ----------------------------
DROP TABLE IF EXISTS `pitch`;
CREATE TABLE `pitch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `size` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'free, busy',
  `image` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of pitch
-- ----------------------------
BEGIN;
INSERT INTO `pitch` (`id`, `size`, `price`, `label`, `status`, `image`, `description`) VALUES (1, '7vs7', 10.00, 'Pitch 1', 'free', NULL, NULL);
INSERT INTO `pitch` (`id`, `size`, `price`, `label`, `status`, `image`, `description`) VALUES (2, '7vs7', 10.00, 'Pitch 2', 'free', NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `cost` decimal(10,2) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `image` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of product
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `profile` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `branch_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
