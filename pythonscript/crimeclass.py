from sklearn import cluster
import pandas as pd
from pyhive import hive

conn = hive.Connection(host="localhost", port=10000, database ='project')
cursor = conn.cursor()
query10="SELECT state_ut,murder,rape,theft,kidnapping_abduction,dacoity,robbery,total_ipc_crimes FROM crime where district = 'TOTAL' and year=2010 order by state_ut"
query11="SELECT state_ut,murder,rape,theft,kidnapping_abduction,dacoity,robbery,total_ipc_crimes FROM crime where district = 'TOTAL' and year=2011 order by state_ut"
query12="SELECT state_ut,murder,rape,theft,kidnapping_abduction,dacoity,robbery,total_ipc_crimes FROM crime where district = 'TOTAL' and year=2012 order by state_ut "
querynw="select staten,population from censuscrime order by staten"

data10 = pd.read_sql_query(query10,conn)
data11 = pd.read_sql_query(query11,conn)
data12 = pd.read_sql_query(query12,conn)
querypopdf=pd.read_sql_query(querynw,conn)
print(querypopdf[::1])

#datas10=data10.iloc[1:,3:]
#datas11=data11.iloc[1:,3:]
#data12=data12.iloc[1:,3:]/querypopdf['population']

data10['murder1'] = data10["murder"]/querypopdf['population']
data10['rape1'] = data10["rape"]/querypopdf['population']
data10['theft1'] = data10["theft"]/querypopdf['population']
data10['robbery'] = data10["robbery"]/querypopdf['population']
data10['dacoity'] = data10["dacoity"]/querypopdf['population']
data10['kidnapping_abduction']=data10['kidnapping_abduction']/querypopdf['population']
data10['total_ipc_crimes']=data10['total_ipc_crimes']/querypopdf['population']

data10=data10[['murder1','rape1','theft1','robbery','dacoity','kidnapping_abduction','total_ipc_crimes']]

data11['murder1'] = data11["murder"]/querypopdf['population']
data11['rape1'] = data11["rape"]/querypopdf['population']
data11['theft1'] = data11["theft"]/querypopdf['population']
data11['robbery'] = data11["robbery"]/querypopdf['population']
data11['dacoity'] = data11["dacoity"]/querypopdf['population']
data11['kidnapping_abduction']=data11['kidnapping_abduction']/querypopdf['population']
data11['total_ipc_crimes']=data11['total_ipc_crimes']/querypopdf['population']

data11=data11[['murder1','rape1','theft1','robbery','dacoity','kidnapping_abduction','total_ipc_crimes']]

data12['murder1'] = data12["murder"]/querypopdf['population']
data12['rape1'] = data12["rape"]/querypopdf['population']
data12['theft1'] = data12["theft"]/querypopdf['population']
data12['robbery'] = data12["robbery"]/querypopdf['population']
data12['dacoity'] = data12["dacoity"]/querypopdf['population']
data12['kidnapping_abduction']=data12['kidnapping_abduction']/querypopdf['population']
data12['total_ipc_crimes']=data12['total_ipc_crimes']/querypopdf['population']

data12=data12[['murder1','rape1','theft1','robbery','dacoity','kidnapping_abduction','total_ipc_crimes']]
k_means10 = cluster.KMeans(n_clusters=5)
k_means10.fit(data10)
k_means11 = cluster.KMeans(n_clusters=5)
k_means11.fit(data11)
k_means12 = cluster.KMeans(n_clusters=5)
k_means12.fit(data12)

#print(x)
print(k_means10.labels_[::1])
print(k_means11.labels_[::1])
print(k_means12.labels_[::1])


