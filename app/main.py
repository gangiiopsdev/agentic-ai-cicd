from fastapi import FastAPI
import subprocess
global_result = {
    'status': None,
}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        global_result['status'] = 'completed'
        return {"status": global_result['status'], "output": result.stdout}
    except subprocess.CalledProcessError as e:
        global_result['status'] = 'failed'
        return {"status": global_result['status'], "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}