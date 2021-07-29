from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    import random
    return random.random()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", debug=True)
    #uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info", debug=True)
    # 開発時
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", debug=True, reload=True)