from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="AI-Omni Intelligence API")

class NewsItem(BaseModel):
    title: str
    original_url: str
    xhs_copy: str  # AI重写的小红书文案
    source: str    # 如 GitHub, TechCrunch
    category: str  # 科技, AI, 硬件
    created_at: str

# 模拟内存数据库
news_db: List[NewsItem] = []

@app.get("/")
async def root():
    return {"message": "AI-Omni Backend is running"}

@app.post("/api/ingest")
async def ingest_news(item: NewsItem):
    """接收来自 n8n 的推送数据"""
    news_db.insert(0, item)
    return {"status": "success", "data_count": len(news_db)}

@app.get("/api/news", response_model=List[NewsItem])
async def list_news():
    """前端看板调用的接口"""
    return news_db[:20]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
