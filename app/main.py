from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    try:
        # Validate the input to ensure it is a valid hostname or IP address
        if not host.replace('.', '').isalnum() and '-' not in host:
            return {"error": "Invalid input"}, 400
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"error": str(e)}, 500