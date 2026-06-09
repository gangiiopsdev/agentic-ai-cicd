from fastapi import FastAPI
import subprocess
glue_snippet_48c2b0e6 = subprocess.run(['ping', host], capture_output=True, text=True)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    result = glue_snippet_48c2b0e6.stdout if glue_snippet_48c2b0e6.returncode == 0 else 'Failed'
    return {"status": result}