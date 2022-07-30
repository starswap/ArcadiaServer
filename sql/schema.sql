CREATE TABLE "Users" (
    UserID SERIAL PRIMARY KEY NOT NULL,
    UserName VARCHAR(18) UNIQUE NOT NULL,
    PasswordHash VARCHAR(512) NOT NULL
);

CREATE TABLE "Badges"(
    BadgeID SERIAL PRIMARY KEY NOT NULL,
    BadgeName VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE "UserBadges" (
    UserID INT REFERENCES "Users"(UserID),
    BadgeID INT REFERENCES "Badges"(BadgeID),
    PRIMARY KEY(BadgeID, UserID)
);

CREATE TABLE "ArcadeIdentifier" (
    ArcadeID NUMERIC(32,0) PRIMARY KEY NOT NULL,
    ParkXCoord REAL NOT NULL,
    ParkYCoord REAL NOT NULL
);


CREATE TABLE "Scores" (
    ScoreID SERIAL PRIMARY KEY NOT NULL,
    UserID INT REFERENCES "Users"(UserID),
    Score INT NOT NULL,
    ArcadeID INT REFERENCES "ArcadeIdentifier"(ArcadeID)

);

