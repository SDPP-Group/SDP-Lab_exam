from flask import Flask, jsonify #import pakage จาก flask เพื่อใช้ทำ api
from math import isqrt #import package isqrt จาก module math เพื่อใช้ในการคำนวณ

app = Flask(__name__) # object app แทน Flask

@app.route('/') #path / หน้าเริ่มต้นบน  browser
def index():
    return "SDPX ----> Exam Start!!!" #show this text in browser

@app.route('/is1honor/<x>', methods=['GET']) #/path/<parameter> and method
def is1honor(x):
    try:
        x = float(x)
        if x>= 3.5 and x<= 4.0:
            return jsonify({'result' : True}), 200
        else:
            return jsonify({'result' : False}), 200
        # if x == 2 or x == 3: 
        #     return jsonify({'result' : 'true'}), 200
        # if x <= 1 or x % 2 == 0 or x % 3 == 0:
        #     return jsonify({'result' : 'false'}), 200
        # stop = isqrt(x)
        # for i in range(5, stop + 1, 6):
        #     if x % i == 0 or x % (i + 2) == 0:
        #         return jsonify({'result' : 'false'}), 200
    
    except:
        return jsonify({'message' : 'Inputs must be float.'}), 400 #ใช้ jsonify เพื่อให้สามารถ return ค่าเป็น json ได้, return status code 400 เพื่อยอก user ว่า "คำขอไม่ถูกต้อง" 
    return jsonify({'result' : False}), 200
if __name__ == '__main__':
    app.run()
    #host 0.0.0.0 หมายถึง run ทุก address บนเครื่อง
    #ทั้ง loop back และ ipv4 ที่เครื่องนั้นใช้อยู่
    #โดยจะ run บน port 5000