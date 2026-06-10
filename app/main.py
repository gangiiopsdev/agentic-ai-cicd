from fastapi import FastAPI
import subprocess
gitignore = open('.gitignore', 'w')
gitignore.write("*.pyc\n__pycache__/\n"), gitignore.close()
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run
    completed_process = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": completed_process.stdout}