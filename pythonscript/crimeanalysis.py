import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from pyhive import hive
from operator import truediv
conn = hive.Connection(host="localhost", port=10000, database ='project')
cursor = conn.cursor()

querymurder="SELECT state_ut,murder FROM crime where district = 'TOTAL' and year=2011 order by state_ut"
querynw="select staten,literacyrate,population,nonworker from censuscrime order by staten"
querypr="select statep,povertyrate from poverty order by statep"

murderdf=pd.read_sql_query(querymurder,conn)
cendf=pd.read_sql_query(querynw,conn)
prdf=pd.read_sql_query(querypr,conn)

murderdf['mrate']=murderdf['murder']/cendf['population']
cendf['unemprate']=cendf['nonworker']/cendf['population']
cendf['illiteracyrate']=-cendf['literacyrate'].subtract(100)
cendf['povrate']=prdf['povertyrate']
murderdf = murderdf.drop(['state_ut','murder'], 1)

# print(murderdf[::1])
# print(cendf[::1])
# print(prdf[::1])

cendf=cendf[["unemprate","illiteracyrate","povrate"]]
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(cendf,murderdf)

# The mean squared error
print("Mean squared error: %.2f"
       % np.mean((regr.predict(cendf) - murderdf) ** 2))
#
# x1=pd.DataFrame(regr.predict(cendf))
# x1["qw"]=((x1 - murderdf).abs())
# print(x1["qw"])
#
# x1["qwe"]=x1["qw"]/murderdf['murder']
#
# print(x1["qwe"])
#Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(cendf, murderdf))

out=pd.DataFrame()
out["state"]=prdf["statep"]
out['unemprate']=cendf['unemprate']
out['illiteracyrate']=-cendf['illiteracyrate']
out['povrate']=prdf['povertyrate']
out["predicted"]=regr.predict(cendf)
out["original"]=murderdf

print(out[::1])