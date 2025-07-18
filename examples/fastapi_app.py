from fastapi import FastAPI
from yololang import yolo

app = FastAPI()

@app.get("/generate_text")
@yolo
async def generate_text(topic: str) -> dict:
    """Generate a short, two-sentence paragraph about the given topic."""
    ... # The implementation will be generated by yolo

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Yolo-powered FastAPI app! Visit /docs for API details."}
