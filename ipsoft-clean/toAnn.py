import os

all_folders = os.listdir("./")
all_files = []

for f in [f for f in all_folders if os.path.isdir(f)]:
    files = [f+"/"+fi for fi in os.listdir(f)]
    anns = []

    for fi in [fi for fi in files if ".ann" in fi]:
        d = [l for l in open(fi)]
        for l in d:
            try:
                inst = l.split()[0]
                sent = l.split()[1]
                word = l.split()[2]
                verb = l.split()[3]
                if not verb.endswith("-v"):
                    verb += "-v"
                tag = l.split()[4]
                anns.append(" ".join([inst, sent, word, verb, tag]) + "\n")
            except:
                print f + " : " + l
        
    output = open(f + "/" + f + ".ann", "w")
    output.writelines(anns)
    output.close()
