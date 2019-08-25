import requests
import unittest
from model.yoy_login_3 import yoy_login
from model.multipart_from_data_1 import addStudent
from common.sql import qita_sql,select_sql


class TestAddStudent(unittest.TestCase):
    def setUp(self):
        # 数据清理
        sql = "delete from hello_student where id='001'"
        qita_sql(sql)
        # 数据准备
        self.s = requests.session()
        yoy_login(self.s,"zhezhe","111111")
    def tearDown(self):
        self.s.close()

    def test_1(self):
        result = addStudent(self.s)
        print(result)
        self.assertTrue(result)

        # 连接数据库，查询
        # 进行新增（写入）数据的断言
        sql_select = "select * from hello_student where student_name='111'"
        res = select_sql(sql_select)
        print(res)
        self.assertTrue(res["teacher_name"] == "111")
        self.assertTrue(res["tel"] == "13800000000")
        self.assertTrue(res["mail"] == "111@qq.com")
        self.assertTrue(res["sex"] == "F")


if __name__ == '__main__':
    unittest.main()