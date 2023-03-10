import MySQLdb
import pandas as pd


# data = pd.read_csv("crawl_travel.csv",encoding="utf-8")

try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(host = "localhost", #主機名稱
                           user = "root", #帳號
                           password = "123456", #密碼
                           port=3308) #port
    
    #使用cursor()方法操作資料庫
    cursor = conn.cursor()
    
    # # 顯示資料庫版本
    # cursor.execute("SELECT VERSION()")
    # db_info = cursor.fetchone()
    # print("資料庫版本：%s" %(db_info))
    
    # # 創建資料庫project
    # sql = "create database if not exists project"
    # cursor.execute(sql)
    # print("資料庫創建成功")
    
    # 使用資料庫project
    sql = "use project"
    cursor.execute(sql) 
    print("資料庫切換成功")
    
    # # 創建資料表travel
    # sql = """create table if not exists travel(content varchar(30))"""
    # cursor.execute(sql)
    # print("資料表創建成功")
    
    # # 插入資料表資料
    # try:
    #     for i in range(len(data)):
    #         sql = "insert into travel (content) VALUES (%s)"
    #         var = data.iloc[i]
    #         cursor.execute(sql, var)
    #     conn.commit() # 重整
    #     print("資料寫入完成")  
    # except Exception as e:
    #     print("錯誤訊息：",e)
    
    # 查詢資料表travel內容
    try:
        cursor.execute("select * from travel")
        d = cursor.fetchall()
        # for i in d:
        #     print(i)
        d1 = pd.DataFrame(d,columns=["留言"])
    except Exception as e:
        print("錯誤訊息：",e)
    
except Exception as e:
    print("資料庫連接失敗",e)
    
finally:
    cursor.close()
    conn.close()
    print("資料庫連接結束")
    
print(d1)