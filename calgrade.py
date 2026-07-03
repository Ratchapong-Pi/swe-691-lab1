def calculate_grade(scores):
    # 1. ตรวจสอบก่อนว่าลิสต์ว่างหรือไม่ เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "No scores provided", 0

    # 2. ใช้ sum() เพื่อหาผลรวม แทนการวน loop (ทำให้โค้ดสั้นและเร็วขึ้น)
    total = sum(scores)
    average = total / len(scores)

    # 3. ตรรกะการตัดเกรด (คงเดิม เพราะถูกต้องอยู่แล้ว)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade, average

# ทดสอบด้วยข้อมูลปกติ
scores1 = [85, 92, 78, 88, 95]
print(f"Normal case: {calculate_grade(scores1)}")

# ทดสอบกรณีลิสต์ว่าง (ถ้าเป็นโค้ดเก่าจะพังที่บรรทัดนี้)
scores2 = []
print(f"Empty list case: {calculate_grade(scores2)}")
