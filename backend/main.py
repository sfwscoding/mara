from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# -----------------------------------------------------------------
# 1. ⚠️ ตั้งค่า CORS (สำคัญมาก)
# -----------------------------------------------------------------
origins = [
    "https://ssth.app",  # ต้องใส่ URL ของ Frontend หลัง Deploy https://frontend-eta-one-otqawr9y18.vercel.app/
    #"http://127.0.0.1:5500",     # สำหรับทดสอบ
    #"http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------
# 2. ข้อมูลจำลอง (Mock Data)
# -----------------------------------------------------------------
# ในแอปจริง คุณครูอาจจะดึงส่วนนี้มาจาก Database
mock_students = [
    {
        "id": 1,
        "first_name": "สมชาย",
        "last_name": "ใจดี",
        "nickname": "ตั้ม",
        "image_url": "https://placehold.co/100x100/E2E2E2/757575.png?text=ตั้ม"
    },
    {
        "id": 2,
        "first_name": "สุดา",
        "last_name": "รักเรียน",
        "nickname": "น้อย",
        "image_url": "https://placehold.co/100x100/D8F8E3/4A4A4A.png?text=น้อย"
    },
    {
        "id": 3,
        "first_name": "วิชิต",
        "last_name": "ขยัน",
        "nickname": "เป้",
        "image_url": "https://placehold.co/100x100/FEF4D9/5B5B5B.png?text=เป้"
    }
]

# -----------------------------------------------------------------
# 3. Model สำหรับรับข้อมูล (Pydantic)
# -----------------------------------------------------------------
class ScoreData(BaseModel):
    student_id: int
    score: float

# -----------------------------------------------------------------
# 4. API Endpoints
# -----------------------------------------------------------------
@app.get("/")
def read_root():
    return {"message": "Gradebook API is running"}

# Endpoint สำหรับส่งรายชื่อนักเรียนทั้งหมด
@app.get("/api/students")
def get_students():
    return mock_students

# Endpoint สำหรับรับคะแนนที่ส่งมาจาก Frontend
@app.post("/api/submit_score")
def submit_score(data: ScoreData):
    # ในแอปจริง ส่วนนี้คือการบันทึกคะแนนลง Database
    print(f"ได้รับคะแนน: นักเรียน ID {data.student_id}, คะแนน {data.score}")
    
    return {
        "status": "success",
        "message": f"บันทึกคะแนน {data.score} ให้กับนักเรียน ID {data.student_id} เรียบร้อย"
    }