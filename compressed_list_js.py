import sys

class cereal:
    def __init__(self):
        self.count = 0
        self.data = []
    def addString(self,s):
        g = s.encode("utf8")
        for x in g:
            self.data.append(x)
    def getCount(self):
        f = self.count
        self.count = self.count+1
        return f
    def toFile(self,filename):
        outfile = open(filename,"wb")
        outfile.truncate(0)
        outfile.seek(0,0)
        outfile.write(bytes(self.data))
        outfile.close()

class node:
    def __init__(self):
        self.text = ""
        self.subs = []
    def makeSub(self):
        self.subs.append(node())
    def __getitem__(self,index):
        return self.subs[index]
    def serialize(self,ce):
        num = ce.getCount()
        ce.addString("<table><tr><td>")
        if len(self.subs)!=0:
            ce.addString("<span id=\"clb-"+str(num)+"\"></span>")
        else:
            ce.addString("<input type=\"button\" value=\"#\">")
        ce.addString("</td><td>")
        if self.text[:2]!="<>":
            ce.addString("<p>")
            ce.addString(self.text)
            ce.addString("</p>")
        else:
            ce.addString(self.text[2:])
        ce.addString("</td></tr></table>")
        if len(self.subs)!=0:
            ce.addString("<table id=\"clt-"+str(num)+"\">")
            for x in self.subs:
                ce.addString("<tr><td width=\"25px\"></td><td>")
                x.serialize(ce)
                ce.addString("</td></tr>")
            ce.addString("</table>")

def save_node_to_file(filename,n,title):
    ce = cereal()
    ce.addString("<DOCTYPE html><html><head>")
    ce.addString("<script src=\"compressed_list.js\"></script>")
    ce.addString("<meta charset=\"utf-8\">")
    ce.addString("<style>input {font-family: monospace;}</style>")
    ce.addString("</head><body>")
    ce.addString("<h1>"+title+"</h1>")
    for x in n:
        x.serialize(ce)
    ce.addString("</body><script>compress_all();</script></html>")
    ce.toFile(filename)

def parseInputFile(raw):
    raw.append(10)
    ou = []
    k = []
    c = 0
    foundText = False
    for x in raw:
        if x==13:
            continue
        if x==10:
            if foundText==True:
                ou.append([c,bytes(k).decode("utf8")])
            c = 0
            k = []
            foundText = False
            continue
        if (x==9) or (x==32):
            if foundText==False:
                c = c+1
                continue
        foundText = True
        k.append(x)
    return ou

def assemble(par):
    j = [node()]
    n = [-1]
    for x in par:
        while n[-1]>=x[0]:
            j.pop()
            n.pop()
        j[-1].makeSub()
        j.append(j[-1][-1])
        n.append(x[0])
        j[-1].text = x[1]
    return j[0]

def build(infilename):
    try:
        infile = open(infilename,"rb")
    except:
        raise Exception("the specified input file does not exist")
    indata = list(infile.read())
    infile.close()
    del(infile)
    par = parseInputFile(indata)
    del(indata)
    a = assemble(par)
    del(par)
    return a.subs

def main(infilename,outfilename,title):
    b = build(infilename)
    save_node_to_file(outfilename,b,title)

if __name__=="__main__":
    if len(sys.argv)<4:
        print("not enough arguments")
        exit()
    main(sys.argv[1],sys.argv[2],sys.argv[3])
