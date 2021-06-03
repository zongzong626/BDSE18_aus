from flask import Flask, render_template, request, redirect, url_for, session
from flask_moment import Moment
from datetime import datetime
import sqlalchemy as db
from sqlalchemy import func
import math

app = Flask(__name__)
moment = Moment(app)





#----------practice start------------
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/mel.html')
def mel():
    return render_template("mel.html")

@app.route('/weather.html')
def weather():
    return render_template("weather.html")

@app.route('/weather1.html')
def weather1():
    return render_template("weather1.html")

@app.route('/visa.html')
def visa():
    return render_template("visa.html")

@app.route('/faq.html')
def faq():
    return render_template("faq.html")

@app.route('/spots.html')
def spots():
    app = Flask(__name__)
    moment = Moment(app)
#連接資料庫
    username = 'watcher'     # 資料庫帳號
    password = 'password'     # 資料庫密碼
    host = 'localhost'    # 資料庫位址
    port = '3306'         # 資料庫埠號
    database = '行程'   # 資料庫名稱
    table = '單點行程'   # 表格名稱
# 建立資料庫引擎
    engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
# 建立資料庫連線
# con = engine.raw_connection()
    connection  = engine.connect()
# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
    metadata = db.MetaData()
    print(f"metadata: \n{metadata.sorted_tables}")
# 取得 office 資料表的 Python 對應操作物件
    table_office = db.Table(table, metadata, autoload=True, autoload_with=engine)
    print(f"metadata: \n{metadata.sorted_tables}",end="\n"+("-"*80)+"\n")  # 比較Table建立前後的metadata 

    # query string
    page = int(request.args.get('page') if request.args.get('page') else 1)
    each_page = 10

    # set total pages
    connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
    query = db.select(func.count()).select_from(table_office)
    proxy = connection.execute(query)
    total_pages = math.ceil(proxy.fetchall()[0][0]/each_page) # [0][0] => inorder to get the value

    # fetch data & decided by page
    query = db.select(table_office).limit(each_page).offset((page-1)*each_page)
    proxy = connection.execute(query)
    results = proxy.fetchall()
    # print(results[1].keys())
    print(results[0].keys())
    # Close connection
    connection.close()
    
    return render_template('spots.html',
                           page_header="list all data",
                           total_pages=total_pages,
                           outputs=results,
                           page=page)

@app.route('/schedule.html')
def schedule():
    app = Flask(__name__)
    moment = Moment(app)
#連接資料庫
    username = 'watcher'     # 資料庫帳號
    password = 'password'     # 資料庫密碼
    host = 'localhost'    # 資料庫位址
    port = '3306'         # 資料庫埠號
    database = '行程'   # 資料庫名稱
    table = '多點行程'   # 表格名稱
# 建立資料庫引擎
    engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
# 建立資料庫連線
# con = engine.raw_connection()
    connection  = engine.connect()
# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
    metadata = db.MetaData()
    print(f"metadata: \n{metadata.sorted_tables}")
# 取得 office 資料表的 Python 對應操作物件
    table_office = db.Table(table, metadata, autoload=True, autoload_with=engine)
    print(f"metadata: \n{metadata.sorted_tables}",end="\n"+("-"*80)+"\n")  # 比較Table建立前後的metadata 
    # query string
    page = int(request.args.get('page') if request.args.get('page') else 1)
    each_page = 10

    # set total pages
    connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
    query = db.select(func.count()).select_from(table_office)
    proxy = connection.execute(query)
    total_pages = math.ceil(proxy.fetchall()[0][0]/each_page) # [0][0] => inorder to get the value

    # fetch data & decided by page
    query = db.select(table_office).limit(each_page).offset((page-1)*each_page)
    proxy = connection.execute(query)
    results = proxy.fetchall()
    # print(results[1].keys())
    print(results[0].keys())
    # Close connection
    connection.close()
    
    return render_template('schedule.html',
                           page_header="list all data",
                           total_pages=total_pages,
                           outputs=results,
                           page=page)


@app.route('/days_schedule.html')
def days_schedule():
    app = Flask(__name__)
    moment = Moment(app)
#連接資料庫
    username = 'watcher'     # 資料庫帳號
    password = 'password'     # 資料庫密碼
    host = 'localhost'    # 資料庫位址
    port = '3306'         # 資料庫埠號
    database = '行程'   # 資料庫名稱
    table = '多日行程'   # 表格名稱
# 建立資料庫引擎
    engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
# 建立資料庫連線
# con = engine.raw_connection()
    connection  = engine.connect()
# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
    metadata = db.MetaData()
    print(f"metadata: \n{metadata.sorted_tables}")
# 取得 office 資料表的 Python 對應操作物件
    table_office = db.Table(table, metadata, autoload=True, autoload_with=engine)
    print(f"metadata: \n{metadata.sorted_tables}",end="\n"+("-"*80)+"\n")  # 比較Table建立前後的metadata 
    # query string
    page = int(request.args.get('page') if request.args.get('page') else 1)
    each_page = 5

    # set total pages
    connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
    query = db.select(func.count()).select_from(table_office)
    proxy = connection.execute(query)
    total_pages = math.ceil(proxy.fetchall()[0][0]/each_page) # [0][0] => inorder to get the value

    # fetch data & decided by page
    query = db.select(table_office).limit(each_page).offset((page-1)*each_page)
    proxy = connection.execute(query)
    results = proxy.fetchall()
    # print(results[1].keys())
    print(results[0].keys())
    # Close connection
    connection.close()
    
    return render_template('days_schedule.html',
                           page_header="list all data",
                           total_pages=total_pages,
                           outputs=results,
                           page=page)

@app.route('/diy.html')
def diy():
#連接資料庫
    username1 = 'watcher'     # 資料庫帳號
    password1 = 'password'     # 資料庫密碼
    host1 = 'localhost'    # 資料庫位址
    port1 = '3306'         # 資料庫埠號
    database1 = '住宿'   # 資料庫名稱
    table1 = 'airbnb'   # 表格名稱
# 建立資料庫引擎
    engine1 = db.create_engine(f'mysql+pymysql://{username1}:{password1}@{host1}:{port1}/{database1}')
# 建立資料庫連線
# con = engine.raw_connection()
    connection1  = engine1.connect()
# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
    metadata1 = db.MetaData()
    print(f"metadata: \n{metadata1.sorted_tables}")
# 取得 office 資料表的 Python 對應操作物件
    table_office1 = db.Table(table1, metadata1, autoload=True, autoload_with=engine1)
    print(f"metadata: \n{metadata1.sorted_tables}",end="\n"+("-"*80)+"\n")  # 比較Table建立前後的metadata 
# fetch data & decided by page
    query = db.select(table_office1)
    proxy = connection1.execute(query)
    results1 = proxy.fetchall()
    # print(results[1].keys())
    print("我是1",results1[0].keys())

#連接資料庫
    username2 = 'watcher'     # 資料庫帳號
    password2 = 'password'     # 資料庫密碼
    host2 = 'localhost'    # 資料庫位址
    port2 = '3306'         # 資料庫埠號
    database2 = '住宿'   # 資料庫名稱
    table2 = '住宿'   # 表格名稱
# 建立資料庫引擎
    engine2 = db.create_engine(f'mysql+pymysql://{username2}:{password2}@{host2}:{port2}/{database2}')
# 建立資料庫連線
# con = engine.raw_connection()
    connection2  = engine2.connect()
# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
    metadata2 = db.MetaData()
    print(f"metadata: \n{metadata2.sorted_tables}")
# 取得 office 資料表的 Python 對應操作物件
    table_office2 = db.Table(table2, metadata2, autoload=True, autoload_with=engine2)
    print(f"metadata: \n{metadata2.sorted_tables}",end="\n"+("-"*80)+"\n")  # 比較Table建立前後的metadata 
# fetch data & decided by page
    query = db.select(table_office2)
    proxy = connection2.execute(query)
    results2 = proxy.fetchall()
    # print(results[1].keys())
    print("我是2",results2[0].keys())


    #連接資料庫
    username3 = 'watcher'     # 資料庫帳號
    password3 = 'password'     # 資料庫密碼
    host3 = 'localhost'    # 資料庫位址
    port3 = '3306'         # 資料庫埠號
    database3 = '景點'   # 資料庫名稱
    table3 = '景點'   # 表格名稱
# 建立資料庫引擎
    engine3 = db.create_engine(f'mysql+pymysql://{username3}:{password3}@{host3}:{port3}/{database3}')
# 建立資料庫連線
# con = engine.raw_connection()
    connection3  = engine3.connect()
# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
    metadata3 = db.MetaData()
    print(f"metadata: \n{metadata3.sorted_tables}")
# 取得 office 資料表的 Python 對應操作物件
    table_office3 = db.Table(table3, metadata3, autoload=True, autoload_with=engine3)
    print(f"metadata: \n{metadata3.sorted_tables}",end="\n"+("-"*80)+"\n")  # 比較Table建立前後的metadata 
# fetch data & decided by page
    query = db.select(table_office3)
    proxy = connection3.execute(query)
    results3 = proxy.fetchall()
    # print(results[1].keys())
    print("我是3",results3[0].keys())

    # Close connection
    connection1.close()
     # Close connection
    connection2.close()
     # Close connection
    connection3.close()

    return render_template('diy.html',
                           outputs1=results1,
                           outputs2=results2,
                           outputs3=results3
                           )
    
@app.route('/site.html')
def site():
    return render_template("site.html")

@app.route('/planning.html')
def planning():
    return render_template("planning.html")
#----------practice end-------------- 


    # query string
    page = int(request.args.get('page') if request.args.get('page') else 1)
    each_page = 5

    # set total pages
    connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
    query = db.select(func.count()).select_from(table_office)
    proxy = connection.execute(query)
    total_pages = math.ceil(proxy.fetchall()[0][0]/each_page) # [0][0] => inorder to get the value

    # fetch data & decided by page
    query = db.select(table_office).limit(each_page).offset((page-1)*each_page)
    proxy = connection.execute(query)
    results = proxy.fetchall()
    # print(results[1].keys())
    print(results[0].keys())


# @app.route('/data-edit', methods=["GET", "POST"])
# def data_edit():
#     if request.method=="POST":
#         try:
#             connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
#             query = db.select(table_office).order_by(table_office)
#             proxy = connection.execute(query)
#             id_list = [idx[0] for idx in proxy.fetchall()]
#             if request.form['FirstName']: # 希望至少要填寫名子
#                 query = db.update(table_office).where(table_office == request.form['行程名稱']).values(**{k:request.form[k] for k in request.form.keys()})
#                 proxy = connection.execute(query)
#             else:
#                 raise Exception
#         except:
#             return render_template('data_edit.html',
#                                     page_header="edit data",id_list=id_list,status="Failed")
#         else:
#             return render_template('data_edit.html',
#                                     page_header="edit data",id_list=id_list,status="Success")
#         finally:
#             # Close connection
#             connection.close()
           
#     if request.method=="GET":
#         connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
#         query = db.select(table_office).order_by(table_office)
#         proxy = connection.execute(query)
#         id_list = [idx[0] for idx in proxy.fetchall()]
#         return render_template('data_edit.html',
#                                 page_header="edit data",id_list=id_list)

if __name__=="__main__":
    app.run(debug=True)