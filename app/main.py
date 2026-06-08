from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(args):
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ["ping", host]
    output, error = run_command(args)
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "output": output}