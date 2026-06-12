from fastapi import FastAPI
import subprocess
call = subprocess.run

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Secure implementation
    try:
        call(['ping', subprocess.check_output(f'echo -n {host}', shell=True).decode()], check=True, timeout=5)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}