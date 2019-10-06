"""


"""
import sqlite3
import pymysql
import datetime

__author__ = "Li Wei (liw@sicnu.edu.cn)"


# config
# sqlite
sqlite_db_path = "data.db"

# mysql
mysql_host = "localhost"
mysql_user = "root"
mysql_password = "_WLee0721!"
mysql_db_name = "mythings"
mysql_charset = "utf8"

# action
sync_table_name = "thing"


def sync_area(sqlite_cu, mysql_cu):
    sqlite_query = "select * from area"
    sqlite_cu.execute(sqlite_query)
    sqlite_query_rst = sqlite_cu.fetchall()

    for sqlite_record in sqlite_query_rst:
        id = sqlite_record[0]
        name = sqlite_record[1]
        image = sqlite_record[2]
        detail = str(sqlite_record[3])
        oid = sqlite_record[4]
        create_time = str(sqlite_record[6])[0:-6]
        modify_time = str(sqlite_record[7])[0:-6]

        sql_mysql_insert = "insert into mythings_area(id,place_id,name,image_src,detail,\
 order_id,add_time,add_user_id,last_time,last_user_id) values("
        sql_mysql_insert = sql_mysql_insert + str(id) + ","
        sql_mysql_insert = sql_mysql_insert + "1,"
        sql_mysql_insert = sql_mysql_insert + "'" + name + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + image + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + detail + "',"
        sql_mysql_insert = sql_mysql_insert + str(oid) + ","
        sql_mysql_insert = sql_mysql_insert + "'" + create_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1,"
        sql_mysql_insert = sql_mysql_insert + "'" + modify_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1)"

        print(mysql_cu.execute(sql_mysql_insert))


def sync_position(sqlite_cu, mysql_cu):
    sqlite_query = "select * from position"
    sqlite_cu.execute(sqlite_query)
    sqlite_query_rst = sqlite_cu.fetchall()

    for sqlite_record in sqlite_query_rst:
        id = sqlite_record[0]
        name = sqlite_record[1]
        area = sqlite_record[2]
        image = sqlite_record[3]
        detail = str(sqlite_record[4])
        oid = sqlite_record[5]
        create_time = str(sqlite_record[7])[0:-6]
        modify_time = str(sqlite_record[8])[0:-6]

        sql_mysql_insert = "insert into mythings_position(id,area_id,name,image_src,detail,\
 order_id,add_time,add_user_id,last_time,last_user_id) values("
        sql_mysql_insert = sql_mysql_insert + str(id) + ","
        sql_mysql_insert = sql_mysql_insert + str(area) + ","
        sql_mysql_insert = sql_mysql_insert + "'" + name + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + image + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + detail + "',"
        sql_mysql_insert = sql_mysql_insert + str(oid) + ","
        sql_mysql_insert = sql_mysql_insert + "'" + create_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1,"
        sql_mysql_insert = sql_mysql_insert + "'" + modify_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1)"

        print(mysql_cu.execute(sql_mysql_insert))


def sync_category_collection(sqlite_cu, mysql_cu):
    sqlite_query = "select * from category_collection"
    sqlite_cu.execute(sqlite_query)
    sqlite_query_rst = sqlite_cu.fetchall()

    for sqlite_record in sqlite_query_rst:
        id = sqlite_record[0]
        name = sqlite_record[1]
        image = sqlite_record[2]
        detail = str(sqlite_record[3])
        oid = sqlite_record[4]
        create_time = str(sqlite_record[6])[0:-6]
        modify_time = str(sqlite_record[6])[0:-6]

        sql_mysql_insert = "insert into mythings_category_collection(id,name,image_src,detail,\
 order_id,add_time,add_user_id,last_time,last_user_id) values("
        sql_mysql_insert = sql_mysql_insert + str(id) + ","
        sql_mysql_insert = sql_mysql_insert + "'" + name + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + image + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + detail + "',"
        sql_mysql_insert = sql_mysql_insert + str(oid) + ","
        sql_mysql_insert = sql_mysql_insert + "'" + create_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1,"
        sql_mysql_insert = sql_mysql_insert + "'" + modify_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1)"

        print(mysql_cu.execute(sql_mysql_insert))


def sync_category(sqlite_cu, mysql_cu):
    sqlite_query = "select * from category"
    sqlite_cu.execute(sqlite_query)
    sqlite_query_rst = sqlite_cu.fetchall()

    for sqlite_record in sqlite_query_rst:
        id = str(sqlite_record[0])
        name = str(sqlite_record[1])
        cc = str(sqlite_record[2])
        image = str(sqlite_record[3])
        detail = str(sqlite_record[4])
        maxcount = str(sqlite_record[5])
        oid = str(sqlite_record[6])
        state = str(sqlite_record[7])
        create_time = str(sqlite_record[8])[0:-6]
        modify_time = str(sqlite_record[9])[0:-6]

        sql_mysql_insert = "insert into mythings_category(id,category_collection_id,name,image_src,max_count,detail,\
 order_id,state,add_time,add_user_id,last_time,last_user_id) values("
        sql_mysql_insert = sql_mysql_insert + id + ","
        sql_mysql_insert = sql_mysql_insert + cc + ","
        sql_mysql_insert = sql_mysql_insert + "'" + name + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + image + "',"
        sql_mysql_insert = sql_mysql_insert + maxcount + ","
        sql_mysql_insert = sql_mysql_insert + "'" + detail + "',"
        sql_mysql_insert = sql_mysql_insert + oid + ","
        sql_mysql_insert = sql_mysql_insert + state + ","
        sql_mysql_insert = sql_mysql_insert + "'" + create_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1,"
        sql_mysql_insert = sql_mysql_insert + "'" + modify_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1)"

        print(mysql_cu.execute(sql_mysql_insert))


def sync_marchant(sqlite_cu, mysql_cu):
    sqlite_query = "select * from marchant"
    sqlite_cu.execute(sqlite_query)
    sqlite_query_rst = sqlite_cu.fetchall()

    for sqlite_record in sqlite_query_rst:
        id = str(sqlite_record[0])
        name = str(sqlite_record[1])
        image = str(sqlite_record[2])
        detail = str(sqlite_record[3])
        oid = str(sqlite_record[4])
        state = str(sqlite_record[5])
        create_time = str(sqlite_record[6])[0:-6]
        modify_time = str(sqlite_record[7])[0:-6]

        sql_mysql_insert = "insert into mythings_marchant(id,name,image_src,detail,\
 order_id,state,add_time,add_user_id,last_time,last_user_id) values("
        sql_mysql_insert = sql_mysql_insert + id + ","
        sql_mysql_insert = sql_mysql_insert + "'" + name + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + image + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + detail + "',"
        sql_mysql_insert = sql_mysql_insert + oid + ","
        sql_mysql_insert = sql_mysql_insert + state + ","
        sql_mysql_insert = sql_mysql_insert + "'" + create_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1,"
        sql_mysql_insert = sql_mysql_insert + "'" + modify_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1)"

        print(mysql_cu.execute(sql_mysql_insert))


def sync_thing(sqlite_cu, mysql_cu):
    sqlite_query = "select * from things"
    sqlite_cu.execute(sqlite_query)
    sqlite_query_rst = sqlite_cu.fetchall()

    for sqlite_record in sqlite_query_rst:
        id = str(sqlite_record[0])
        name = str(sqlite_record[1])
        category = str(sqlite_record[2])
        position = str(sqlite_record[3])
        owner = str(sqlite_record[4])
        count = str(sqlite_record[5])
        maxcount = str(sqlite_record[6])
        date = str(sqlite_record[7])[0:-6]
        expeir = str(sqlite_record[8])[0:-6]
        price = str(sqlite_record[9])
        img = str(sqlite_record[10])
        marchant = str(sqlite_record[11])
        type = str(sqlite_record[12])
        detail = str(sqlite_record[13])
        state = str(sqlite_record[14])
        create_time = str(sqlite_record[15])[0:-6]
        modify_time = str(sqlite_record[16])[0:-6]

        sql_mysql_insert = "insert into mythings_thing(id,name,count,max_count,obtain_date,expire_date,price,marchant_id,type,detail,\
 order_id,state,add_time,add_user_id,last_time,last_user_id) values("
        sql_mysql_insert = sql_mysql_insert + id + ","
        sql_mysql_insert = sql_mysql_insert + "'" + name + "',"
        sql_mysql_insert = sql_mysql_insert + count + ","
        sql_mysql_insert = sql_mysql_insert + maxcount + ","
        sql_mysql_insert = sql_mysql_insert + "'" + date + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + expeir + "',"
        sql_mysql_insert = sql_mysql_insert + price + ","
        sql_mysql_insert = sql_mysql_insert + marchant + ","
        sql_mysql_insert = sql_mysql_insert + "'" + type + "',"
        sql_mysql_insert = sql_mysql_insert + "'" + detail + "',"
        sql_mysql_insert = sql_mysql_insert + "0,"
        sql_mysql_insert = sql_mysql_insert + state + ","
        sql_mysql_insert = sql_mysql_insert + "'" + create_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1,"
        sql_mysql_insert = sql_mysql_insert + "'" + modify_time + "',"
        sql_mysql_insert = sql_mysql_insert + "1)"
        print(mysql_cu.execute(sql_mysql_insert))

        sql_mysql_thing_category_insert = "insert into mythings_thing_category(thing_id,category_id) values("
        sql_mysql_thing_category_insert = sql_mysql_thing_category_insert + id + ","
        sql_mysql_thing_category_insert = sql_mysql_thing_category_insert + category + ")"
        print(mysql_cu.execute(sql_mysql_thing_category_insert))

        sql_mysql_thing_image_insert = "insert into mythings_thing_image(thing_id,image_src) values("
        sql_mysql_thing_image_insert = sql_mysql_thing_image_insert + id + ","
        sql_mysql_thing_image_insert = sql_mysql_thing_image_insert + img + ")"
        print(mysql_cu.execute(sql_mysql_thing_image_insert))

        sql_mysql_thing_position_insert = "insert into mythings_thing_position(thing_id,position_id) values("
        sql_mysql_thing_position_insert = sql_mysql_thing_position_insert + id + ","
        sql_mysql_thing_position_insert = sql_mysql_thing_position_insert + position + ")"
        print(mysql_cu.execute(sql_mysql_thing_position_insert))

        if owner != "1":
            sql_mysql_thing_user_insert = "insert into mythings_thing_user(thing_id,user_id) values("
            sql_mysql_thing_user_insert = sql_mysql_thing_user_insert + id + ","
            sql_mysql_thing_user_insert = sql_mysql_thing_user_insert + owner + ")"
            print(mysql_cu.execute(sql_mysql_thing_user_insert))
        elif owner == "1":
            sql_mysql_thing_user_insert = "insert into mythings_thing_user(thing_id,user_id) values("
            sql_mysql_thing_user_insert = sql_mysql_thing_user_insert + id + ",2)"
            print(mysql_cu.execute(sql_mysql_thing_user_insert))
            sql_mysql_thing_user_insert = "insert into mythings_thing_user(thing_id,user_id) values("
            sql_mysql_thing_user_insert = sql_mysql_thing_user_insert + id + ",3)"
            print(mysql_cu.execute(sql_mysql_thing_user_insert))
            sql_mysql_thing_user_insert = "insert into mythings_thing_user(thing_id,user_id) values("
            sql_mysql_thing_user_insert = sql_mysql_thing_user_insert + id + ",4)"
            print(mysql_cu.execute(sql_mysql_thing_user_insert))


def start(sync_table):
    sqlite_conn = sqlite3.connect(sqlite_db_path)   # open sqlite database
    sqlite_cu = sqlite_conn.cursor()                # create sqlite cursor
    mysql_conn = pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_password,
                                 database=mysql_db_name, charset=mysql_charset)
    mysql_cu = mysql_conn.cursor()                  # create mysql cursor

    if sync_table == "area":
        sync_area(sqlite_cu, mysql_cu)
    elif sync_table == "position":
        sync_position(sqlite_cu, mysql_cu)
    elif sync_table == "category_collection":
        sync_category_collection(sqlite_cu, mysql_cu)
    elif sync_table == "category":
        sync_category(sqlite_cu, mysql_cu)
    elif sync_table == "marchant":
        sync_marchant(sqlite_cu, mysql_cu)
    elif sync_table == "thing":
        sync_thing(sqlite_cu, mysql_cu)

    mysql_conn.commit()
    sqlite_cu.close()
    mysql_cu.close()
    sqlite_conn.close()
    mysql_conn.close()


if __name__ == "__main__":
    start(sync_table_name)

