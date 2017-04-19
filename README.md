# AWSjson
MySQL import of AWS Json files into databases for servers without internet access (local file load).

Files can be downloaded from [AWS.dk](http://download.aws.dk/adresser)

# Usage
Create the database for import in MySQL:
CREATE TABLE IF NOT EXISTS `geodata` (
  `street` varchar(200) COLLATE utf8_danish_ci NOT NULL,
  `number` varchar(10) COLLATE utf8_danish_ci NOT NULL,
  `door` varchar(10) COLLATE utf8_danish_ci DEFAULT NULL,
  `floor` varchar(10) COLLATE utf8_danish_ci DEFAULT NULL,
  `zip` int(10) NOT NULL,
  `city` varchar(100) COLLATE utf8_danish_ci NOT NULL,
  `longtitude` decimal(40,15) NOT NULL,
  `latitude` decimal(40,15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci;

Edit config.ini-example and rename to config.ini

Run it with Python2.7

????

Profit.
