import commands
import time

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

print "APKTool total time %f" %cmp_apktool("/Users/mac/Desktop/smsup_signed.apk")
print "AAPT total time %f" %cmp_aapt("/Users/mac/Desktop/smsup_signed.apk")
