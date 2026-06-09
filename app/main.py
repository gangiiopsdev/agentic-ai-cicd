from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def execute(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
class App:
    def __init__(self):
        self.app = FastAPI()

    def ping(self, host: str):
        return SafePing.execute(host)

app = App().app
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = app.ping(host)
    return {"status": "completed", "result": result}