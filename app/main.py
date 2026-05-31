from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not any(char in host for char in ' ;&|()$`\t\n\r*?{}[]<>,/\\^~#\"\'@!-'):
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid characters in host input')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}