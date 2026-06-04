from fastapi import FastAPI
import subprocess

class App:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/')
    def home(self):
        return {"message": "Agentic Self-Healing Pipeline"}

    def ping(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "output": result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr.decode()}

    @app.get('/ping')
    def ping_route(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "output": result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr.decode()}
c
app = App().app