from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            subprocess.run(['ping', host], check=True, shell=False)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed for {host}: {e}')
app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    SafeSubprocess.ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}