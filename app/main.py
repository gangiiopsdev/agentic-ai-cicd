from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        ip_address = host.split('@')[1]
        if not ip_address.isdigit() and '.' in ip_address:
            return subprocess.run(['ping', '-c', '4', ip_address], capture_output=True, text=True)
    except Exception as e:
        print(f'Error: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result:
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed'}