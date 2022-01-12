import random
def get_forenames_surnames():
    forenames=[]
    surnames=[]

    for names,filename in ((forenames,'forenames.txt'),(surnames,'surnames.txt')):
        #print(filename)
        #print(names)
        for name in open(filename, encoding='utf8'):
            #print(name)
            names.append(name.rstrip())
    return forenames, surnames

fnames,snames = get_forenames_surnames()
fh = open('test_name.txt','w',encoding="utf8")
for i in range(100):
    line = "{0} {1}\n".format(random.choice(fnames),random.choice(snames))
    print(line)
    fh.write(line)
