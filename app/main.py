from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def call(host):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = str(e.output, 'utf-8')
        return output

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = PingCommand.call(host)
    return {"status": "completed", "response": response}