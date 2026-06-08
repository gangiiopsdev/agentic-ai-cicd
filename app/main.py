from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '1', subprocess.quote(self.host)], universal_newlines=True)
            return output
        except Exception as e:
            return str(e)
global_safe_ping = SafePing(None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_safe_ping.host = host
    result = global_safe_ping.execute()
    return {"status": "completed", "result": result}