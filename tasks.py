from celery import Celery
import os
import subprocess
#app = Celery('tasks', broker='amqp://guest@localhost//')
#app = Celery('tasks', backend='redis://localhost', broker='amqp://')
#app = Celery('tasks', backend='amqp', broker='amqp://')
app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y


@app.task
def fibiter(n): # Escribe n nmeros de Fibonacci    "Escribe n nmeros de Fibonacci."    
    a,b = 0,1           #Asignacin mltiple      
    salida=[]
    for x in range(n):  #Creamos una secuencia 1,2,...,n con range
        print b,        # Escribimos en una sola lnea
        salida.append(b)
        a, b = b, a+b
        
    return salida

@app.task
def list_dir():
  lst=[]
  for file in os.listdir("./"):
    if os.path.isdir(file):
      tipo='D'
    else:
      tipo='F'
    lst.append((file,tipo))
  return lst

@app.task
def cmd(cmd):
 return subprocess.check_output(cmd)
  

#def wait_animation
#	animation = "|/-\\"
#	idx = 0
#	while thing_not_complete():
#	    print animation[idx % len(animation)] + "\r",
#	    idx += 1
#	    time.sleep(0.1)
