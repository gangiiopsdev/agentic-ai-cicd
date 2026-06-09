from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        ip_address = host.split('@')[-1]
        if ip_address.replace('.', '').isdigit() or ip_address == 'localhost':
            result = subprocess.run(['ping', ip_address], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'error', 'message': 'Invalid IP address'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)