'''
มีนักวิ่ง 2 คน (R1,R2) วิ่งโดยเริ่มที่จุด x1,x2 บนเส้นจำนวน ตามลำดับ (-10000<=x1<x2<=10000)
เมื่อเริ่มวิ่ง นักวิ่งจะวิ่งไปทางขวาของเส้นจำนวนพร้อมกัน โดย R1 วิ่งด้วยอัตราเร็ว v1 หน่วย/วินาที
และ R2 วิ่งด้วยอัตราเร็ว v2 หน่วย/วินาที (1<=v2<v1<=100) และอัตราเร็วทั้งคู่จะไม่เพิ่มไม่ลด
จงหาว่า R1 ใช้เวลากี่วินาทีในการแซง R2

มี 2 บรรทัด
บรรทัดที่ 1 รับค่าของจำนวนเต็ม x1 และ x2 แทนจุดเริ่มต้นของ R1 และ R2 บนเส้นจำนวน ตามลำดับ (-10000<=x1<x2<=10000)
บรรทัดที่ 2 รับค่าของจำนวนเต็ม v1 และ v2 แทนอัตราเร็วของ R1 และ R2 ตามลำดับ (1<=v2<v1<=100)
(สังเกตว่า v2<v1 และ x1<x2)
'''
import math

