#to pass paremeters. You get an sys.
#argv array sys.argv[0] is the program name
#sys.argv[1] the first parameter
import sys
#-------------------------
import docker
client=docker.from_env()
#-------------------------
import sys  #needed when using parameters
print ("STOPCON:")
print (sys.argv[1])

#selecteer the container from parameter
cont=client.containers.get(sys.argv[1])
#stop de container
cont.stop()
print ("done")
