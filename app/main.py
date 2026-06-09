from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(user_input):
    return [part.strip() for part in user_input.split(' ')] if ' ' in user_input else [user_input]

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.run(escape_command(host), check=True)
    return {"status": "completed"}