from fastapi import FastAPI
import subprocess

class App:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/')
    def home(self):
        return {'message': 'Agentic Self-Healing Pipeline'}

    @app.get('/ping')
    def ping(host: str):
        # Safe implementation
        subprocess.call(['ping', host])
        return {'status': 'completed'}

app_instance = App().app