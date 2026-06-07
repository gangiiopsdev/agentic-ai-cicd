from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = subprocess.quote(host)
        result = subprocess.run(['ping', '--', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}