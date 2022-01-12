import random
fnames = []
snames = []
for f in open("forenames.txt"):
    fnames.append(f.strip())
for f in open("surnames.txt"):
   snames.append(f.strip())
fh = open('test_name.txt','w',encoding="utf8")
for i in range(100):
    line = "{0} {1}".format(random.choice(fnames),random.choice(snames))
    print(line)
    fh.write(line)
