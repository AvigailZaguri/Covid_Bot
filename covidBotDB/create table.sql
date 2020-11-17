
CREATE TABLE Person
(
  id INT,
  name VARCHAR(30),
  phone INT,
  telegramUserName VARCHAR(30) NOT NULL,
  Conversation_state INT NOT NULL,
  PRIMARY KEY (telegramUserName)
);

CREATE TABLE Location
(
  lat FLOAT NOT NULL,
  lon FLOAT NOT NULL,
  PRIMARY KEY (lat,lon)
);

CREATE TABLE LocationPerson
(
  startDateTime DATETIME NOT NULL,
  duration INT NOT NULL,
  isMask INT NOT NULL,
  isOpenSpace INT NOT NULL,
  telegramUserName VARCHAR(30) NOT NULL,
  lat FLOAT NOT NULL,
  lon FLOAT NOT NULL,
  PRIMARY KEY (telegramUserName, lat, lon),
  FOREIGN KEY (telegramUserName) REFERENCES Person(telegramUserName),
  FOREIGN KEY (lat,lon) REFERENCES Location(lat,lon)
 
);