from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        # Validate the host input to prevent command injection
        if not all(char.isalnum() or char in ['.', '-'] for char in host):
            raise ValueError('Invalid hostname')
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}