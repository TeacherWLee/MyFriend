"""


"""

__author__ = "Li Wei (liw@sicnu.edu.cn)"


from . import web
from flask import render_template
from app.models.dp import dp


# -------- common --------
def calc_page_number(record_num):
    if record_num % dp.page_len != 0:
        return int(record_num / dp.page_len) + 1
    else:
        return int(record_num / dp.page_len)


# -------- index ---------
@web.route("/index")
def index():
    return render_template("index.html")

# -------- category_collection --------
@web.route("/category_collection_list/<p_id>/<int:page>")
def category_collection_list(p_id=-1, page=0):
    max_page = calc_page_number(dp.get_category_collection_count())
    list_record = dp.get_category_collection(page=page)
    list_cell = []
    for i in list_record:
        dict_cell = {"id": i[0], "name": i[1], "image_src": i[2], "detail": i[3],
                     "endpoint": "web.category_list"}
        list_cell.append(dict_cell)
    return render_template("item_list.html", list_cell=list_cell, title="分类组",
                           p_id=p_id, page=page, max_page=max_page,
                           endpoint="web.category_collection_list")

# -------- category --------
@web.route("/category_list/<p_id>/<int:page>")
def category_list(p_id=-1, page=0):
    max_page = calc_page_number(dp.get_category_count(p_id=p_id))
    list_record = dp.get_category(p_id=p_id, page=page)
    list_cell = []
    for i in list_record:
        dict_cell = {"id": i[0], "name": i[2], "image_src": i[3], "detail": i[5],
                     "endpoint": "web.thing_list"}
        list_cell.append(dict_cell)
    return render_template("item_list.html", list_cell=list_cell, title="分类组",
                           p_id=p_id, page=page, max_page=max_page,
                           endpoint="web.category_list")


# -------- place --------
@web.route("/places")
def places():
    list_record = dp.get_all_place()
    list_item = []
    for i in list_record:
        dict_item = {"id": i[0], "name": i[1], "image_src": i[2], "detail": i[3]}
        list_item.append(dict_item)
    return render_template("item_list.html", list_item=list_item, title="所有分类组")


# -------- thing --------
@web.route("/thing_list/<p_id>/<int:page>")
def thing_list(p_id="-1", page=0):
    max_page = calc_page_number(dp.get_thing_count(p_id=p_id))

    if int(p_id) == -1:
        list_record = dp.get_all_thing(page=page)
    else:
        list_record = dp.get_thing(p_id=p_id, page=page)

    list_cell = []
    for i in list_record:
        dict_cell = {"id": i[0],
                     "name": i[1],
                     "detail": i[9],
                     "type": i[8],
                     "image_src": dp.get_thing_image(i[0])[0],
                     "endpoint": "web.thing_detail"}
        list_cell.append(dict_cell)
    return render_template("item_list.html", list_cell=list_cell, title="物品",
                           p_id=p_id, page=page, max_page=max_page,
                           endpoint="web.thing_list")


@web.route("/thing_detail/<p_id>/<int:page>")
def thing_detail(p_id=-1, page=0):
    return render_template("item_detail.html",
                           title="物品详情")
