import re
import datetime as dt
import pymongo as dr

# get connection
def get_con(data_set_find = ()):                
    myclient = dr.MongoClient("mongodb://" + data_set_find[1] + ":" + str(data_set_find[2]) + "/", 
                              username=data_set_find[4], 
                              password=data_set_find[5])
    return myclient

# add curs db
def add_db(data_db = [], curr_code = '', data_set_find = (), type_db = ''):
    try:
        # connect
        with get_con(data_set_find) as myclient:                    
            # insert data
            mydb = myclient[data_set_find[3]]
            mycol = mydb[data_set_find[8]]                
            mydict_list = []
            for mas in data_db:                  
                my_dt = dt.datetime(mas[0].year, mas[0].month, mas[0].day, 0, 0, 0)
                mydict = { "curr_code" : curr_code,  "curs_date" : my_dt, "rate" : mas[1], "forc" : 1}
                is_exists = False
                for ff in mycol.find({},{"curr_code": curr_code, "curs_date": my_dt }):
                    is_exists = True
                if not is_exists:
                    mydict_list.append(mydict)                
            if len(mydict_list) > 0:
                mycol.insert_many(mydict_list)


    except Exception as err:
        print(type_db + ': ' + re.sub("^\s+|\n|\r|\s+$", '', str(err)))


# load data report
def load_data_report(data_set_find = (), type_db = ''):
    data_report = []
    try:
        # connect
        with get_con(data_set_find) as myclient:                     
            mydb = myclient[data_set_find[3]]
            mycol = mydb[data_set_find[8]]   
            data_report = []
            data_report.append(["Дата курса", "Код валюти","Курс","Відхилення,%"])
            #
            start_dt = dt.datetime(dt.date.today().year, 1, 1, 0, 0, 0)   
            end_dt = dt.datetime(dt.date.today().year, 12, 31, 0, 0, 0)   
            myquery = {"curr_code": "USD", "curs_date": {"$lt": end_dt, "$gte": start_dt}}
            mydoc = mycol.find(myquery)
            for mas in mydoc:                
                data_report.append([mas["curs_date"].strftime("%d.%m.%Y"), mas["curr_code"], mas["rate"], mas["forc"]])                

    except Exception as err:
        print(type_db + ': ' + re.sub("^\s+|\n|\r|\s+$", '', str(err)))
    return data_report

