import re
import cassandra.cluster as dr

# get connection
def get_con(data_set_find = ()):            
    auth_provider = dr.PlainTextAuthProvider(username=data_set_find[4], password=data_set_find[5])
    cluster = dr.Cluster([data_set_find[1]], port=data_set_find[2], auth_provider=auth_provider)
    session = cluster.connect()
    return session

# add curs db
def add_db(data_db = [], curr_code = '', data_set_find = (), type_db = ''):
    try:
        # connect
        with get_con(data_set_find) as session:                    
            # insert data
            for mas in data_db:
                params = (curr_code, mas[0].strftime("%Y-%m-%d"))                                        
                table_name = data_set_find[3]  + "." + data_set_find[8]
                results = session.execute("SELECT COUNT(*) AS KOL FROM " + table_name + " WHERE curr_code = %s AND curs_date = %s allow filtering", 
                                          params)
                row = results[0]
                if row.kol == 0:
                    params = (curr_code, mas[0].strftime("%Y-%m-%d"), 1, mas[1])                                        
                    session.execute("INSERT INTO " + table_name + " (curr_code, curs_date, forc, rate) VALUES (%s, %s, %s, %s)", params)

    except Exception as err:
        print(type_db + ': ' + re.sub("^\s+|\n|\r|\s+$", '', str(err)))


# load data report
def load_data_report(data_set_find = (), type_db = ''):
    data_report = []
    try:
        # connect
        with get_con(data_set_find) as session:                     
            table_name = data_set_find[3]  + "." + data_set_find[8]
            results = session.execute("SELECT CAST(curs_date AS text) as curs_date, curr_code, rate, forc FROM " + table_name + " WHERE curr_code = 'USD' allow filtering")       
            data = []
            for mas in results:
                data.append([mas.curs_date, mas.curr_code, mas.rate, mas.forc])
            #            
            data_report.append(["Дата курса", "Код валюти","Курс","Відхилення,%"])
            for mas in data:
                dat = mas[0][8:10] + "." + mas[0][5:7] + "." + mas[0][0:4]
                data_report.append([dat, mas[1], mas[2], mas[3]])                
    except Exception as err:
        print(type_db + ': ' + re.sub("^\s+|\n|\r|\s+$", '', str(err)))
    return data_report

