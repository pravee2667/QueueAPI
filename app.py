# -*- coding: utf-8 -*-

import pyodbc

import time
import datetime
from flask import Flask,render_template,request


app=Flask(__name__)

server = 'tcp:idcdbserver.database.windows.net,1433' 
database = 'IDCDB' 
username = 'idclogin' 
password = 'Idc@login' 
cnxn = pyodbc.connect(DRIVER='{SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template("source.html")
    

@app.route('/count',methods=['POST','GET'])
def connection():
    if request.method=="POST":
        ts = time.time()
        #value=int(count)
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        cursor = cnxn.cursor()
        results=list(cursor.execute("""select * from dbo.QueueOne where people_count=2"""))
        print(results)
        cursor.commit()
        return "Commited"
    return "Gret"


if __name__=="__main__":
    app.run()