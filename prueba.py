import time,sys
from tasks import fibiter,list_dir,cmd

try:
 #rs=cmd.delay(["ls"])
 rs=fibiter.delay(2000)
except:
 print rs.traceback

animation = ['|' , '/' , '-','\\']
idx = 0

print 'Por favor Espere  ',
sys.stdout.flush()
while  not rs.ready():
 sys.stdout.write("\b%s" % animation[idx])
 idx += 1
 if idx==3:
  idx=0
 sys.stdout.flush
 time.sleep(0.0001)

tam=rs.get(propagate=False)

print "\n",tam,type(tam)
#print "\nFinalizado !\n" %tam
