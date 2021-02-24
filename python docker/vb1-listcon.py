#get the docker library
#-------------------------
import docker
client=docker.from_env()
#-------------------------
print ("listcon:")
#loop door alle containers
print ("ALL CONTAINERS")
print ("-----------------------------------")
for  cont in client.containers.list(all=True):
  print (cont.id, "\t", cont.name)   # \t is tab
  #print (cont.id[0:4], "\t", cont.name)

print ("done")
