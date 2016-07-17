from file import function

sampleList = [1,2,3,4,5,6,7,8]
print (sampleList[1])

myTuple = (1,2,3)
myList = list(myTuple)
myList.append(4)
print (myList)

a = 1
while a < 10:
    print (a)
    a+=1

for a in range(1,3):
    print (a)

a = 20
if a >= 22:
    print("if")
elif a >= 21:
    print("elif")
else:
    print("else")

myExample = {'someItem': 2, 'otherItem': 20}
print(myExample['otherItem'])
myExample['newItem'] = 400

var1 = '1'
try:
 var2 = var1 + 1 # since var1 is a string, it cannot be added to the number 1
except:
 var2 = int(var1) + 1
print(var2)

#   [^#\w\s]    grabs punctuation

#   #[\w\s]+    grabs hashtags

#   \d+\snotes    grabs notes

f = open("test.txt", "r") #opens file with name of "test.txt"

f = open("test.txt", "w") #opens file with name of "test.txt"

file.readline(n)
file.read(n)

f = open("test.txt","w") #opens file with name of "test.txt"
file.write("I am a test file.")
file.write("Maybe someday, he will promote me to a real file.")
file.write("Man, I long to be a real file")
file.close()

os.path.isdir(path)
Return True if path is an existing directory. This follows symbolic links, so both islink() and isdir() can be true for the same path.
