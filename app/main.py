from fastapi import FastAPI
import subprocess
get_shell = False
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not get_shell:
        try:
            output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "shell mode not allowed"}