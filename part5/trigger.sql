drop trigger if exists TBI.InsertAID;
DELIMITER |
CREATE TRIGGER TBI.InsertAID AFTER insert on TBI.Weight 
for each row begin
if (new.AID NOT IN (select AID from TBI.BasicInfo)) then
	INSERT INTO TBI.BasicInfo values(new.AID, null, null);
	#insert into TBI.avgweight values(new.AID, null);
end if;
end;
|
