drop view if exists TBI.AvgWeights;
create view TBI.AvgWeights as
    select 
        AID, round(AVG(weight), 0.01)
    from
        TBI.Weight
    group by AID;

drop view if exists TBI.BalanceBeamSlipsFallsSum;
create view TBI.BalanceBeamSlipsFallsSum as
    select 
        AID,
        TestDate,
        TrialNum,
        (FLSlips + FRSlips + BLSlips + BRSlips) as TotalSlips,
        (FFalls + BFalls + FullBodyFalls) as TotalFalls
    from
        TBI.balancebeam
    group by AID , TestDate , TrialNum;

drop view if exists TBI.GNGAvgCorrectness;
create view TBI.GNGAvgCorrectness as
    select 
        AID, round(avg(Correctness), 0.01)
    from
        TBI.gng
    group by AID;

drop view if exists TBI.TmazeAvgARCR;
create view TBI.TmazeAvgARCR as
    select 
        AID,
        TestDate,
        round(avg(AlterRate), 0.01),
        round(avg(CorrectRate), 0.01)
    from
        TBI.tmaze
    group by AID , TestDate;