from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.stderr}"

class SafeFastAPI(FastAPI):
    @app.get("/ping")
    def ping(self, host: str):
        return safe_ping(host)

app = SafeFastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}