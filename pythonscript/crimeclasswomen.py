from sklearn import cluster
import pandas as pd
from pyhive import hive

conn = hive.Connection(host="localhost", port=10000, database ='project')
cursor = conn.cursor()
query10="SELECT rape,custodial_rape,other_rape,kidnapping_abduction_of_women_and_girls,dowry_deaths,assault_on_women_with_intent_to_outrage_her_modesty," \
        "insult_to_modesty_of_women,cruelty_by_husband_or_his_relatives FROM crime where district = 'TOTAL' and year=2010 "
query11="SELECT rape,custodial_rape,other_rape,kidnapping_abduction_of_women_and_girls,dowry_deaths,assault_on_women_with_intent_to_outrage_her_modesty," \
        "insult_to_modesty_of_women,cruelty_by_husband_or_his_relatives FROM crime where district = 'TOTAL' and year=2011 "
query12="SELECT rape,custodial_rape,other_rape,kidnapping_abduction_of_women_and_girls,dowry_deaths,assault_on_women_with_intent_to_outrage_her_modesty," \
        "insult_to_modesty_of_women,cruelty_by_husband_or_his_relatives FROM crime where district = 'TOTAL' and year=2012 "

data10 = pd.read_sql_query(query10,conn)
data11 = pd.read_sql_query(query11,conn)
data12 = pd.read_sql_query(query12,conn)

k_means10 = cluster.KMeans(n_clusters=5)
k_means10.fit(data10)
k_means11 = cluster.KMeans(n_clusters=5)
k_means11.fit(data11)
k_means12 = cluster.KMeans(n_clusters=5)
k_means12.fit(data12)

print( k_means10.labels_[::1])
print(k_means11.labels_[::1])
print(k_means12.labels_[::1])

