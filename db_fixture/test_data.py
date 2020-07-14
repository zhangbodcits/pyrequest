import sys

sys.path.append('../db_fixture')
from db_fixture.mysql_db import DB

# 创建测试数据
datas = {
    # 发布会表数据
    'sign_event': [
        {'id': '1', 'name': '华为P51发布会', '`limit`': '2000', 'status': '1', 'address': '芮城县花园小区',
         'start_time': '2020-08-01 12:00:00', 'create_time': '2020-08-01 12:00:00'},
        {'id': '2', 'name': '参加人数0', '`limit`': '0', 'status': '1', 'address': '芮城县花园小区',
         'start_time': '2020-08-01 12:00:00', 'create_time': '2020-08-01 12:00:00'},
        {'id': '3', 'name': '状态为0关闭', '`limit`': '2000', 'status': '0', 'address': '芮城县花园小区',
         'start_time': '2020-08-01 12:00:00', 'create_time': '2020-08-01 12:00:00'},
        {'id': '4', 'name': '发布会结束', '`limit`': '2000', 'status': '1', 'address': '芮城县花园小区',
         'start_time': '2020-08-01 12:00:00', 'create_time': '2020-08-01 12:00:00'},
        {'id': '5', 'name': 'Iphone12发布会', '`limit`': '2000', 'status': '1', 'address': '芮城县花园小区',
         'start_time': '2020-08-01 12:00:00', 'create_time': '2020-08-01 12:00:00'}
    ],
    # 嘉宾表数据
    'sign_guest': [
        {'id': 1, 'realname': 'erfeng', 'phone': 15035461679, 'email': 'zhangbo_dcits@163.com', 'sign': 0,
         'event_id': 1, 'create_time': '2020-08-01 12:00:00'},
        {'id': 2, 'realname': 'has sign', 'phone': 15035461678, 'email': 'erfeng_dcits@163.com', 'sign': 1,
         'event_id': 1, 'create_time': '2020-08-01 12:00:00'},
        {'id': 3, 'realname': 'shafeng', 'phone': 15035461677, 'email': 'shafeng_dcits@163.com', 'sign': 0,
         'event_id': 5, 'create_time': '2020-08-01 12:00:00'}
    ],
}
# 11111111111111


# 将测试数据插入表
def init_data():
    db = DB()
    for table, data in datas.items():
        print(datas.items, 11111111111111111)
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()

if __name__ == '__main__':
    init_data()
