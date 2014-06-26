import time
from datetime import date
from datetime import timedelta
import sys
import random
import os

#fabricate record for BasicInfo 
def basicInfoFab():
	recordFile = open('basicInfo.dat', 'r')
	lines = recordFile.readlines()
	fabSQL = ""
	for line in lines:
		record = line.split()
		fabSQL += "INSERT INTO TBI.BasicInfo (AID, DOB, Impulse) "
		fabSQL += "VALUES(" + record[0] + ",'" + record[1] + "','" + record[2] + "');\n"
			
	return fabSQL

#fabricate record for Weight
def weightFab():
	recordFile = open('weight.dat', 'r')
	lines = recordFile.readlines()
	fabSQL = ""
	for line in lines:
		record = line.split()
		fabSQL += "INSERT INTO TBI.Weight (AID, WeightDate, Weight) "
		fabSQL += "VALUES(" + record[0] + ",'" + record[1] + "'," + record[2] + ");\n"
			
	return fabSQL

#fabricate record for BalanceBeam
def balanceBeamFab():
	recordFile = open('balanceBeam.dat', 'r')
	lines = recordFile.readlines()
	fabSQL = ""
	for line in lines:
		record = line.split()
		fabSQL += "INSERT INTO TBI.BalanceBeam " 
		fabSQL += "(AID, TestDate, TrialNum, Duration,"
		fabSQL += "FLSlips, FRSlips, BLSlips, BRSlips, FFalls, BFalls, FullBodyFalls) "
		fabSQL += "VALUES(" + record[0] + ",'" + record[1] + "'," + record[2] + ","
		fabSQL += record [3] + "," + record[4] + "," + record[5] + "," 
		fabSQL += record [6] + "," + record[7] + "," + record[8] + "," 
		fabSQL += record [9] + "," + record[10] + ");\n"
			
	return fabSQL

#fabricate record for GNG
def gNGFab():
	recordFile = open('gNG.dat', 'r')
	lines = recordFile.readlines()
	fabSQL = ""
	for line in lines:
		record = line.split()
		fabSQL += "INSERT INTO TBI.GNG (AID, TestDate, Correctness) "
		fabSQL += "VALUES(" + record[0] + ",'" + record[1] + "'," + record[2] + ");\n"
	
	return fabSQL

#fabricate record for SHB
def sHBFab():
	recordFile = open('sHB.dat', 'r')
	lines = recordFile.readlines()
	fabSQL = ""
	for line in lines:
		record = line.split()
		fabSQL += "INSERT INTO TBI.SHB " 
		fabSQL += "(AID, TestDate, TrialNum, Duration,"
		fabSQL += "BaitedRevisits, BaitedVisits, UnbaitedVisits) "
		fabSQL += "VALUES(" + record[0] + ",'" + record[1] + "'," + record[2] + ","
		fabSQL += record [3] + "," + record[4] + "," + record[5] + "," 
		fabSQL += record [6] + ");\n"
	
	return fabSQL		

#fabricate record for TMaze
def tMazeFab():
	recordFile = open('tMaze.dat', 'r')
	lines = recordFile.readlines()
	fabSQL = ""
	for line in lines:
		record = line.split()
		fabSQL += "INSERT INTO TBI.TMaze " 
		fabSQL += "(AID, TestDate, TrialNum, "
		fabSQL += "AlterRate, CorrectRate) "
		fabSQL += "VALUES(" + record[0] + ",'" + record[1] + "'," + record[2] + ","
		fabSQL += record [3] + "," + record[4] + ");\n"
	
	return fabSQL		

#export all fabricated records into a sql file
def exportSQLFile(fileName, insertSQL):
	print "SQL export starts"
	fabSQLFile = open(fileName, 'w')
	fabSQLFile.write(insertSQL)
	print "SQL export finishes"

if __name__ == "__main__":
	fileName = 'insertSyntheticData.sql'
	insertSQL = ''

	insertSQL += basicInfoFab()
	insertSQL += balanceBeamFab()
	insertSQL += gNGFab()
	insertSQL += sHBFab()
	insertSQL += tMazeFab()
	insertSQL += weightFab()

	exportSQLFile(fileName, insertSQL)
