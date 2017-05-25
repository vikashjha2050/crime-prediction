import numpy
from pyhive import hive
import pandas as pd
conn = hive.Connection(host="localhost", port=10000, database ='project')
cursor = conn.cursor()
murderdf=pd.read_sql_query("select povertyrate from poverty ",conn)
murdertar=pd.read_sql_query("select murder from crime where district ='TOTAL' and year = 2011",conn)

a=murderdf.as_matrix()
b=murdertar.as_matrix()

print(a)
print(b)
#
# murder = [871, 970, 1095, 1171, 1238, 1244, 1437, 1438, 1631, 1721]
#
# a = [1523, 112]
# b = [10, 20]

print(numpy.corrcoef(a,b))
