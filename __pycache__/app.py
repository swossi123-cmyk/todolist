from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
def home():
    return {"message":"hello my name is abdelkabir age is 13 years old i love programing: "}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
