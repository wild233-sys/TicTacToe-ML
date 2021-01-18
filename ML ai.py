import random
import time
train=int(input("训练次数"))
data_base={}
times=0
blackt=0
whitet=0
darwt=0
chess1=[0,0,0]
chess2=[0,0,0]
chess3=[0,0,0]
def show_result():
    global chessboard,chess1,chess2,chess3
    chess1=chessboard[0:3]
    chess2=chessboard[3:6]
    chess3=chessboard[6:9]
    print("棋局细节：")
    print(chess1)
    print(chess2)
    print(chess3)
    print("------------")
def rreset():
    global chessboard,stop,blackcho,whitecho
    chessboard=[0,0,0,0,0,0,0,0,0]
    stop=0
    blackcho={}
    whitecho={}
rreset()
def result():
    global chessboard,stop
    board = [(0,1,2), (3,4,5), (6,7,8),(0,3,6), (1,4,7), (2,5,8),(0,4,8), (2,4,6)]
    for i in board:
        win=0
        for ii in i:
            win=win+chessboard[ii]
        if win==3:
            print("black win")
            stop=1
            return 1
        if win==-3:
            print("white win")
            stop=1
            return -1
    if 0 not in chessboard:
        print("darw")
        stop=1
        return 0
    return "keep"
def defult(chessboard):
    defultt=[]
    can=get_index1(chessboard,0)
    for i in range(0,9):
        if i in can:
            defultt.append(20)
        if i not in can:
            defultt.append(0)
    return defultt
def randcho(data):
    chooslist=[]
    weight=data[str(chessboard)]
    for v,i in enumerate(list(weight)):
        for ii in range(int(i)):
            chooslist.append(v)
    return chooslist
def ai_black():
    global data_base,blackcho,chessboard
    if str(chessboard) not in data_base:
        data_base[str(chessboard)]=defult(chessboard)
    try:
        chooslist=randcho(data_base)
    except:
        return (chessboard.index(0),1)
    list=get_index1(chessboard,0)
    if len(list)==0:
        return "darw"
    choose=random.choice(chooslist)
    blackcho[str(chessboard)] = str(choose)
    return (choose,1)
def ai_white():
    global data_base,whitecho,chessboard
    if str(chessboard) not in data_base:
        data_base[str(chessboard)]=defult(chessboard)
    try:
        chooslist=randcho(data_base)
    except:
        return (chessboard.index(0),-1)
    list=get_index1(chessboard,0)
    if len(list)==0:
        return "darw"
    choose=random.choice(chooslist)
    whitecho[str(chessboard)] = str(choose)
    return (choose,-1)
def play(x):
    if x=="darw":
        return
    chessboard[int(x[0])]=x[1]
def get_index1(lst=None, item=''):
    tmp = []
    tag = 0
    for i in lst:
        if i == item:
            tmp.append(tag)
        tag += 1
    return tmp
def endding():
    global times,darwt,blackt,whitet,data_base,blackcho,whitecho
    ending=result()
    if ending==0:
            darwt=darwt+1
            times=times+1
            show_result()
            for i in blackcho:
                target=data_base[i]
                target[int(blackcho[i])]=str(int(target[int(blackcho[i])])+1)
                data_base[i]=target
            for i in whitecho:
                target=data_base[i]
                target[int(whitecho[i])]=str(int(target[int(whitecho[i])])+1)
                data_base[i]=target
    elif ending==1:
            blackt=blackt+1
            times=times+1
            show_result()
            for i in blackcho:
                target=data_base[i]
                target[int(blackcho[i])]=str(int(target[int(blackcho[i])])+2)
                data_base[i]=target
            for i in whitecho:
                target=data_base[i]
                target[int(whitecho[i])]=str(int(target[int(whitecho[i])])-2)
                data_base[i]=target
    elif ending==-1:
            whitet=whitet+1
            times=times+1
            show_result()
            for i in blackcho:
                target=data_base[i]
                target[int(blackcho[i])]=str(int(target[int(blackcho[i])])-2)
                data_base[i]=target
            for i in whitecho:
                target=data_base[i]
                target[int(whitecho[i])]=str(int(target[int(whitecho[i])])+2)
                data_base[i]=target
while True:
    if stop==0:
        try:
            play(ai_black())
        except:
            chessboard[int(chessboard.index(0))]=1
        endding()
        if stop==0:
            try:
                play(ai_white())
            except:
                chessboard[int(chessboard.index(0))]=-1
            endding()
    if stop==1:
        rreset()
        if times//train==times/train:
            print("运行了 "+str(times)+" 次，其中黑方获胜 "+str(blackt)+" 次，白方获胜 "+str(whitet)+" 次，平局 "+str(darwt))
            train=int(input("训练次数"))
            if int(input("输入1观看数据库： "))==1:
                print ((data_base))
                input("ML ai.py")
            time.sleep(1)  
