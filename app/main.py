from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_run(command, *args, **kwargs):
        return subprocess.run(command, *args, **kwargs, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):