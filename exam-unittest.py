import unittest

from app import examapi

class TestExam(unittest.TestCase):
    def setUp(self): #เป็น function ที่ต้องเรียกเพื่อทำการเปิด api แล้ว test โดยอัตโนมัติ ถ้าไ่ม่มีจะใช้งาน unittest ไม่ได้
        self.app = examapi.app.test_client()

    #function ที่เป็น testcase จะต้องขึ้นต้นด้วย test เสมอ
    def test_x_is_3dot6(self):
        resp = self.app.get('/is1honor/3.6')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json['result'], True) # resp.json จะได้ค่าที่ get มาคือ {'result' : 'true'} ถ้าเรียน resp.json[parameter] ก็จะได้ค่าใน parameter นั้นมา

    def test_x_is_3dot5(self):
        resp = self.app.get('/is1honor/3.5')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json['result'], True)

    def test_x_is_3dot4(self):
        resp = self.app.get('/is1honor/3.4')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json['result'], False)
if __name__ == '__main__':
    unittest.main()