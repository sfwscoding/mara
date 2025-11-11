from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# -----------------------------------------------------------------
# ⚠️ สำคัญมาก: ตั้งค่า CORS
# ให้ใส่ URL ของ Frontend ที่จะได้หลังจาก Deploy (หรือใส่ * ไปก่อนตอนทดสอบ)
# -----------------------------------------------------------------
origins = [
    "https://frontend-eta-one-otqawr9y18.vercel.app",  # เช่น https://my-frontend.vercel.app
   # "http://localhost:5500",     # สำหรับทดสอบบนเครื่อง
   # "http://127.0.0.1:5500",     # สำหรับทดสอบบนเครื่อง
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Backend"}

@app.get("/api/data")
def get_data():
    return {"message": "นี่คือข้อมูลที่ส่งมาจาก Backend", "value": 12345}