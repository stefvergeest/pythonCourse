import subprocess
#output wordt geschreven naar variable kommaarhier(....PIPE) en wel als text (universal......=True)
process=subprocess.run(["ls", "-a"],stdout=subprocess.PIPE, universal_newlines=True)
#process=subprocess.run(["mkdir", "gooiweg"],stdout=subprocess.PIPE, universal_newlines=True)
#process=subprocess.run(["sudo","apt","install","-y","tree"],stdout=subprocess.PIPE, universal_newlines=True)
kommaarhier=process.stdout
#Manier 1 : print de hele  tekst stream
print("return code",process.returncode)
print("als tekst stream")
print(kommaarhier)
print("------------------------------------------------------------------------")

#Manier 2 : print karakter voor karakter
print("karakter voor karakter")
for i in range(len(kommaarhier)):
  print(kommaarhier[i],end="")
print("------------------------------------------------------------------------")
#Manier 3 : de string ophakken  op basis van \n
print("")
print("Ophakken in substring lijst ")
chunks=kommaarhier.split('\n')
for i in range(len(chunks)):
  print(chunks[i])
