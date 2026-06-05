from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping():
    result = subprocess.run(['ping', '8.8.8.8'], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}