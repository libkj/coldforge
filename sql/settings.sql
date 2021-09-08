DROP TABLE IF EXISTS `hosts`;
CREATE TABLE `hosts` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `host` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`host`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;