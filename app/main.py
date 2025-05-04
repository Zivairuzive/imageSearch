from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(
    title ='AI powered image search',
    description = "Search free images using natural language powered by AI embeddings.",
    version = '1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
    )

@app.get("/")
def route():
    return {"message": "AI Image Search API is running."}