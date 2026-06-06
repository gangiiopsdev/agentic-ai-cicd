from fastapi import FastAPI
import subprocess
global ping_count
count = 0

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global count
count += 1
if count > 10:
return {"status": "Too many pings", "error": "Limit exceeded"}

# Safe implementation
try:
result = subprocess.run(['ping', host], capture_output=True, text=True)
return {"status": "completed", "output": result.stdout}
except Exception as e:
return {"status": "failed", "error": str(e)}