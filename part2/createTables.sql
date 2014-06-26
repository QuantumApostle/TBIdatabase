CREATE DATABASE TBI;
CREATE TABLE TBI.BasicInfo(
    AID INT, 
    DOB DATE,
    Impulse DATE,
    PRIMARY KEY (AID)
);

CREATE TABLE TBI.Weight(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    WeightDate DATE,
    Weight FLOAT,
    PRIMARY KEY (AID, WeightDate)    
);

CREATE TABLE TBI.GNG(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    TestDate DATE,
    Correctness FLOAT,
    PRIMARY KEY (AID, TestDate)
);

CREATE TABLE TBI.BalanceBeam(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    TestDate DATE,
    TrialNum INT,
    Duration FLOAT,

    FLSlips INT,
    FRSlips INT,
    BLSlips INT,
    BRSlips INT,
    
    FFalls INT,
    BFalls INT,
    FullBodyFalls INT,
    
    PRIMARY KEY (AID, TestDate, TrialNum)
);

CREATE TABLE TBI.TMaze(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    TestDate DATE,
    TrialNum INT,
    
    AlterRate FLOAT,
    CorrectRate FLOAT,

    PRIMARY KEY (AID, TestDate, TrialNum)
);

CREATE TABLE TBI.SHB(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    TestDate DATE,
    TrialNum INT,
    Duration FLOAT,
    BaitedRevisits INT,
    BaitedVisits INT,
    UnbaitedVisits INT,
    PRIMARY KEY (AID, TestDate, TrialNum)
);














