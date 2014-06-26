import os
import time
from datetime import date
from datetime import timedelta
import sys
import random

#create data for basicInfo data
def createBasicInfo():
	print "create BasicInfo starts"
	basicInfo = {}
	timeDelta = timedelta(days = 180)
	for i in range(5):
		AID = 6000 + random.randint(1, 999)
		mon = random.randint(1, 12)
		day = random.randint(1, 28)
		
		DOB = date(2013, mon, day)
		impulse = DOB + timeDelta
 
		basicInfo.setdefault(AID, {})
		basicInfo[AID].setdefault('DOB', DOB)
		basicInfo[AID].setdefault('impulse', impulse)
	
	print "create BasicInfo finishes"
	basicInfoExport(basicInfo)		

	return basicInfo

#export data for basicInfo data
def basicInfoExport(basicInfo):
	print "basicInfo export starts"
	fileName = 'basicInfo.dat'
	newFile = open(fileName, "w")
	
	for AID in basicInfo:
		insertTuple = str(AID) + " " 
		insertTuple += str(basicInfo[AID]['DOB']) + " "
		insertTuple += str(basicInfo[AID]['impulse']) + "\n"
		newFile.write(insertTuple)
	print "basicInfo export finishes"

#create data for balanceBeam test table
def createBalanceBeam(basicInfo):
	print "create balanceBeam starts"
	balanceBeam = {}
	for AID in basicInfo:
		balanceBeam.setdefault(AID, {})
		for i in range(1):
			daysAfterDOB = random.randint(100, 200)
			testDate = str(basicInfo[AID]['DOB'] + timedelta(days = daysAfterDOB))
			balanceBeam[AID].setdefault(testDate, {})
			for j in range(1,6):
				duration = random.uniform(20.0, 50.0)
				fLSlips = random.randint(0, 10)
				fRSlips = random.randint(0, 10)
				bLSlips = random.randint(0, 10)
				bRSlips = random.randint(0, 10)
				fFalls = random.randint(0, 10)
				bFalls = random.randint(0, 10)
				fullBodyFalls = random.randint(0, 10)
				
				balanceBeam[AID][testDate].setdefault(j, {})
				balanceBeam[AID][testDate][j].setdefault('duration', duration)
				balanceBeam[AID][testDate][j].setdefault('fLSlips', fLSlips)
				balanceBeam[AID][testDate][j].setdefault('fRSlips', fRSlips)
				balanceBeam[AID][testDate][j].setdefault('bLSlips', bLSlips)
				balanceBeam[AID][testDate][j].setdefault('bRSlips', bRSlips)
				balanceBeam[AID][testDate][j].setdefault('fFalls', fFalls)
				balanceBeam[AID][testDate][j].setdefault('bFalls', bFalls)
				balanceBeam[AID][testDate][j].setdefault('fullBodyFalls', fullBodyFalls)
				
				
	print "create balanceBeam finishes"
	exportBalanceBeam(balanceBeam)
	return balanceBeam

#export data for balanceBeam test table
def exportBalanceBeam(balanceBeam):
	print "balanceBeam export starts"
	fileName = 'balanceBeam.dat'
	newFile = open(fileName, "w")
	for AID in balanceBeam:
		for testDate in balanceBeam[AID]:
			for trialNum in balanceBeam[AID][testDate]:
				insertTuple = str(AID) + ' ' + testDate + ' ' + str(trialNum) + ' '
				insertTuple += str(balanceBeam[AID][testDate][trialNum]['duration']) + ' '
				insertTuple += str(balanceBeam[AID][testDate][trialNum]['fLSlips']) + ' '
				insertTuple += str(balanceBeam[AID][testDate][trialNum]['fRSlips']) + ' '
				insertTuple += str(balanceBeam[AID][testDate][trialNum]['bLSlips']) + ' '
				insertTuple += str(balanceBeam[AID][testDate][trialNum]['bRSlips']) + ' '
				insertTuple += str(balanceBeam[AID][testDate][trialNum]['fFalls']) + ' '
				insertTuple += str(balanceBeam[AID][testDate][trialNum]['bFalls']) + ' '
				insertTuple += str(balanceBeam[AID][testDate][trialNum]['fullBodyFalls']) + '\n'
				newFile.write(insertTuple)
	print "balanceBeam export finishes"
	
#create data for GNG table
def createGNG(basicInfo):
	print "GNG create starts"
	gNG = {}
	for AID in basicInfo:
		gNG.setdefault(AID, {})
		for i in range(5):
			daysAfterDOB = random.randint(100, 200)
			testDate = str(basicInfo[AID]['DOB'] + timedelta(days = daysAfterDOB))
			correctness = random.uniform(0.0, 1.0)
			gNG[AID].setdefault(testDate, {})
			gNG[AID][testDate].setdefault('correctness', correctness)

	
	exportGNG(gNG)			
	print "GNG create finishes"

	return gNG

#export data for GNG table
def exportGNG(gNG):
	print "GNG export starts"
	fileName = 'gNG.dat'
	newFile = open(fileName, "w")
	for AID in gNG:
		for testDate in gNG[AID]:
			insertTuple = str(AID) + ' ' + testDate + ' '
			insertTuple += str(gNG[AID][testDate]['correctness']) + '\n'
			newFile.write(insertTuple)		
		
	print "GNG export finishes"

#create data for SHB table
def createSHB(basicInfo):
	print "sHB create starts"
	sHB = {}
	for AID in basicInfo:
		sHB.setdefault(AID, {})
		for i in range(1):
			daysAfterDOB = random.randint(100, 200)
			testDate = str(basicInfo[AID]['DOB'] + timedelta(days = daysAfterDOB))
			sHB[AID].setdefault(testDate, {})
			for j in range(1, 6):
				duration = random.uniform(20.0, 60.0)
				bRevisits = random.randint(0, 10)
				bVisits = random.randint(0, 10)
				UbVisits = random.randint(0, 10)

				sHB[AID][testDate].setdefault(j, {})				
				sHB[AID][testDate][j].setdefault('duration', duration)				
				sHB[AID][testDate][j].setdefault('bRevisits', bRevisits)				
				sHB[AID][testDate][j].setdefault('bVisits', bVisits)				
				sHB[AID][testDate][j].setdefault('ubVisits', UbVisits)				
	
	exportSH(sHB)
	print "sHB create finishes"
	return sHB

#export data for SHB table
def exportSH(sHB):
	print "sHB export starts"
	fileName = 'sHB.dat'
	newFile = open(fileName, 'w')
	for AID in sHB:
		for testDate in sHB[AID]:
			for trialNum in sHB[AID][testDate]:
				insertTuple = str(AID) + ' ' + testDate + ' ' + str(trialNum) + ' '
				insertTuple += str(sHB[AID][testDate][trialNum]['duration']) + ' '
				insertTuple += str(sHB[AID][testDate][trialNum]['bRevisits']) + ' '
				insertTuple += str(sHB[AID][testDate][trialNum]['bVisits']) + ' '
				insertTuple += str(sHB[AID][testDate][trialNum]['ubVisits']) + '\n'
				newFile.write(insertTuple)
	
	print"sHB export finishes"
 
#create data for tMaze table
def createTMaze(basicInfo):
	print "tMaze create starts"
	tMaze = {}
	for AID in basicInfo:
		tMaze.setdefault(AID, {})
		for i in range(1):
			daysAfterDOB = random.randint(100, 200)
			testDate = str(basicInfo[AID]['DOB'] + timedelta(days = daysAfterDOB))
			tMaze[AID].setdefault(testDate, {})
			for j in range(1, 6):
				alterRate = random.uniform(0.0, 1.0)
				correctRate = random.uniform(0.0, 1.0)
				
				tMaze[AID][testDate].setdefault(j, {})
				tMaze[AID][testDate][j].setdefault('alterRate', alterRate)
				tMaze[AID][testDate][j].setdefault('correctRate', correctRate)
	
	exportTMaze(tMaze)
	print "tMaze create finishes"
	return tMaze

#export data for tMaze table
def exportTMaze(tMaze):
	print "tMaze export starts"
	fileName = 'tMaze.dat'
	newFile = open(fileName, 'w')
	for AID in tMaze:
		for testDate in tMaze[AID]:
			for trialNum in tMaze[AID][testDate]:
				insertTuple = str(AID) + ' ' + testDate + ' ' + str(trialNum) + ' '
				insertTuple += str(tMaze[AID][testDate][trialNum]['alterRate']) + ' '
				insertTuple += str(tMaze[AID][testDate][trialNum]['correctRate']) + '\n'
				newFile.write(insertTuple)
	
	print "tMaze export finishes"

#create data for weight table
def createWeight(basicInfo):
	print "weight create starts"
	weight = {}
	for AID in basicInfo:
		weight.setdefault(AID, {})
		for i in range(1):
			daysAfterDOB = random.randint(100, 200)
			weightDate = str(basicInfo[AID]['DOB'] + timedelta(days = daysAfterDOB))
			weightValue = random.uniform(10.0, 20.0)
			weight[AID].setdefault(weightDate, weightValue)
	
	exportWeight(weight)
	print "weight create finishes"
	return weight

#export data for weight table
def exportWeight(weight):
	print "weight export starts"
	fileName = 'weight.dat'
	newFile = open(fileName, 'w')
	for AID in weight:
		for weightDate in weight[AID]:
			insertTuple = str(AID) + ' ' + weightDate + ' '
			insertTuple += str(weight[AID][weightDate]) + '\n'
			newFile.write(insertTuple)
	
	print "weight export finishes"

if __name__ == "__main__":
	basicInfo = createBasicInfo()
	balanceBeam = createBalanceBeam(basicInfo)
	gNG = createGNG(basicInfo)
	sHB = createSHB(basicInfo)
	tMaze = createTMaze(basicInfo)	
	weight = createWeight(basicInfo)
	sys.exit()


