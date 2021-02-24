#this import is necessary  in order to read
#arguments
import sys
#argument are placed in the list sys.argv[]
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:')
for i in range(len(sys.argv)):
  print("argument ", i, ":", sys.argv[i])

print("done")
