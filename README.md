# SDP-Lab_exam have 5 tasks
-------------------- Task 1(Local) --------------------
1. สร้าง API ตามที่โจทย์กำหนด API ไม่ซับซ้อน
2. สร้าง Unittest สำหรับ API ที่ถูกสร้างขึ้นมา
3. แสดง Code API แล้ว Run Unittest ให้อาจารย์ดู
4. Commit ไปยัง branch ชื่อ "my-feature-01"
    - git branch my-feature-01
    - git checkout my-feature-01
    - git add [something]
    - git commit -m "[something]"
    - git push
5. ทำการ merge request จาก my-feature-01 ไปยัง main

-------------------- Task 2(Local) --------------------
1. สร้าง robot framework สำหรับ case ตาม task 1
2. แสดง code และ run robot framework ใหผู้คุมสอบดู
    - robot "file.robot"
3. Commit code 
** repository ของ robot อยู่คนละที่กับ API

-------------------- Task 3 --------------------
1. Approve การทำ Merge Request จาก task
2. ดูผลลัพธ์ Unittest และ robot framework จากเครื่อง VM
3. ทดลองเรียก API 0าก VM 
    - เรียกผ่าน browser โดยการทำ port forwarding จาก vm
-------------------- Task 4 --------------------
1. ทดสอบ Load test ของ API ที่เรียกใช้บน VM
    - ใช้ JMeter บน Local เซ็ต User 10 คนใน 10 วินาที
2. แสดงกราฟ และตอบคำถามเกี่ยวกับค่า Throughput ของการทดลองนี้

# File Hierachy
- repo
- |----app
-     |---api.py
-     |---Dockerfile
-     |---requirement.txt 
- |----Jenkinsfile
- |----api-unittest.py
- |----README.md

# Jenkins pipeline
---------- [VM1] run jenkins ----------
1. run unittest [VM2]
2. create docker image [VM2]
3. create container [VM2]
4. Clone robot repository [VM2]
5. run robot test [VM2]
6. Push image into gitlab registry [VM2]
7. Pull Image from gitlab registry [VM3]
8. Create container from image [VM3] = *api run here*

