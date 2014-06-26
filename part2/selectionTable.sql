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

CREATE TABLE TBI.BalanceBeamFalls(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    TestDate DATE,
    TrialNum INT,
    Duration FLOAT,
    TotalFalls INT,
    Front INT,
    Back INT,
    FullBody INT,
    PRIMARY KEY (AID, TestDate, TrialNum)
);

CREATE TABLE TBI.BalanceBeamSlips(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    TestDate DATE,
    TrialNum INT,
    Duration INT,
    FrontLeft INT,
    FrontRight INT,
    BackLeft INT,
    BackRight INT,
    TotalSlips INT,
    PRIMARY KEY (AID, TestDate, TrialNum)
);

CREATE TABLE TBI.GNGSelect(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    Mean FLOAT,
    MeanRank INT,
    SD Float,
    SDRank INT,
    PRIMARY KEY (AID)
);

CREATE TABLE TBI.SelectTotalRank(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    RankValue INT,
    TotalRank INT,
    PRIMARY KEY (AID)
);

CREATE TABLE TBI.TMazeSelectC(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    Mean FLOAT,
    MeanRank INT,
    SD Float,
    SDRank INT,
    PRIMARY KEY (AID)
);

CREATE TABLE TBI.TMazeSelectNC(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    Mean FLOAT,
    MeanRank INT,
    SD Float,
    SDRank INT,
    PRIMARY KEY (AID)
);

CREATE TABLE TBI.TMaze(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    TestDate DATE,
    AMorPM CHAR(2),
    CorrectRate FLOAT,
    AlterRate FLOAT,
    PRIMARY KEY (AID, TestDate, AMorPM)
);

CREATE TABLE TBI.SH(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    TestDate DATE,
    TrialNum INT,
    Duration FLOAT,
    WM FLOAT,
    RM FLOAT,
    BaitedRevisits INT,
    BaitedVisits INT,
    UnbaitedVisits INT,
    TotalVisits INT,
    PRIMARY KEY (AID, TestDate, TrialNum)
);

CREATE TABLE TBI.SHSelect(
    AID INT REFERENCES TBI.BasicInfo(AID) ON DELETE CASCADE,
    WM FLOAT,
    WMRank INT,
    RM FLOAT,
    RMRank INT,
    PRIMARY KEY (AID) 
);













