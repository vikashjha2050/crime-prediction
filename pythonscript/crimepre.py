from pyhive import hive
import pandas as pd
conn = hive.Connection(host="localhost", port=10000, database ='project')
cursor = conn.cursor()
murderdf=pd.read_sql_query("select murder from crime where district ='TOTAL' and state_ut='MAHARASHTRA' and year != 2012",conn)
murdertar=pd.read_sql_query("select murder from crime where district ='TOTAL' and state_ut='MAHARASHTRA' and year = 2012",conn)

murder=murderdf.as_matrix()
murdertarget=murdertar.as_matrix()

# murder = [871, 970, 1095, 1171, 1238, 1244, 1437, 1438, 1631, 1721]
rape = [1356, 1253, 1191, 1214, 1194, 1207, 1374, 1426, 1323, 1223]
weight = [0.04, .05, .06, .08, .09, .11, .13, .19, .25]
val = []
sum1 = []
arg = []


for i in range(1,10):
    val.append(murder[i]-murder[i-1])
#print(val)

for i in range(1, len(val)-1):
    sum1.append(val[i]*weight[i])
#print(sum1)

for i in range(0, len(sum1)):
    arg.append(float(sum1[i]/1000))
#print(arg)

sum2 = sum(arg)
#print(sum2)

sum3 = sum2*murder[10]
#print(sum3)

sum4 = sum3 + murder[10]
print("predicted value")
print(sum4)
print("original value")
print(murdertarget)

Accuracy = 100 - ((sum4 - murdertarget)/murdertarget)*100
Accuracy1 = 100 + ((sum4 - murdertarget)/murdertarget)*100

print("accuracy")
if sum4 > murdertarget:
    print(Accuracy)
else: print(Accuracy1)
#
# if(Accuracy<0):
#     print(-Accuracy)
# else:
#     print(Accuracy)


# Accuracy = 100 - ((sum4 - murdertarget)/murdertarget)*100
# print("qwe")
# print(Accuracy)
