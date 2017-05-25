from pyhive import hive
import pandas as pd
conn = hive.Connection(host="localhost", port=10000, database ='project')
cursor = conn.cursor()
murderdf=pd.read_sql_query("select rape from crime where district ='TOTAL' and state_ut='UTTAR PRADESH' and year != 2012",conn)
murdertar=pd.read_sql_query("select rape from crime where district ='TOTAL' and state_ut='UTTAR PRADESH' and year = 2012",conn)

murder=murderdf.as_matrix()
murdertarget=murdertar.as_matrix()

#murder = [871, 970, 1095, 1171, 1238, 1244, 1437, 1438, 1631, 1721]
rape = [1356, 1253, 1191, 1214, 1194, 1207, 1374, 1426, 1323]
weight = [.20, .32, .48]
val = []
val1 = []
sum1 = []
argg = []


val.append(((murder[1]-murder[0])+(murder[2]-murder[1]))/2)


val.append(((murder[4]-murder[3])+(murder[5]-murder[4]))/2)


val.append(((murder[7]-murder[6])+(murder[8]-murder[7]))/2)
#print(val)

for i in range(0, len(val)):
    sum1.append(val[i]*weight[i])
#print(sum1)

for i in range(0, len(sum1)):
     argg.append(float(sum1[i]/1000))
#print(argg)

sum2 = sum(argg)
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
