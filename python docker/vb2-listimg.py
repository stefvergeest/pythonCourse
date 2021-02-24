#get the docker library
#-------------------------
import docker
client=docker.from_env()
#-------------------------
print ("listimg:")
#loop door alle images
print ("ALL IMAGES")
print ("-----------------------------------")
for  img in client.images.list():
  #print (img.id[0:4], "\t", img.tags)
  print (img.id[0:14], "\t", img.tags[0])  #de eerste tag

print ("done")
