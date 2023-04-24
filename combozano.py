import os, random
os.system('rm -rf emailtxt.txt')
name=input('name : ')


g = '@gmail.com'
for x in range(10000):
    ne=str(random.choice(name))
    print(ne+str(x)+g)
    open('emailtxt.txt', 'a').write(ne+str(x)+g+':'+ne+str(x)+'\n')
    
