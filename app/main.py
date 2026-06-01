from fastapi import FastAPI
import subprocess
global_subprocess = subprocess.Popen(['ping'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_subprocess.stdin.write(host.encode('utf-8') + b'\n')
    output, error = global_subprocess.communicate()
    return {"status": "completed", "output": output.decode('utf-8'), "error": error.decode('utf-8')} if error else {"status": "completed", "output": output.decode('utf-8')}