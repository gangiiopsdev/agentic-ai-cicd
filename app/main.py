from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', '-c', '1']
app = FastAPI()
@app.get="/")def home():    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")def ping(host: str):    try:
        result = subprocess.run(generate_ping_command + [host], check=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}