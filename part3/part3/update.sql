update TBI.GNG set Correctness = 0.5394 where TestDate = '2013-08-16' and AID = 6204;
update TBI.TMaze set AlterRate = 0.578, CorrectRate = 0.2398 where AID = 6570 and TestDate = '2013-10-24' and TrialNum = 3;
delete from TBI.GNG where TestDate = '2013-09-26' and AID = 6792;
delete from TBI.SHB where AID = 6185 and TrialNum = 3 and TestDate = '2014-04-08';
insert into TBI.BasicInfo values (6936, '2012-12-26', '2013-05-06');
insert into TBI.TMaze values (6936, '2013-04-14', 3, 0.5364, 0.9447);