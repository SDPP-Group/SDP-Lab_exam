import unittest

from app import examapi

class TestExam(unittest.TestCase):
    def setUp(self): #เป็น function ที่ต้องเรียกเพื่อทำการเปิด api แล้ว test โดยอัตโนมัติ ถ้าไ่ม่มีจะใช้งาน unittest ไม่ได้
        self.app = examapi.app.test_client()

    #function ที่เป็น testcase จะต้องขึ้นต้นด้วย test เสมอ
    def test_Case1(self):
        resp = self.app.get('/is_prime/17')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json['result'], 'true') # resp.json จะได้ค่าที่ get มาคือ {'result' : 'true'} ถ้าเรียน resp.json[parameter] ก็จะได้ค่าใน parameter นั้นมา

    def test_Case2(self):
        resp = self.app.get('/is_prime/36')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json['result'], 'false')

    def test_Case3(self):
        resp = self.app.get('/is_prime/13219')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json['result'], 'true')
if __name__ == '__main__':
    unittest.main()