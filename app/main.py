from fastapi import FastAPI
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout,
global_safe_ping = SafePing.safe_ping

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = global_safe_ping(host)
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}