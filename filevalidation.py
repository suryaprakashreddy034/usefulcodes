import re
res="2022-03-06_1-y_1-sem_1-mid_169l_ece.csv"
file_path =["77-y_1-sem_2-mid_209l_eee.csv","4-y_1-sem_2-mid_209l_eee.csv","4-y_1-sem_2-mid_209l_ee.csv"]
valid_files=[]
invalid_files=[]
def file_validation(file_path):
    res=file_path[:-4]
    mainstr=res
    spli=res.split("_")

    years=["1-y","2-y","3-y","4-y"]
    sems=["1-sem","2-sem"]
    mids=["1-mid","2-mid"]

    depts=["ece","civil","mech","eee"]
    def yer(yaa):
        if yaa in years:
            return yaa

    def sem(yaa):
        if yaa in sems:
            return yaa
    def mid(yaa):
        if yaa in mids:
            return yaa

    def ser(yaa):
        series=yaa[:-2]
        x = re.search("^(0[1-9]|[1-9][0-9]|99)$", series)
        x=x.group()
        if str(x)+"9l" == yaa:
            return yaa
        else:
            print("student series not correct")

    def dept(yaa):
        if yaa in depts:
            return yaa



    res= (str(yer(spli[0]))+"_"+str(sem(spli[1]))+"_"+str(mid(spli[2]))+"_"+str(ser(spli[3]))+"_"+str(dept(spli[4])))
    try:
        if mainstr==res:
            valid_files.append(file_path)
        else:
            invalid_files.append(file_path)
    except:
        print("file not in correct format")
for i in file_path:
    file_validation(i)
print(valid_files)
print(invalid_files)

