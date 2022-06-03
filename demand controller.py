# Duration 8 Hr
# 38500 BTU
# EER 21.5
# 1790 Wt
# T=Ce⁻ᵏᵗ+Tₐ

import math
from turtle import position
import matplotlib.pyplot as plt
import time
import paho.mqtt.client as paho


broker = "test.mosquitto.org"
port = 1883
def on_publish(client,userdata,result):             #create function for callback
    #print("data published \n")
    pass

def on_message(client, userdata, message):
    global temp1,temp2,sw
    AppPayload = str(message.payload.decode("utf-8"))
    AppTopic = message.topic
    #print(AppTopic)
    if AppTopic == "/switch/main":
        if AppPayload == "True":
            sw = 1  # เปิดswitch = 1
            print("ON")
        if AppPayload == "False":
            sw = 2  # ปิดswitch = 2
            print("OFF")
    if AppTopic == "/con/temperature1":
        temp1 = int(AppPayload)
        #print("Temperature %d" % temp)
    if AppTopic == "/con/temperature2":
        temp2 = int(AppPayload)
        #print("Temperature %d" % temp2)

client = paho.Client("")
client.on_publish = on_publish  # When this program connect to MQTT Broker successfully
client.on_message = on_message  # When device publish MATCHED subscribed topics
client.connect(broker,port)
client.loop_start() # Start the loop
client.subscribe("/con/temperature1")
client.subscribe("/con/temperature2")
client.subscribe("/switch/main")


Te = 31
tk = 120
td = 180  # time in k term
e = []
h = [0]
Tee = 20

M = 60
Icl = 0.5
V = 0.2
Tcl = 35.7
Fcl = 0.5
Ps = 23.8

rpmv1 = []
rpmv2 = []

present = []
predic = []
sw = 0
temp1 = []
temp2 = []

while True:
    if sw == 2:
        def Room(x, y, setT):
            T2 = [setT - 2.5]
            T = [x, y, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x]
            pog = []
            pog2 = []
            pog.append(x)
            pog2.append(y)
            pog3 = []
            pog3.append(x)
            pog4 = []
            pog5 = []
            pog6 = []
            pog7 = []
            pog8 = []
            pog9 = []
            pog10 = []
            pog11 = []
            pog12 = []
            pog13 = []
            pog14 = []
            pog15 = []
            pog16 = []
            pog17 = []
            pog18 = []
            pog19 = []
            pog20 = []
            pog21 = []
            pog22 = []
            pog23 = []
            pog24 = []
            pog25 = []
            pog4.append(x)
            pog5.append(x)
            pog6.append(x)
            pog7.append(x)
            pog8.append(x)
            pog9.append(x)
            pog10.append(x)
            pog11.append(x)
            pog12.append(x)
            pog13.append(x)
            pog14.append(x)
            pog15.append(x)
            pog16.append(x)
            pog17.append(x)
            pog18.append(x)
            pog19.append(x)
            pog20.append(x)
            pog21.append(x)
            pog22.append(x)
            pog23.append(x)
            pog24.append(x)
            pog25.append(x)
            sig = 0
            PMVroom1=[]
            PMVroom2=[]
            PMVroom3=[]
            PMVroom4=[]
            PMVroom5=[]
            PMVroom6=[]
            PMVroom7=[]
            PMVroom8=[]
            PMVroom9=[]
            PMVroom10=[]
            PMVroom11=[]
            PMVroom12=[]
            PMVroom13=[]
            PMVroom14=[]
            PMVroom15=[]
            PMVroom16=[]
            PMVroom17=[]
            PMVroom18=[]
            PMVroom19=[]
            PMVroom20=[]
            PMVroom21=[]
            PMVroom22=[]
            PMVroom23=[]
            PMVroom24=[]
            PMVroom25=[]
            newPMV = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            humi = [60]
            Airstr = [720, 720, 360, 360, 1080, 1080, 2520, 2520, 1080, 1080, 1080, 1080, 1080, 1080, 1, 1, 1, 1, 1, 1, 2360,
                      2360, 2360, 1, 1]
            Airend = [2160, 2160, 2160, 2160, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 2160, 2160, 3600,
                      3600, 2160, 2160, 4319, 4319, 4319, 4319, 4319]
            timer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ontime = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            durat = 4320  # scale1:6 24hr = 1440 min 12hr = 720
            count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0]  # ตอนสลับ count = 0 เสมอ จะได้ Temp เดิมมาคำนวณหลังจากสลับ
            power = 3580
            power1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ppower = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            tpower = []  # power ที่เวลาต่างๆ
            gpower = []  # power ที่เวลาต่างๆหลังโดนตัด
            Etts = [0]
            E = [0]
            Ep = [0]
            Emin = 40000
            D = 10
            n = [5]
            Ts = D / n[0]
            Emax = 300000
            violationcount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            loadcutcount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            loadcuttime = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            Threshold = [0, 0]  # setting ระดับเทรชโชวก่อนตัดโหลดตัวแรกหรือคืนโหลดตัวแรก
            delay_flag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            delay_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            Time1 = 30  # Tmoff minimun
            Time2 = 60  # Tmoff maximun
            Time3 = 60  # Tm on minimum
            prior_flag = 0
            PMV = [0, 5, 3, 6, 7, 2]
            largest = -100

            def decrease_temp():
                T10 = T[i] - 2.5
                C = T[i] - Tee
                k = (math.log((T10 - Tee) / (T[i] - Tee)) / td) * -1
                Tnew = Tee + C * (math.exp(-k * count[i]))
                # print("decrease1 = ", Tnew)
                newcount = 0  # เอาไว้ยัดค่า 0 ลงไปใน count
                if Tnew < (setT - 2.5):  # ปรับเพดานของ temp เพื่อสลับเป้น increase
                    T[i] = Tnew
                    count[i] = newcount
                if i == 0:
                    if timer[0] == Airend[0]:
                        T[0] = pog[timer[0]]
                    timer[0] += 1
                    pog.append(Tnew)
                if i == 1:
                    if timer[1] == Airend[1]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[1] = pog2[timer[1]]
                    timer[1] += 1
                    pog2.append(Tnew)
                if i == 2:
                    if timer[2] == Airend[2]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[2] = pog3[timer[2]]
                    timer[2] += 1
                    pog3.append(Tnew)
                if i == 3:
                    if timer[3] == Airend[3]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[3] = pog4[timer[3]]
                    timer[3] += 1
                    pog4.append(Tnew)
                if i == 4:
                    if timer[4] == Airend[4]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[4] = pog5[timer[4]]
                    timer[4] += 1
                    pog5.append(Tnew)
                if i == 5:
                    if timer[5] == Airend[5]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[5] = pog6[timer[5]]
                    timer[5] += 1
                    pog6.append(Tnew)
                if i == 6:
                    if timer[6] == Airend[6]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[6] = pog7[timer[6]]
                    timer[6] += 1
                    pog7.append(Tnew)
                if i == 7:
                    if timer[7] == Airend[7]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[7] = pog8[timer[7]]
                    timer[7] += 1
                    pog8.append(Tnew)
                if i == 8:
                    if timer[8] == Airend[8]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[8] = pog9[timer[8]]
                    timer[8] += 1
                    pog9.append(Tnew)
                if i == 9:
                    if timer[9] == Airend[9]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[9] = pog10[timer[9]]
                    timer[9] += 1
                    pog10.append(Tnew)
                if i == 10:
                    if timer[10] == Airend[10]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[10] = pog11[timer[10]]
                    timer[10] += 1
                    pog11.append(Tnew)
                if i == 11:
                    if timer[11] == Airend[11]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[11] = pog12[timer[11]]
                    timer[11] += 1
                    pog12.append(Tnew)
                if i == 12:
                    if timer[12] == Airend[12]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[12] = pog13[timer[12]]
                    timer[12] += 1
                    pog13.append(Tnew)
                if i == 13:
                    if timer[13] == Airend[13]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[13] = pog14[timer[13]]
                    timer[13] += 1
                    pog14.append(Tnew)
                if i == 14:
                    if timer[14] == Airend[14]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[14] = pog15[timer[14]]
                    timer[14] += 1
                    pog15.append(Tnew)
                if i == 15:
                    if timer[15] == Airend[15]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[15] = pog16[timer[15]]
                    timer[15] += 1
                    pog16.append(Tnew)
                if delay_flag[16] == 1:
                    if i == 16:
                        T[16] = pog17[timer[16]]
                if i == 16:
                    #print("decrease1 = ", Tnew)
                    #print('ti',T[i])
                    if timer[16] == Airend[16]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[16] = pog17[timer[16]]
                    timer[16] += 1
                    pog17.append(Tnew)
                if i == 17:
                    if timer[17] == Airend[17]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[17] = pog18[timer[17]]
                    timer[17] += 1
                    pog18.append(Tnew)
                if i == 18:
                    if timer[18] == Airend[18]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[18] = pog19[timer[18]]
                    timer[18] += 1
                    pog19.append(Tnew)
                if i == 19:
                    if timer[19] == Airend[19]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[19] = pog20[timer[19]]
                    timer[19] += 1
                    pog20.append(Tnew)
                if i == 20:
                    if timer[20] == Airend[20]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[20] = pog21[timer[20]]
                    timer[20] += 1
                    pog21.append(Tnew)
                if i == 21:
                    if timer[21] == Airend[21]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[21] = pog22[timer[21]]
                    timer[21] += 1
                    pog22.append(Tnew)
                if i == 22:
                    if timer[22] == Airend[22]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[22] = pog23[timer[22]]
                    timer[22] += 1
                    pog23.append(Tnew)
                if i == 23:
                    if timer[23] == Airend[23]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[23] = pog24[timer[23]]
                    timer[23] += 1
                    pog24.append(Tnew)
                if i == 24:
                    if timer[24] == Airend[24]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[24] = pog25[timer[24]]
                    timer[24] += 1
                    pog25.append(Tnew)

            def increase_temp():
                T10 = setT + 2.5
                C = T[i] - Te
                k = (math.log((T10 - Te) / (T[i] - Te)) / tk) * -1
                # print('count', count[1])
                Tnew = Te + C * (math.exp(-k * count[i]))
                # print('T1ที่ใช้=', T[1])
                newcount = 0
                # print("T10:",T10)
                # print("setT",setT)
                #print("increase1 = ", Tnew)
                # print('T[0]',T[0])
                if Tnew > (setT + 2):  # ปรับเพดานของ temp เพื่อสลับเป็น decrease
                    # print('T1ที่ใช้ ตอน 1=', T[1])
                    T[i] = Tnew
                    # print('T1ที่ใช้ ตอน 2=', T[1])
                    count[i] = newcount
                if i == 0:
                    if timer[0] == Airend[0]:
                        T[0] = pog[timer[0]]
                    timer[0] += 1
                    pog.append(Tnew)
                if i == 1:
                    if timer[1] == Airend[1]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        # print('T0ที่ใช้ ตอน 2=', T[0])
                        # print('T1ที่ใช้ ตอน 2=', T[1])
                        T[1] = pog2[timer[1]]
                    timer[1] += 1
                    pog2.append(Tnew)
                if i == 2:
                    if timer[2] == Airend[2]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        # print('T0ที่ใช้ ตอน 2=', T[0])
                        # print('T1ที่ใช้ ตอน 2=', T[1])
                        T[2] = pog3[timer[2]]
                    timer[2] += 1
                    pog3.append(Tnew)
                if i == 3:
                    if timer[3] == Airend[3]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        # print('T0ที่ใช้ ตอน 2=', T[0])
                        # print('T1ที่ใช้ ตอน 2=', T[1])
                        T[3] = pog4[timer[3]]
                    timer[3] += 1
                    pog4.append(Tnew)
                if i == 4:
                    if timer[4] == Airend[4]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        # print('T0ที่ใช้ ตอน 2=', T[0])
                        # print('T1ที่ใช้ ตอน 2=', T[1])
                        T[4] = pog5[timer[4]]
                    timer[4] += 1
                    pog5.append(Tnew)
                if i == 5:
                    if timer[5] == Airend[5]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        # print('T0ที่ใช้ ตอน 2=', T[0])
                        # print('T1ที่ใช้ ตอน 2=', T[1])
                        T[5] = pog6[timer[5]]
                    timer[5] += 1
                    pog6.append(Tnew)
                if i == 6:
                    if timer[6] == Airend[6]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        # print('T0ที่ใช้ ตอน 2=', T[0])
                        # print('T1ที่ใช้ ตอน 2=', T[1])
                        T[6] = pog7[timer[6]]
                    timer[6] += 1
                    pog7.append(Tnew)
                if i == 7:
                    if timer[7] == Airend[7]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        # print('T0ที่ใช้ ตอน 2=', T[0])
                        # print('T1ที่ใช้ ตอน 2=', T[1])
                        T[7] = pog8[timer[7]]
                    timer[7] += 1
                    pog8.append(Tnew)
                if i == 8:
                    if timer[8] == Airend[8]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        # print('T0ที่ใช้ ตอน 2=', T[0])
                        # print('T1ที่ใช้ ตอน 2=', T[1])
                        T[8] = pog9[timer[8]]
                    timer[8] += 1
                    pog9.append(Tnew)
                if i == 9:
                    if timer[9] == Airend[9]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        # print('T0ที่ใช้ ตอน 2=', T[0])
                        # print('T1ที่ใช้ ตอน 2=', T[1])
                        T[9] = pog10[timer[9]]
                    timer[9] += 1
                    pog10.append(Tnew)
                if i == 10:
                    if timer[10] == Airend[10]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[10] = pog11[timer[10]]
                    timer[10] += 1
                    pog11.append(Tnew)
                if i == 11:
                    if timer[11] == Airend[11]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[11] = pog12[timer[11]]
                    timer[11] += 1
                    pog12.append(Tnew)
                if i == 12:
                    if timer[12] == Airend[12]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[12] = pog13[timer[12]]
                    timer[12] += 1
                    pog13.append(Tnew)
                if i == 13:
                    if timer[13] == Airend[13]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[13] = pog14[timer[13]]
                    timer[13] += 1
                    pog14.append(Tnew)
                if i == 14:
                    if timer[14] == Airend[14]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[14] = pog15[timer[14]]
                    timer[14] += 1
                    pog15.append(Tnew)
                if i == 15:
                    if timer[15] == Airend[15]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[15] = pog16[timer[15]]
                    timer[15] += 1
                    pog16.append(Tnew)
                if i == 16:
                    #print("increase1 = ", Tnew)
                    if timer[16] == Airend[16]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[16] = pog17[timer[16]]
                    timer[16] += 1
                    pog17.append(Tnew)
                if i == 17:
                    if timer[17] == Airend[17]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[17] = pog18[timer[17]]
                    timer[17] += 1
                    pog18.append(Tnew)
                if i == 18:
                    if timer[18] == Airend[18]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[18] = pog19[timer[18]]
                    timer[18] += 1
                    pog19.append(Tnew)
                if i == 19:
                    if timer[19] == Airend[19]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[19] = pog20[timer[19]]
                    timer[19] += 1
                    pog20.append(Tnew)
                if i == 20:
                    if timer[20] == Airend[20]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[20] = pog21[timer[20]]
                    timer[20] += 1
                    pog21.append(Tnew)
                if i == 21:
                    if timer[21] == Airend[21]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[21] = pog22[timer[21]]
                    timer[21] += 1
                    pog22.append(Tnew)
                if i == 22:
                    if timer[22] == Airend[22]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[22] = pog23[timer[22]]
                    timer[22] += 1
                    pog23.append(Tnew)
                if i == 23:
                    if timer[23] == Airend[23]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[23] = pog24[timer[23]]
                    timer[23] += 1
                    pog24.append(Tnew)
                if i == 24:
                    if timer[24] == Airend[24]:  # ตอนเปลี่ยน def ให้ทำการ save ค่า temp ล่าสุดไว้
                        T[24] = pog25[timer[24]]
                    timer[24] += 1
                    pog25.append(Tnew)

            def increase_temp2():
                T10 = setT + 2.5
                C = (setT - 2.5) - Te
                k = (math.log((T10 - Te) / (setT - 2.5 - Te)) / tk) * -1
                h[0] = 0
                Tnew = Te + C * (math.exp(-k * h[0]))
                # print('Tnew',Tnew)
                if delay_flag[0] == 1:
                    if i == 0:
                        T[0] = pog[timer[0]]
                if delay_flag[1] == 1:
                    if i == 1:
                        T[1] = pog2[timer[1]]
                if delay_flag[2] == 1:
                    if i == 2:
                        T[2] = pog3[timer[2]]
                if delay_flag[3] == 1:
                    if i == 3:
                        T[3] = pog4[timer[3]]
                if delay_flag[4] == 1:
                    if i == 4:
                        T[4] = pog5[timer[4]]
                if delay_flag[5] == 1:
                    if i == 5:
                        T[5] = pog6[timer[5]]
                if delay_flag[6] == 1:
                    if i == 6:
                        T[6] = pog7[timer[6]]
                if delay_flag[7] == 1:
                    if i == 7:
                        T[7] = pog8[timer[7]]
                if delay_flag[8] == 1:
                    if i == 8:
                        T[8] = pog9[timer[8]]
                if delay_flag[9] == 1:
                    if i == 9:
                        T[9] = pog10[timer[9]]
                if delay_flag[10] == 1:
                    if i == 10:
                        T[10] = pog11[timer[10]]
                if delay_flag[11] == 1:
                    if i == 11:
                        T[11] = pog12[timer[11]]
                if delay_flag[12] == 1:
                    if i == 12:
                        T[12] = pog13[timer[12]]
                if delay_flag[13] == 1:
                    if i == 13:
                        T[13] = pog14[timer[13]]
                if delay_flag[14] == 1:
                    if i == 14:
                        T[14] = pog15[timer[14]]
                if delay_flag[15] == 1:
                    if i == 15:
                        T[15] = pog16[timer[15]]
                if delay_flag[16] == 1:
                    if i == 16:
                        T[16] = pog17[timer[16]]
                if delay_flag[17] == 1:
                    if i == 17:
                        T[17] = pog18[timer[17]]
                if delay_flag[18] == 1:
                    if i == 18:
                        T[18] = pog19[timer[18]]
                if delay_flag[19] == 1:
                    if i == 19:
                        T[19] = pog20[timer[19]]
                if delay_flag[20] == 1:
                    if i == 20:
                        T[20] = pog21[timer[20]]
                if delay_flag[21] == 1:
                    if i == 21:
                        T[21] = pog22[timer[21]]
                if delay_flag[22] == 1:
                    if i == 22:
                        T[22] = pog23[timer[22]]
                if delay_flag[23] == 1:
                    if i == 23:
                        T[23] = pog24[timer[23]]
                if delay_flag[24] == 1:
                    if i == 24:
                        T[24] = pog25[timer[24]]

                while Tnew <= T[i]:
                    h[0] = h[0] + 1
                    Tnew = Te + C * (math.exp(-k * h[0]))
                T[i] = Tnew
                if i == 0:
                    timer[0] += 1
                    pog.append(Tnew)
                if i == 1:
                    timer[1] += 1
                    pog2.append(Tnew)
                if i == 2:
                    timer[2] += 1
                    pog3.append(Tnew)
                if i == 3:
                    timer[3] += 1
                    pog4.append(Tnew)
                if i == 4:
                    timer[4] += 1
                    pog5.append(Tnew)
                if i == 5:
                    timer[5] += 1
                    pog6.append(Tnew)
                if i == 6:
                    timer[6] += 1
                    pog7.append(Tnew)
                if i == 7:
                    timer[7] += 1
                    pog8.append(Tnew)
                if i == 8:
                    timer[8] += 1
                    pog9.append(Tnew)
                if i == 9:
                    timer[9] += 1
                    pog10.append(Tnew)
                if i == 10:
                    timer[10] += 1
                    pog11.append(Tnew)
                if i == 11:
                    timer[11] += 1
                    pog12.append(Tnew)
                if i == 12:
                    timer[12] += 1
                    pog13.append(Tnew)
                if i == 13:
                    timer[13] += 1
                    pog14.append(Tnew)
                if i == 14:
                    timer[14] += 1
                    pog15.append(Tnew)
                if i == 15:
                    timer[15] += 1
                    pog16.append(Tnew)
                if i == 16:
                    #print("increase2 = ", Tnew)
                    #print('ti',T[i])
                    timer[16] += 1
                    pog17.append(Tnew)
                if i == 17:
                    timer[17] += 1
                    pog18.append(Tnew)
                if i == 18:
                    timer[18] += 1
                    pog19.append(Tnew)
                if i == 19:
                    timer[19] += 1
                    pog20.append(Tnew)
                if i == 20:
                    timer[20] += 1
                    pog21.append(Tnew)
                if i == 21:
                    timer[21] += 1
                    pog22.append(Tnew)
                if i == 22:
                    timer[22] += 1
                    pog23.append(Tnew)
                if i == 23:
                    timer[23] += 1
                    pog24.append(Tnew)
                if i == 24:
                    timer[24] += 1
                    pog25.append(Tnew)
                # print('increase2 =', Tnew)

            def predict():
                a = 0
                b = 0
                for k in range(0, n[0]):  # ช่วง 1 -> n + 1
                    a += (tpower[timer[i] - (k + 1)] + tpower[timer[i] - (k)]) / 2
                Etts[0] = a * 2
                for m in range(0, n[0]):
                    b += tpower[timer[i] - m]
                E[0] = b * Ts
                Ep[0] = (2 * E[0]) - Etts[0]
                # print('อดีต', Etts[0])
                # print('ปัจจุบัน', E[0])
                # print('อนาคต', Ep[0])
                # print(tpower[time[i]])
                # print(tpower[(time[i]) - 1])
                # print(tpower[(time[i]) - 2])
                # print(tpower[(time[i]) - 3])
                # print(tpower[(time[i]) - 4])
                # print(tpower[(time[i]) - 5])
                # print(tpower[(time[i]) - 6])

            def predict2():
                a = 0
                b = 0
                for k in range(0, n[0]):  # ช่วง 1 -> n + 1
                    a += (ppower[(timer[24] - 1) - (k + 1)] + ppower[(timer[24] - 1) - (k)]) / 2
                Etts[0] = a * 2
                for m in range(0, n[0]):
                    b += ppower[(timer[24] - 1) - m]
                E[0] = b * Ts
                Ep[0] = (2 * E[0]) - Etts[0]
                # print('อดีต', Etts[0])
                # print('ปัจจุบัน', E[0])
                # print('อนาคต', Ep[0])
                # print(ppower[(time[9]-1) - (0)])
                # print(ppower[(time[9]-1) - (1)])
                # print(ppower[(time[9]-1) - (2)])
                # print(ppower[(time[9]-1) - (3)])
                # print(ppower[(time[9]-1) - (4)])
                # print(ppower[(time[9]-1) - (5)])
                # print(ppower[(time[9]-1) - (6)])

            # Calculate
            while timer[24] <= durat:
                print("Time in sec =  ", timer[24])
                cpower = power1[0] + power1[1] + power1[2] + power1[3] + power1[4] + power1[5] + power1[6] + power1[7] + power1[
                    8] + power1[9] + power1[10] + power1[11] + power1[12] + power1[13] + power1[14] + power1[15] + power1[16] + \
                         power1[17] + power1[18] + power1[19] + power1[20] + power1[21] + power1[22] + power1[23] + power1[24]
                tpower.append(cpower)
                # print('tpow',tpower[time[24]])
                if timer[24] >= 6 and timer[24]%6==0:
                    predict()
                    if E[0] > Emax:  # เช็คค่า violation ค่าที่มากสุดจะอยู่ที่ violation[0]
                        violationcount[1] = E[0] - Emax
                        if E[0] - Emax > violationcount[0]:
                            violationcount[0] = violationcount[1]

                for i in range(25):
                    sig = 0  # ไม่ให้ tpower append ซ้ำ2รอบใน1time
                    if 0 <= i < 25:
                        # print('ห้อง101')
                        calPog = [pog[timer[i]], pog2[timer[i]], pog3[timer[i]], pog4[timer[i]], pog5[timer[i]], pog6[timer[i]], pog7[timer[i]], pog8[timer[i]], pog9[timer[i]], pog10[timer[i]], pog11[timer[i]], pog12[timer[i]], pog13[timer[i]], pog14[timer[i]],
                                  pog15[timer[i]],
                                  pog16[timer[i]], pog17[timer[i]], pog18[timer[i]], pog19[timer[i]], pog20[timer[i]],
                                  pog21[timer[i]],
                                  pog22[timer[i]], pog23[timer[i]], pog24[timer[i]], pog25[timer[i]]]
                        Ta = calPog[i]
                        Tmrt = calPog[i]
                        Rh = humi[0]
                        Pv = (Ps * Rh) / 100
                        hc = 0

                        if 2.38 * math.pow(Tcl - Ta, 0.25) > 10.4 * math.sqrt(V):
                            hc = 2.05 * math.pow(Tcl - Ta, 0.25)
                        else:
                            hc = 10.4 * math.sqrt(V)

                        PMV = (0.325 * math.exp(-0.042 * M) + 0.032) * (M - (0.35 * (43 - 0.061 * M - Pv)) - (0.42 * (M - 50)) -
                                                                        (0.0023 * M * (44 - Pv)) - (0.0014 * M * (34 - Ta)) - (
                                                                                3.4 * math.pow(10, -8) * Fcl *
                                                                                (math.pow(Tcl + 273, 4) - math.pow(Tmrt + 273,
                                                                                                                   4))) - (
                                                                                Fcl * hc * (Tcl - Ta)))
                        newPMV[i] = PMV
                        if i == 0:
                            PMVroom1.append(PMV)
                        if i == 1:
                            PMVroom2.append(PMV)
                        if i == 2:
                            PMVroom3.append(PMV)
                        if i == 3:
                            PMVroom4.append(PMV)
                        if i == 4:
                            PMVroom5.append(PMV)
                        if i == 5:
                            PMVroom6.append(PMV)
                        if i == 6:
                            PMVroom7.append(PMV)
                        if i == 7:
                            PMVroom8.append(PMV)
                        if i == 8:
                            PMVroom9.append(PMV)
                        if i == 9:
                            PMVroom10.append(PMV)
                        if i == 10:
                            PMVroom11.append(PMV)
                        if i == 11:
                            PMVroom12.append(PMV)
                        if i == 12:
                            PMVroom13.append(PMV)
                        if i == 13:
                            PMVroom14.append(PMV)
                        if i == 14:
                            PMVroom15.append(PMV)
                        if i == 15:
                            PMVroom16.append(PMV)
                        if i == 16:
                            PMVroom17.append(PMV)
                        if i == 17:
                            PMVroom18.append(PMV)
                        if i == 18:
                            PMVroom19.append(PMV)
                        if i == 19:
                            PMVroom20.append(PMV)
                        if i == 20:
                            PMVroom21.append(PMV)
                        if i == 21:
                            PMVroom22.append(PMV)
                        if i == 22:
                            PMVroom23.append(PMV)
                        if i == 23:
                            PMVroom24.append(PMV)
                        if i == 24:
                            PMVroom25.append(PMV)

                        if delay_flag[i] == 1:  # delay เวลา 100 ขั้นต่ำ
                            if delay_count[i] < Time1:
                                increase_temp2()
                                power1[i] = 0
                                count[i] = 0
                                delay_count[i] += 1
                                loadcuttime[i] += 1
                                # print('delay')
                            elif delay_count[i] >= Time1 and delay_count[i] <= Time2:
                                if Ep[0] < Emin and Airstr[i] <= timer[i] <= Airend[i]:
                                    delay_flag[i] = 2
                                    #print('คืนโหลดห้องที่ : ', i)
                                    delay_count[i] = 0
                                    if T[i] < (setT - 2):
                                        increase_temp()
                                        count[i] = count[i] + 1
                                        power1[i] = power / 2
                                    else:
                                        decrease_temp()
                                        ontime[i] += 1
                                        count[i] = count[i] + 1
                                        power1[i] = power / 2
                                else:
                                    # print('++++++++++++++++คืนโหลดไม่สำเร็จ++++++++++++++')
                                    increase_temp2()
                                    power1[i] = 0
                                    loadcuttime[i] += 1
                                    count[i] = 0
                                if delay_count[i] == Time2:
                                    delay_flag[i] = 2
                                    #print('คืนโหลดห้องที่ : ', i)
                                    delay_count[i] = 0
                                delay_count[i] += 1
                        elif delay_flag[i] == 2:  # หลัง delay ห้ามโดนตัดอีก ในเวลา 150
                            if delay_count[i] < Time3:
                                # print('delay = 2')
                                delay_count[i] += 1
                                if Airstr[i] <= timer[i] <= Airend[i]:
                                    #print('ทำงานปกติห้องที่ : ', i)
                                    if T[i] < (setT - 2):
                                        increase_temp()
                                        count[i] = count[i] + 1
                                        power1[i] = power / 2
                                    else:
                                        decrease_temp()
                                        ontime[i] += 1
                                        count[i] = count[i] + 1
                                        power1[i] = power / 2
                                else:
                                    # print('ยังไม่ทำงาน')
                                    increase_temp2()
                                    power1[i] = 0
                            if delay_count[i] >= Time3:
                                delay_flag[i] = 0
                                delay_count[i] = 0
                        else:
                            if Airstr[i] <= timer[i] <= Airend[i]:
                                #print('ทำงานปกติห้องที่ : ', i)
                                if T[i] < (setT - 2):
                                    increase_temp()
                                    count[i] = count[i] + 1
                                    power1[i] = power / 2
                                else:
                                    decrease_temp()
                                    ontime[i] += 1
                                    count[i] = count[i] + 1
                                    power1[i] = power / 2
                            else:
                                increase_temp2()
                                power1[i] = 0
                if timer[24] >= 7:
                    ppower[0] = tpower[0]
                    ppower[1] = tpower[1]
                    ppower[2] = tpower[2]
                    ppower[3] = tpower[3]
                    ppower[4] = tpower[4]
                    ppower[5] = tpower[5]
                    ppower[6] = tpower[6]
                    ppower[timer[24] - 1] = tpower[timer[24] - 1]
                    cpower = power1[0] + power1[1] + power1[2] + power1[3] + power1[4] + power1[5] + power1[6] + power1[7] + \
                             power1[8] + power1[9] + power1[10] + power1[11] + power1[12] + power1[13] + power1[14] + \
                             power1[15] + power1[16] + power1[17] + power1[18] + power1[19] + power1[20] + power1[21] + \
                             power1[22] + power1[23] + power1[24]
                    # print('cpow2',cpower)
                    ppower[timer[24] - 1] = cpower
                    ppower.append(0)
                    kk=0 # ให้ตัดทีละตัว
                    xd = newPMV
                    yd = sorted(enumerate(xd), key = lambda i : i[1])
                    #print(yd)
                    jj=0
                    i=0
                    while kk==0 and Ep[0] > Emax:  # ตัดโหลดตรงนี้ ตัดทีตัว ตัดตาม pmv
                        #predict2()
                        #print('d')
                        if i==yd[jj][0]:
                            #print('a')
                            if yd[jj][1]>0.5:
                                #print('s')
                                kk=1
                            elif delay_flag[i] ==0:
                                #print('f')
                                if Airstr[i] <= timer[i] <= Airend[i] and kk==0 and yd[jj][1]<=0.5:
                                    #print('k')
                                    #print('ตัดโหลดห้องที่ : ', i)
                                    delay_flag[i] = 1
                                    power1[i] = 0
                                    kk=1
                                    loadcutcount[i] += 1
                                else:
                                    kk=1
                            elif yd[jj][0] == 24:
                                kk=1
                            else:
                                #print('j')
                                jj+=1
                                i=0
                        else:
                            i+=1
                    if 1070 < timer[i] < 2200:
                        print('Status = 0 "ทำงานปกติ"')
                        print('Status = 1 "ตัดโหลด"')
                        print('Status = 2 "คืนโหลด"')
                        print('ห้องที่ 1  : ', delay_flag[0])
                        print('ห้องที่ 2  : ', delay_flag[1])
                        print('ห้องที่ 3  : ', delay_flag[2])
                        print('ห้องที่ 4  : ', delay_flag[3])
                        print('ห้องที่ 5  : ', delay_flag[4])
                        print('ห้องที่ 6  : ', delay_flag[5])
                        print('ห้องที่ 7  : ', delay_flag[6])
                        print('ห้องที่ 8  : ', delay_flag[7])
                        print('ห้องที่ 9  : ', delay_flag[8])
                        print('ห้องที่ 10 : ', delay_flag[9])
                        print('ห้องที่ 11 : ', delay_flag[10])
                        print('ห้องที่ 12 : ', delay_flag[11])
                        print('ห้องที่ 13 : ', delay_flag[12])
                        print('ห้องที่ 14 : ', delay_flag[13])
                        print('ห้องที่ 15 : ', delay_flag[14])
                        print('ห้องที่ 16 : ', delay_flag[15])
                        print('ห้องที่ 17 : ', delay_flag[16])
                        print('ห้องที่ 18 : ', delay_flag[17])
                        print('ห้องที่ 19 : ', delay_flag[18])
                        print('ห้องที่ 20 : ', delay_flag[19])
                        print('ห้องที่ 21 : ', delay_flag[20])
                        print('ห้องที่ 22 : ', delay_flag[21])
                        print('ห้องที่ 23 : ', delay_flag[22])
                        print('ห้องที่ 24 : ', delay_flag[23])
                        print('ห้องที่ 25 : ', delay_flag[24])
                        client.publish("/cut/load1", int(delay_flag[0]))
                        client.publish("/cut/load2", int(delay_flag[1]))
                        client.publish("/cut/load3", int(delay_flag[2]))
                        client.publish("/cut/load4", int(delay_flag[3]))
                        client.publish("/cut/load5", int(delay_flag[4]))
                        client.publish("/cut/load6", int(delay_flag[5]))
                        client.publish("/cut/load7", int(delay_flag[6]))
                        client.publish("/cut/load8", int(delay_flag[7]))
                        client.publish("/cut/load9", int(delay_flag[8]))
                        client.publish("/cut/load10", int(delay_flag[9]))
                        client.publish("/cut/load11", int(delay_flag[10]))
                        client.publish("/cut/load12", int(delay_flag[11]))
                        client.publish("/cut/load13", int(delay_flag[12]))
                        client.publish("/cut/load14", int(delay_flag[13]))
                        client.publish("/cut/load15", int(delay_flag[14]))
                        client.publish("/cut/load16", int(delay_flag[15]))
                        client.publish("/cut/load17", int(delay_flag[16]))
                        client.publish("/cut/load18", int(delay_flag[17]))
                        client.publish("/cut/load19", int(delay_flag[18]))
                        client.publish("/cut/load20", int(delay_flag[19]))
                        client.publish("/cut/load21", int(delay_flag[20]))
                        client.publish("/cut/load22", int(delay_flag[21]))
                        client.publish("/cut/load23", int(delay_flag[22]))
                        client.publish("/cut/load24", int(delay_flag[23]))
                        client.publish("/cut/load25", int(delay_flag[24]))
                        time.sleep(1)
                    gpower.append(E[0] / 10)
                    # print('อดีต', Etts[0])
                    # print('ปัจจุบัน', E[0])
                    # print('อนาคต', Ep[0])
            # print('time =', ontime)  # นับเวลาคอมเพสเซอร์ทำงาน
            energy = (power * ((ontime[0] + ontime[1]) / 3600))
            e.append(energy)
            print('ontime =', ontime)
            print('energy =', e)
            print('loadcuttime')
            print(loadcuttime[0])
            print(loadcuttime[1])
            print(loadcuttime[2])
            print(loadcuttime[3])
            print(loadcuttime[4])
            print(loadcuttime[5])
            print(loadcuttime[6])
            print(loadcuttime[7])
            print(loadcuttime[8])
            print(loadcuttime[9])
            print(loadcuttime[10])
            print(loadcuttime[11])
            print(loadcuttime[12])
            print(loadcuttime[13])
            print(loadcuttime[14])
            print(loadcuttime[15])
            print(loadcuttime[16])
            print(loadcuttime[17])
            print(loadcuttime[18])
            print(loadcuttime[19])
            print(loadcuttime[20])
            print(loadcuttime[21])
            print(loadcuttime[22])
            print(loadcuttime[23])
            print(loadcuttime[24])
            print('loadcutcount')
            print(loadcutcount[0])
            print(loadcutcount[1])
            print(loadcutcount[2])
            print(loadcutcount[3])
            print(loadcutcount[4])
            print(loadcutcount[5])
            print(loadcutcount[6])
            print(loadcutcount[7])
            print(loadcutcount[8])
            print(loadcutcount[9])
            print(loadcutcount[10])
            print(loadcutcount[11])
            print(loadcutcount[12])
            print(loadcutcount[13])
            print(loadcutcount[14])
            print(loadcutcount[15])
            print(loadcutcount[16])
            print(loadcutcount[17])
            print(loadcutcount[18])
            print(loadcutcount[19])
            print(loadcutcount[20])
            print(loadcutcount[21])
            print(loadcutcount[22])
            print(loadcutcount[23])
            print(loadcutcount[24])
            print('violation', violationcount[0])
            # print(pog)
            # print(pog2)
            #plt.plot(tpower,'-b')

            plt.plot(PMVroom1, '-b')
            #plt.plot(PMVroom2, '-b')
            #plt.plot(PMVroom3, '-b')
            #plt.plot(PMVroom4, '-b')
            plt.plot(PMVroom5, '-r')
            #plt.plot(PMVroom6, '-b')
            #plt.plot(PMVroom7, '-b')
            #plt.plot(PMVroom8, '-b')
            #plt.plot(PMVroom9, '-b')
            plt.plot(PMVroom15, '-g')

            plt.xlabel('Time')  # แกน x พร้อมตั้งชื่อในวงเล็บ
            plt.ylabel('PMV')  # แกน y พร้อมตั้งชื่อในวงเล็บ
            for i in range(timer[24]):
                x += tpower[i]
            print(x)

            j = 0
            p = 0
            c = 0
            for i in range(1080,2080):
                j = tpower[i]
                if j > 30000:
                    p += (j - 30000)
                    print(p)
                    c += 1
            print(c)
            u = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        Room(temp1, temp2, 25)

        plt.show()  # คำสั่งนี้โชว์กราฟจะไว้เป็นคำสั่งสุดท้าย


client1.disconnect()
