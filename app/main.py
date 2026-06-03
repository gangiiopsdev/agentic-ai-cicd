from fastapi import FastAPI
import subprocess
def shlex_quote(input_string):
    return shlex.quote(input_string)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command_parts = ["ping", shlex_quote(host)]
    subprocess.run(command_parts, check=True)
    return {"status": "completed"}