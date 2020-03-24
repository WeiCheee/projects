#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import platform
import re
import shutil
import struct
import time
from sys import version_info

def get_current_time():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "[%s.%03d]" % (data_head, data_secs)
    return time_stamp

def MsgOut(Sstr):
    print (get_current_time()+" "+Sstr)
    return

### change all files to 777 start
Sstr = "find ./ -type f -exec chmod 777 {} \;"
os.system(Sstr)
### change all files to 777 end

if platform.machine() == "aarch64":
	pgm="./VULnx/vulnx64a"
else:
	if platform.machine() == "x86_64":
		pgm="./VULnx/vulnx64"
	else:
		pgm="./VULnx/vulnx86"

if(len(sys.argv)>2):
	devInfo = []
	print (sys.argv[1])
	devInfo.append(sys.argv[1]) 
	devInfo.append(sys.argv[2])
else:
	###Get drive SN from ./hdparm -i start	
	Sstr = "./" + pgm + " -l " + "|tee DriveInfo.txt"
	print (Sstr)
	p = os.system(Sstr)

	'''
	f = open('DriveInfo.txt', 'r')
	for line in f:
		print (line)
	f.close()
	''' 

	## input deveice path ,port id start
	print ("if Megarid disk,Please intput Device Path and Port ID:")
	print ("-->For example: /dev/sda 8:")
	print ("if none Megarid disk,Please intput Device Path:")
	print ("-->For example: /dev/sdc:")
	if(version_info.major == 2):
		Sstr = raw_input(" ")
	else:
		Sstr = input(" ")
	Sstr.strip()
	devInfo = Sstr.split(' ')
	for i in range(devInfo.count('')):
		devInfo.remove('')
	print(devInfo)
	## input deveice path ,port id  end

if len(devInfo) > 0:
	###check modle start
	if (len(devInfo) == 1):
		Sstr = "./" + pgm + " " + "-d" + " " + devInfo[0] + " -f vucmd cdb=21 in=512 >CheckModel.txt"
	else:
		Sstr = "./" + pgm + " " + "-d" + " " + devInfo[0] +","+devInfo[1] + " -f vucmd cdb=21 in=512 >CheckModel.txt"

	MsgOut(Sstr) 
	p = os.system(Sstr)
	f = open('CheckModel.txt', 'r')
	ModelName=""
	#DriveSN = "0000"
	for line in f:
		##print line
		##get driver model name start	
		if re.match('0000', line):
			##print (line)
			line = line.lstrip()
			line = line.rstrip()
			line = line.replace("  ", " ")
			line = line.replace("-", " ")
			line = line.replace(".", "")
			getString = line.split(' ')
			#print (getString)
			ModelName1 = getString[len(getString)-4]
			ModelName2 = getString[len(getString)-3]
			ModelName = ModelName1 + ModelName2
			if(ModelName == ""):
				ModelName = "NULL"
			#print ModelName			
			ModelName = ModelName.strip()
			MsgOut("ModelName:" + ModelName)
		##get driver model name end
	f.close()
	###check modle end


	##get driver SN	start
	if (len(devInfo) == 1):
		Sstr = "./" + pgm + " " + "-d" + " " + devInfo[0] + " -f vucmd cdb=2D in=8192 >E2.txt"
	else:
		Sstr = "./" + pgm + " " + "-d" + " " + devInfo[0] +","+devInfo[1] + " -f vucmd cdb=2D in=8192 >E2.txt"

	MsgOut(Sstr) 
	p = os.system(Sstr)
	f = open('E2.txt', 'r')
	#DriveSN = "0000"
	for line in f:
		##print line
		
		##get driver SN	start
		if re.match('04C0', line):
			#print line
			line = line.lstrip()
			line = line.rstrip()
			line = line.replace("  ", " ")
			line = line.replace("-", " ")
			line = line.replace(".", "")
			getString = line.split(' ')
			##print (getString)	
			DriveSN = getString[len(getString)-1]
			if(DriveSN == ""):
				DriveSN = "0000"
			#print ModelName			
			DriveSN = DriveSN.strip()
			DriveSN = "SN"+DriveSN
			DriveSN = DriveSN.upper()
			#print "DriveSN:" + DriveSN 	
		##get driver SN	end
	f.close()
	###check modle end

	if (ModelName == "SMI22581")or(ModelName == "SMI22582"):
		if platform.machine() == "aarch64":
			if (len(devInfo) == 1):
				Sstr = "./" + "./SmartCtl/smartctla" + " " + "-a" + " " + devInfo[0] + "  > SMARTInfo.txt"
			else:
				Sstr = "./" + "./SmartCtl/smartctla" + " " + "-a" + " " +"-d" + " "+ "megaraid,"+ devInfo[1] +" "+ devInfo[0] + "  > SMARTInfo.txt"
		else:
			if (len(devInfo) == 1):
				Sstr = "./" + "./SmartCtl/smartctl" + " " + "-a" + " " + devInfo[0] + "  > SMARTInfo.txt"
			else:
				Sstr = "./" + "./SmartCtl/smartctl" + " " + "-a" + " " +"-d" + " "+ "megaraid,"+ devInfo[1] +" "+ devInfo[0] + "  > SMARTInfo.txt"
		p = os.system(Sstr)
		MsgOut(Sstr)
		if(DriveSN == "SN0000"):
			#pass
			f = open('SMARTInfo.txt', 'r')
			for line in f:
				if re.search('\Serial Number:', line):
					#print line
					line = line.lstrip()
					line = line.rstrip()
					getString = line.split(':')
					#print getString
					DriveSN = getString[1]
					DriveSN = DriveSN.replace(" ", "")
					#print DriveSN
					#DriveSN = DriveSN.replace("\n", "")
					DriveSN = "SN" + DriveSN
					MsgOut("DriveSN:" +DriveSN)
					break			
			f.close()
		
	## make a dir use SN name start
	if os.path.isdir("./" + DriveSN) != True:
		MsgOut("make dir:" +  "./" + DriveSN)
		#os.mkdir("./" + DriveSN,0777)
	else:
		print ("remove dir:" +  "./" + DriveSN)
		shutil.rmtree("./" + DriveSN)
		# os.removedirs("./" + DriveSN)
		MsgOut("make dir:" +  "./" + DriveSN)
		#os.mkdir("./" + DriveSN,0777)
	os.mkdir("./" + DriveSN)
	## make a dir use SN name end

	if(ModelName == "SMI22581")or(ModelName == "SMI22582"):
		MsgOut("===Dump Save Log Start===")
		#Dump log Raw data -- 16KB one loop
		for i in range(0,128):
			if len(devInfo) > 3:
				fileName = "./" + DriveSN  + "/" + str(i).zfill(3)+ "_"+str(devInfo[3]) + ".raw"
			else:
				fileName = "./" + DriveSN  + "/" + str(i).zfill(3) + ".raw"
        
			#judge file is object
			if os.path.isfile(fileName): 
				os.remove(fileName)		
		
			lpg = str(hex(i%0x100)).replace('0x','')

			#print hpg +lpg -- VU(1C,BE,10,LPage,HPage)
			if (len(devInfo) == 1):
				Sstr = "./" + pgm + " -d " + devInfo[0] 
			else:
				Sstr = "./" + pgm + " -d " + devInfo[0] +","+devInfo[1]
			Sstr += " -f vucmd cdb=1C,BE,10,"+lpg.zfill(2) + ",00" +" in=16384 outfile=" + fileName + " >log.txt"
			MsgOut(Sstr)
			p = os.system(Sstr)
					
			### Wait one second
			time.sleep(0.05)		
	else:
		MsgOut("Model name is not CV8/CVZ,can not down savelog!!")
		pass

		
	if os.path.isfile("./in.txt"):				
		os.rename("in.txt", "SavelogInfo.txt")

	#print "./" + DriveSN + "/SavelogInfo.txt"
	if os.path.isfile("./" + DriveSN + "/SavelogInfo.txt"):
		os.remove("./" + DriveSN + "/SavelogInfo.txt")

	if os.path.isfile("./SavelogInfo.txt"):
		shutil.move("./SavelogInfo.txt", "./" + DriveSN)

	if os.path.isfile("./log.txt"):
		os.remove("./log.txt")

	if os.path.isfile("./CheckModel.txt"):
		shutil.move("./CheckModel.txt", "./" + DriveSN)

	if os.path.isfile("./E2.txt"):
		shutil.move("./E2.txt", "./" + DriveSN)

	if os.path.isfile("./SMARTInfo.txt"):
		shutil.move("./SMARTInfo.txt", "./" + DriveSN)

	if os.path.isfile("./tmp.txt"):	
		os.remove("./tmp.txt")

	p = os.system('chmod 777 -R ./' + DriveSN + '/')

	if os.path.isfile("out.bin"):
		os.remove("out.bin")

	if os.path.isfile("DriveInfo.txt"):
		os.remove("DriveInfo.txt")

	MsgOut("tar file... please wait about 1 minute")

	# tar -jvcf DriveSN.tar.bz2 DriveSN/
	p = os.system('tar -jcf ' + DriveSN + '.tar.bz2 ' + DriveSN + '/')
	# chmod 777 DriveSN.tar.bz2 
	p = os.system('chmod 777 ' + DriveSN + '.tar.bz2 ')
	#p = os.system('chmod 777 log.txt')

	MsgOut("Dump Log done!!")

else:
	if os.path.isfile("DriveInfo.txt"):
		os.remove("DriveInfo.txt")
	print ("Error: Please specify the drive path")
	print ("if Megarid disk,Please intput Device Path and Port ID:")
	print ("-->For example: /dev/sda 8:")
	print ("if none Megarid disk,Please intput Device Path:")
	print ("-->For example: /dev/sdc:")
