#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import urllib
from time import sleep
from IPython.display import clear_output
from pymongo import MongoClient

while(True):
    k=[]
    clear_output(wait=True)
    MONGODB_CONNECTION_STRING = "mongodb+srv://KDRM:"+urllib.parse.quote("pass@123")+"@cluster0.iffy9by.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(MONGODB_CONNECTION_STRING)
    db = client.symbolsDB
    symbol_list_from_DB = db.test.find({})
    source = pd.DataFrame(list(symbol_list_from_DB))
    no = db.test.count_documents({})  
    for i in range(no):
        # appennding timestamps according to the count of documents in a collection
        k.append(pd.Timestamp.now()) 
    # defining a column for Time for timestamps mapped to the documents    
    source['Time']= k
    # reinitiating the list as one could perform insert, delete operation and change the count of documents
    k=[] 
    display(source.set_index('Time'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


#Since we will be displaying dataframe we import the library pandas
import pandas as pd 
#To avoid error due to Cluster's password containing specila character '@', 
import urllib
#We need this for 
import time
from time import sleep
from IPython.display import clear_output
from pymongo import MongoClient

def querydb():
    MONGODB_CONNECTION_STRING = "mongodb+srv://KDRM:"+urllib.parse.quote("pass@123")+"@cluster0.iffy9by.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(MONGODB_CONNECTION_STRING)
    db = client.symbolsDB    
    source = pd.DataFrame(list(db.test.find()))
    clear_output(wait=True)
    myQ = input("Enter Query")
    execute = """source = pd.DataFrame(list(db.test."""+myQ+"""))"""
    try:
        exec(execute)
    except Exception:
        pass      
    return source


def streamdb():      
    k=[]
    clear_output(wait=True)
    MONGODB_CONNECTION_STRING = "mongodb+srv://KDRM:"+urllib.parse.quote("pass@123")+"@cluster0.iffy9by.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(MONGODB_CONNECTION_STRING)
    db = client.symbolsDB
    symbol_list_from_DB = db.test.find({})
    querydb()
    source = pd.DataFrame(list(db.test.find()))
    no = source.shape[0]  
    for i in range(int(no)):
        # appennding timestamps according to the count of documents in a collection
        k.append(pd.Timestamp.now()) 
     # defining a column for Time for timestamps mapped to the documents    
    source['Time']= k
    # reinitiating the list as one could perform insert, delete operation and change the count of documents
    k=[] 
    time.sleep(1)
    display(source)
    time.sleep(5)

p= True

while(p):
    i = int(input('Do you want to perform query press 1 for yes | 0 for no : '))
    if i:
        streamdb()
    else:
        p=False
    
# insert_one({'_id':9,'Name':'RRR'})  
# delete_one({'_id':9,'Name':'RRR'}) 


# In[ ]:


# import basic libraries needed
import pandas as pd
import numpy as np
# We need this bceause of password of your cluster containing special characters 
import urllib
# import streamz
from streamz.dataframe import PeriodicDataFrame,DataFrame
from streamz import Stream
# import hvplot to stream plots
import panel as pn
import hvplot.pandas
import hvplot.streamz
# import MongoClient from pymongo
from pymongo import MongoClient

def streamdb(**kwargs):
    k=[]
    #Connect with your MongoDB cluster.
    MONGODB_CONNECTION_STRING = "mongodb+srv://KDRM:"+urllib.parse.quote("pass@123")+"@cluster0.iffy9by.mongodb.net/?retryWrites=true&w=majority"
    # establish a client connection
    client = MongoClient(MONGODB_CONNECTION_STRING)
    # point to symbolsDB collection 
    db = client.symbolsDB
    # emtpy symbols collection before inserting new records
    db.symbols.drop()
    # get all records from collection
    symbol_list_from_DB = db.test.find({})
    source = pd.DataFrame(list(symbol_list_from_DB))
    # get the count of documents in a collection
    no = db.test.count_documents({})  
    for i in range(no):
        # appennding timestamps according to the count of documents in a collection
        k.append(pd.Timestamp.now()) 
    # defining a column for Time for timestamps mapped to the documents    
    source['Time']= k
    # reinitiating the list as one could perform insert, delete operation and change the count of documents
    k=[] 
    # here we return the dataframe
    return source.set_index(['Time','_id','Name'])  

# we use PeriodicDatarame to call streamdb function periodically based on the value of the interval attribute provided
sdf = PeriodicDataFrame(streamdb,interval='0s')
sdf


# In[ ]:




