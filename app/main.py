from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_input(input_string):
    # Escape any shell metacharacters in the input string
    return subprocess.list2cmdline([input_string])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', escape_shell_input(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}