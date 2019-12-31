"""
data processor

"""

__author__ = "Li Wei (liw@sicnu.edu.cn)"

import pymysql

# -------- mysql config --------
mysql_host = "localhost"
mysql_user = "root"
mysql_password = "_WLee0721!"
mysql_db_name = "mythings_dev"
mysql_charset = "utf8"


class Dp:
    page_len = 10

    _mysql_cu = pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_password,
                                database=mysql_db_name, charset=mysql_charset).cursor()

    # -------- common --------
    def execute(self, sql):
        self._mysql_cu.execute(sql)
        return self._mysql_cu.fetchall()

    # -------- category_collection --------
    def get_category_collection(self, page=0):
        sql = "SELECT * FROM mythings_category_collection  ORDER BY order_id"
        sql += " LIMIT {},{}".format(int(page) * self.page_len, self.page_len)
        return self.execute(sql)

    def get_category_collection_count(self):
        sql = "SELECT COUNT(*) FROM mythings_category_collection"
        return self.execute(sql)[0][0]

    # -------- category --------
    def get_category(self, p_id=-1, page=0):
        sql = "SELECT * FROM mythings_category"
        if p_id != -1:
            sql += " WHERE category_collection_id={}".format(p_id)
        sql += " ORDER BY order_id"
        sql += " LIMIT {},{}".format(int(page) * self.page_len, self.page_len)
        return self.execute(sql)

    def get_category_count(self, p_id=-1):
        sql = "SELECT COUNT(*) FROM mythings_category"
        if p_id != -1:
            sql = sql+" WHERE category_collection_id={}".format(p_id)
        return self.execute(sql)[0][0]

    # -------- thing --------
    def get_all_thing(self, page):
        sql = "SELECT * FROM mythings_thing  ORDER BY order_id"
        sql += " LIMIT {},{}".format(page * self.page_len, self.page_len)
        list_thing = []
        tuple_all_thing = self.execute(sql)
        for thing in tuple_all_thing:
            list_thing.append(thing)
        return list_thing

    def get_thing(self, p_id=-1, page=0):
        sql = "SELECT thing_id FROM mythings_thing_category WHERE category_id=" + str(p_id)
        list_thing_id = self.execute(sql)[page*self.page_len: (page+1)*self.page_len]
        list_thing = []
        for thing_id in list_thing_id:
            sql = "SELECT * FROM mythings_thing WHERE id=" + str(thing_id[0])
            list_thing.append(self.execute(sql)[0])
        return list_thing

    def get_thing_count(self, p_id=-1):
        if int(p_id) == -1:
            sql = "SELECT COUNT(*) FROM mythings_thing"
        else:
            sql = "SELECT COUNT(thing_id) FROM mythings_thing_category WHERE category_id=" + str(p_id)
        return self.execute(sql)[0][0]

    def get_thing_image(self, thing_id):
        sql = "SELECT image_src FROM mythings_thing_image WHERE thing_id="+str(thing_id)
        return self.execute(sql)[0]


dp = Dp()
