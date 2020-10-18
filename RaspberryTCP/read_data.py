#16/10/2020 v3
import blynklib
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import time
#-----------define value------------------
init_connect = True
init_read = False
var_Compare=0
list_Buffer1=[]
list_Buffer2=[]
list_Buffer3=[]
list_buffer4=[]
list_buffer5=[]
list_Buffer=[]
list_Buffer_Start=[]
list_Buffer_Final=[]
count = 0
list_String_IVT1=[25,22,22,19,18,22,22,20,20,19,22,19,22,22,22]
list_Data_F=[]
flag_read_Current=True
flag_read_Weather=False
data_Weather=0
keep_Alarm=False
var_alarm_up = False #initilize value
list_Alarm=[]
lsit_Count_Alarm=[]
count_Alarm=0
Var_Flag_Add=0
Var_Flag_Clear=0
list_SCB=["SCB01","SCB02","SCB03","SCB04","SCB05","SCB06","SCB07","SCB08","SCB09","SCB010","SCB011","SCB012","SCB013","SCB014","SCB015","SCB016"]
on_Alarm= False
off_Alarm=False
# Flag -------->
list_Error_Flag=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]# No 17 is Count error
list_Error_Flag_Save=[]
var_Index_Error=""
#list_FError_Flag=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]# No 17 is Count error
list_Alarm_Buffer=[]
list_Alarm_Write=[]
list_Alarm_Save=[]
count_Alarm=0
list_Count_Alarm=[]
"""
ip_Device=["192.168.1.151","192.168.1.152","192.168.1.153","192.168.1.154","192.168.1.155","192.168.1.156",
           "192.168.1.157","192.168.1.158","192.168.1.159","192.168.1.160","192.168.1.161","192.168.1.162",
           "192.168.1.163","192.168.1.164","192.168.1.165","192.168.1.166"]
"""
ip_Device=["192.168.1.151"]
name_Device=["IVT1.1","IVT1.2","IVT2.1","IVT2.2","IVT3.1","IVT3.2","IVT4.1","IVT4.2","IVT5.1","IVT5.2","IVT6.1","IVT6.2","IVT7.1","IVT7.2","IVT8.1","IVT8.2"]
#-----------end define value -------------
class FloatModbusClient(ModbusClient):
    def read_float(self , address, number=1):
        reg_l = self.read_holding_registers(address,number * 2)
        if reg_l:
            return [utils.decode_ieee(f) for f  in utils.word_list_to_long(reg_l)]
        else:
            reg_l = [16000,16000]
            return [utils.decode_ieee(f) for f  in utils.word_list_to_long(reg_l)]    
c = FloatModbusClient()
def Connect_MbTCP(ip,func,reg_addr,reg_nb):
    SERVER_HOST = ip
    SERVER_PORT = 502
    #c = ModbusClient()
    c.host(SERVER_HOST)
    c.port(SERVER_PORT)
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
    if c.is_open():
        init_read = True
    if init_read==True:
        if func==3:
            regs_data = c.read_float(reg_addr,reg_nb)
            #find_MaxMin(regs_data)
            #print(regs_data)
            return regs_data
        if func==4:
            regs_data=c.read_input_registers(reg_addr,reg_nb)
            return regs_data
            c.close()
        else:
            print("PLS! choose FunctionCod")
def find_MaxMin(data):
    max_data=max(data)
    var_Compare=(max_data*10)/100
    print(var_Compare)
    for y in data:
        if y<max_data-var_Compare:
            print("Lost Current at") 
#Blynk set up github commit
#BLYNK_AUTH = 'yJrIM13raUXVjmYPoGxIyd2LYdOSs0w3'
BLYNK_AUTH = 'ER7orEIO8KJD9D0AsoP6apQ2DztWBc8x'
blynk = blynklib.Blynk(BLYNK_AUTH)

@blynk.handle_event('read V0')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, W0)
@blynk.handle_event('read V1')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB01)
@blynk.handle_event('read V2')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB02)
@blynk.handle_event('read V3')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB03)
@blynk.handle_event('read V4')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB04)
@blynk.handle_event('read V5')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB05)
@blynk.handle_event('read V6')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB06)
@blynk.handle_event('read V7')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB07)
@blynk.handle_event('read V8')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB08)
@blynk.handle_event('read V9')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB09)
@blynk.handle_event('read V10')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB10)
@blynk.handle_event('read V11')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB11)
@blynk.handle_event('read V12')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB12)
@blynk.handle_event('read V13')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB13)
@blynk.handle_event('read V14')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB14)
@blynk.handle_event('read V15')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, SCB15)
###########################################################
# infinite loop that waits for event
###########################################################
def read_weather():
    data=Connect_MbTCP("192.168.1.111",4,1,1)
    return data
#def find_Alarm(var_find):
def get_list_Alarm(list_data_alarm): #phan tich list su co nhan duoc
    list_Count_Alarm=[]
    list_Alarm_Buffer=[]
    count_Alarm_sub=0
    list_Error_Flag=[]
    # khong cho phep them, chi ghi de
    for i in range(len(list_SCB)):
        for y in range(len(list_data_alarm)):
            if list_SCB[i]==list_data_alarm[y]:
                count_Alarm_sub=count_Alarm_sub+1
        if count_Alarm_sub >0:
            list_Alarm_Buffer.append(list_SCB[i])
            list_Count_Alarm.append(str(count_Alarm_sub))
            count_Alarm_sub=0     
    # tim so luong gia tri >80%
    print("in list loi")
    print(list_Alarm_Buffer)
    print(list_Count_Alarm)
    list_Alarm_Buffer=[]
    # STOP HERE
    if len(list_Alarm_Write)>1:
        for i in range(len(list_Count_Alarm)):
            if int(list_Count_Alarm[i])>1: # gia tri cai dat
                var_Index_Error=list_Alarm_Write[i]#<----------- lay gia tri name of COB to compare
                for i in range(len(list_SCB)):
                    if var_Index_Error==list_SCB[i]:
                        list_Error_Flag[i]=1
    return list_Error_Flag
    list_Count_Alarm=[]               
    print(list_Alarm_Write)
    print(list_Count_Alarm)
    '''
    print(list_Alarm_Write)
    for i in range(len(list_Alarm_Write)):
        for y in range(len(list_SCB)):
            if list_Alarm_Write[i]==list_SCB[y]:
                list_Error_Flag[y]=1
    print(list_Error_Flag)
    # flag_Add flag_Error
    '''
def Alarm():
    if on_Alarm == True:
        blynk.notify(alarm_msg)
        blynk.email("cuonglbq@geccom.vn", alarm_msg , "https://shorturl.at/hDTY2")
        on_Alarm = False
    if off_Alarm == True:
        blynk.notify('Alarm CLEAR!')
        off_Alarm = False
def convert_float_int(value_float):
           value_int=int(value_float*100)/100
           return value_int
while True:
    #blynk.run()
    if flag_read_Weather == True:
        data_Weather=read_weather()

    
        W0=data_Weather[0]/10
        if(data_Weather[0]>4000):
            flag_read_Current = True
            flag_read_Weather=False
        else:
            flag_read_Current = False
            flag_read_Weather=True
            print("Low Irradian"+str(data_Weather[0]))
        time.sleep(1)       
#    blynk.run()

#    for x in ip_Device:
#        print(x)
#        a=Connect_MbTCP(x,3,1,10)
#        print(a)
#        print("***********************")
#        time.sleep(5)   
    if flag_read_Current == True:
        data=Connect_MbTCP("192.168.1.151",3,1,15)
        if len(data)>1:
            list_Buffer.append(data)
            count=count+1
            time.sleep(1)
        if count==5:
            count=0
            count_len_Subbuff=len(list_Buffer[1]) # <------ dem so data trong mang 1 cua buffer
            count_len_Buff=len(list_Buffer) # <-------------dem so data trong mang =5
            for a in range(int(count_len_Subbuff)):
                for b in range(count_len_Buff):
                    list_Buffer_Start.append(list_Buffer[b][a])
                
                list_Buffer_Final.append(max(list_Buffer_Start))
                list_Buffer_Start=[]     
            list_Buffer=[]
            SCB01=convert_float_int(list_Buffer_Final[0])
            SCB02=convert_float_int(list_Buffer_Final[1])         
            SCB03=convert_float_int(list_Buffer_Final[2])
            SCB04=convert_float_int(list_Buffer_Final[3])
            SCB05=convert_float_int(list_Buffer_Final[4])
            SCB06=convert_float_int(list_Buffer_Final[5])
            SCB07=convert_float_int(list_Buffer_Final[6])
            SCB08=convert_float_int(list_Buffer_Final[7])
            SCB09=convert_float_int(list_Buffer_Final[8])
            SCB10=convert_float_int(list_Buffer_Final[9])
            SCB11=convert_float_int(list_Buffer_Final[10])
            SCB12=convert_float_int(list_Buffer_Final[11])
            SCB13=convert_float_int(list_Buffer_Final[12])
            SCB14=convert_float_int(list_Buffer_Final[13])
            SCB15=convert_float_int(list_Buffer_Final[14])
            for u in range(len(list_Buffer_Final)):
                d=list_Buffer_Final[u]/list_String_IVT1[u]
                list_Data_F.append(d)
                d=0
            print(list_Data_F)
            max_data=max(list_Data_F)
            var_Compare=(max_data*5)/100
            print(str(var_Compare) + " - " + str(max_data))
            count_Alarm=count_Alarm+1
            for y in list_Data_F:
                if y<max_data-var_Compare:
                    b=list_Data_F.index(y)+1
                    #print("Low Current at SCB No:  " + str(b))#check ok
                    list_Alarm.append(list_SCB[list_Data_F.index(y)])
                    alarm_msg =   "Low Current at SCB No:  " + str(b)
                    var_alarm_up == True
                    #Alarm(var_alarm_up)
                                 
                else:
                    var_alarm_up == False
                    #Alarm(var_alarm_up)
            flag_read_Weather=True
            
            if count_Alarm==2:
                print(list_Alarm)
                value_f=len(get_list_Alarm(list_Alarm))
                print(value_f)
                if value_f==0:
                    list_Error_Flag_Save=list_Error_Flag # gan gia tri vao mang
                    list_Error_Flag=[]
                else:
                    #so sanh chuoi moi va cu
                    for i in list_Error_Flag:
                        if list_Error_Flag[i]!=list_Error_Flag_Save[i]:# khacs gia tri
                            #check la them moi hay cu
                            if list_Error_Flag[i]==0:
                                #du lieu duoc xoa
                                list_Error_Flag_Save[i]=0
                                print("du lieu duoc xoa")
                            if list_Error_Flag[i]==1: # string or int ???????
                                #du lieu duoc them
                                list_Error_Flag_Save[i]=1
                                print("du lieu duoc them")           
                print("hello")
                list_Alarm=[]
                count_Alarm=0
        list_Data_F=[] 
        list_Buffer_Final=[]
def Alarm_thermal():
    if var_RH  > 80.0 and var_alarm_up == True: 
        blynk.notify('Humidity high alarm SET!')
        blynk.email("cuonglbq@geccom.vn", "Sensor Temperature & Humidity", "https://drive.google.com/file/d/1SzKMVdSz59slXK4rYwqK5kk_zL_PKdxi/view?usp=sharing");
        var_alarm_up = False
    if var_alarm_up == False and var_RH < 75.0:
        blynk.notify('Humidity high alarm CLEAR!')
        var_alarm_up = True
