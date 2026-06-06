from fastapi import FastAPI
import subprocess
get_input = subprocess.run

app = FastAPI()

def sanitize_input(host):
    if not host.replace('.', '').isdigit():
        raise ValueError("Invalid input")

@app.get("/ping")
def ping(host: str):    
    try:
        output = get_input(['ping', '-c', '1', host], capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}