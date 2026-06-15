from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Safe implementation using subprocess.Popen
        args = ['ping', host]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output, error
global Ping_service
Ping_service = PingService()
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output, error = Ping_service.ping(host)
    if error:
        return {"status": "error", "message": error.decode()}
    else:
        return {"status": "completed", "output": output.decode()}