## คิวคือแถวเรียงหนึ่ง ถ้าใช้ลิสต์แบบเดิม เวลาเอาคนข้างหน้าสุดออกจากแถว คนที่เหลือต้องขยับมาข้างหน้าทั้งหมด ทำให้เสียเวลา 
# แต่ถ้าเราใช้ deque เหมือนกับว่ามีแถวที่ยืดหยุ่นได้ เราสามารถเอาคนข้างหน้าออกได้เลย โดยที่คนอื่นไม่ต้องขยับ ทำให้เร็วกว่ามาก โดยเฉพาะถ้าแถวยาวมากๆ