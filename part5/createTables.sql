CREATE DATABASE TBI;
CREATE TABLE TBI.BasicInfo (
    AID INT,
    DOB DATE,
    Impulse DATE,
    PRIMARY KEY (AID)
);

CREATE TABLE TBI.Weight (
    AID INT REFERENCES TBI.BasicInfo (AID)
    ON DELETE CASCADE,
    WeightDate DATE,
    Weight FLOAT CHECK (Weight > 0.0),
    PRIMARY KEY (AID , WeightDate)
);

CREATE TABLE TBI.GNG (
    AID INT REFERENCES TBI.BasicInfo (AID)
    ON DELETE CASCADE,
    TestDate DATE,
    Correctness FLOAT CHECK (Correctness >= 0.0
        AND Correctness <= 1.0),
    PRIMARY KEY (AID , TestDate)
);

CREATE TABLE TBI.BalanceBeam (
    AID INT REFERENCES TBI.BasicInfo (AID)
    ON DELETE CASCADE,
    TestDate DATE,
    TrialNum INT CHECK (TrialNum >= 1 AND TrialNum <= 5),
    Duration FLOAT check (Duration > 0.0),
    FLSlips INT check (FLSlips >= 0),
    FRSlips INT check (FRSlips >= 0),
    BLSlips INT check (BLSlips >= 0),
    BRSlips INT check (BRSlips >= 0),
    FFalls INT check (FFalls >= 0),
    BFalls INT check (BFalls >= 0),
    FullBodyFalls INT check (FullBodyFalls >= 0),
    PRIMARY KEY (AID , TestDate , TrialNum)
);

CREATE TABLE TBI.TMaze (
    AID INT REFERENCES TBI.BasicInfo (AID)
    ON DELETE CASCADE,
    TestDate DATE,
    TrialNum INT CHECK (TrialNum >= 1 AND TrialNum >= 5),
    AlterRate FLOAT,
    CorrectRate FLOAT,
    PRIMARY KEY (AID , TestDate , TrialNum),
    CHECK (AlterRate >= 0.0 AND CorrectRate >= 0.0
        AND AlterRate <= 1.0
        AND CorrectRate <= 1.0)
);

CREATE TABLE TBI.SHB (
    AID INT REFERENCES TBI.BasicInfo (AID)
    ON DELETE CASCADE,
    TestDate DATE,
    TrialNum INT CHECK (TrialNum >= 1 AND TrialNum >= 5),
    Duration FLOAT,
    BaitedRevisits INT,
    BaitedVisits INT,
    UnbaitedVisits INT,
    PRIMARY KEY (AID , TestDate , TrialNum),
    check (Duration >= 0.0 and BaitedRevisits >= 0
        and BaitedVisits >= 0
        and UnbaitedVisits >= 0)
);














