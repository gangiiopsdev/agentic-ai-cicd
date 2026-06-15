from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        self.ping_command = ['ping', 'localhost']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    pinger = SafePinger()
    try:
        subprocess.run(pinger.ping_command + [host], check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": subprocess.check_output(pinger.ping_command + [host]).decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)