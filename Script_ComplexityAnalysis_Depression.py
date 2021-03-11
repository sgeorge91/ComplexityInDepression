#Finds the recurrence plots of all the time series and writes the determinism and laminarity to a separate file
import numpy as np
import math
import time as tm
import os


##ID numbers of individuals with depression
ID_dep={"56","62","64","68","69","71","72","81","85","87","88","90", "93", "95", "96", "111", "139", "143", "150", "164", "166", "171","177", "198", "201","175"}


NN=4000
flag=True
fout_sig=open("Output.dat","w")
file_list=glob.glob("10*.csv")
for fn in file_list:
	b=np.loadtxt(fn)
	l1=len(b)
	temp_fil=fn.split("_")
	leng=min(l1,NN)	
	a=b[0:leng]
	file_mean=np.mean(a)
	print(file_mean)
	a=a/max(a)
	epsilon=.002
	nmean=np.nanmean(a)
	print("no nan mean is ",nmean) 
	fout123=open("junk1", "w")
	for i in range (0,len(a)): #Replace nan values with mean
		if(np.isnan(a[i])):			
			a[i]=nmean
		fout123.write(str(a[i])+'\n')
	fout123.close()
	fn1="ud_"+fn
	###The following code is written in Cpp for speed, to generate the rank ordered time series 
	os.system ("./UD.out junk1 "+str(leng))
	fn1="ud_"+fn
	ctr_e=1
	###This section increases the recurrence threshold slowly until the recurrence rate of 5% is breached 
	while(flag==True):
		#The rp is calculated using the standalone software TOCSY available at https://tocsy.pik-postdam.de 		
		os.system("./rp -i ud_junk1 -r RP_"+fn1+" -o RQA_"+fn1+" -m 1 -e "+str(ctr_e*epsilon))
		fin2=open("RQA_"+fn1)
		rpm=fin2.readlines()
		rpm2=rpm[1].split()
		ctr_e=ctr_e+1	
		if(float(rpm2[0])<.05):
			os.remove("RQA_"+fn1)									
			continue			
		else:			
			flag=False
	fin2=open("RQA_"+fn1)
	rpm=fin2.readlines()
	rpm2=rpm[1].split()	
	print(rpm2, len(rpm2))
	ID=temp_fil[1][2:len(temp_fil[1])]
	if(float(rpm2[0])>.055):
		fout_sig.write("#")
	fout_sig.write(ID+'\t'+rpm2[0]+'\t'+rpm2[1]+'\t'+rpm2[2]+'\t'+rpm2[3]+'\t'+rpm2[4]+'\t'+rpm2[5]+'\t'+rpm2[6]+'\t'+rpm2[7]+'\t'+rpm2[8]	+'\t'+rpm2[9]+'\t'+rpm2[10]+'\t'+rpm2[11]+'\t'+rpm2[12]+'\t'+rpm2[13]+'\t'+rpm2[15]+'\n')
	os.rename("ud_junk1","./ReccPlot5/ud_"+fn)
	os.rename("RQA_ud_"+fn,"./ReccPlot5/RQA_ud_"+fn)
	os.rename("RP_ud_"+fn,"./ReccPlot5/RP_ud_"+fn)
	
	flag=True

