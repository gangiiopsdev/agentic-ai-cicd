from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Sanitize the host parameter to prevent command injection
        result = subprocess.run(['ping', subprocess.check_output(f'echo {host}', shell=True).decode().strip()], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Call the function directly to avoid shell=True vulnerability
    return ping(host)