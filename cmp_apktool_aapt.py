import commands
import time
import sys

def cmp_apktool(apkdir):
	entry_time = time.time()
	result = commands.getoutput("java -jar apktool.jar d " + apkdir + " -o output")
	f = open("output/AndroidManifest.xml", "rb")
	#print f.read()
	data = f.read()
	end_time = time.time()

	return float(end_time - entry_time)

def cmp_aapt(apkdir):
	entry_time = time.time()
	result = commands.getoutput("./aapt dump badging " + apkdir)
	#print result
	data = result
	end_time = time.time()
	return float(end_time - entry_time)

print "APKTool total time %f" %cmp_apktool(sys.argv[1])
print "AAPT total time %f" %cmp_aapt(sys.argv[1])
