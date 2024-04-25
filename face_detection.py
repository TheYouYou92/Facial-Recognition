import cv2
import numpy as np
import sqlite3

FaceDetect = cv2.CascadeClassifier('database.xml')
cam = cv2.VideoCapture(0)


def insertorupdate(Id, Name, age):
    conn = sqlite3.connect('data.db')
    cmd = "SELECT * FROM STUDENTS WHERE ID="+str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist==1:
        conn.execute("UPDATE STUDENTS SET Name=? WHERE Id=? ",(Name, Id, ))
        conn.execute("UPDATE STUDENTS SET age=? WHERE Id=? ",(age, Id, ))
    else:
        conn.execute("INSERT INTO STUDENTS (Id, Name, age) values(?,?,?)", (Id,Name, age))
    conn.commit()
    conn.close()

Id = input("Id: ")
Name = input("Name: ")
age = input("Age: ")

insertorupdate(Id, Name, age)

sampleNum = 0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = FaceDetect.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        sampleNum += 1
        cv2.imwrite(f"dataset/user.{Id}.{sampleNum}.jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0), 2)
        cv2.waitKey(100)

    cv2.imshow("Face", img)
    cv2.waitKey(100)
    if sampleNum> 20:
        break

cam.release()
cv2.destroyAllWindows()







