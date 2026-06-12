from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', '-c', '1', host]  # Limit the number of pings to mitigate risks
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(generate_ping_command(host), capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout,
            "error": None
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "output": e.output,
            "error": str(e)
        }