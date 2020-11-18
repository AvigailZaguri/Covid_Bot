
CREATE TABLE Person
(
  id VARCHAR(9),
  name VARCHAR(30),
  phone VARCHAR(11),
  telegramUserName VARCHAR(10) NOT NULL,
  Conversation_state INT NOT NULL,
  day_daignose VARCHAR(10),
  PRIMARY KEY (telegramUserName)
);

CREATE TABLE Location
(
  lat VARCHAR(30) NOT NULL,
  lon VARCHAR(30) NOT NULL,
  PRIMARY KEY (lat,lon)
);

CREATE TABLE LocationPerson
(
  startDateTime DATETIME NOT NULL,
  duration INT NOT NULL,
  isMask INT NOT NULL,
  isOpenSpace INT NOT NULL,
  telegramUserName VARCHAR(10) NOT NULL,
  lat VARCHAR(30) NOT NULL,
  lon VARCHAR(30) NOT NULL,
  PRIMARY KEY (telegramUserName, lat, lon),
  FOREIGN KEY (telegramUserName) REFERENCES Person(telegramUserName),
  FOREIGN KEY (lat,lon) REFERENCES Location(lat,lon)
 
);