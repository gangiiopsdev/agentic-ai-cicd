from fastapi import FastAPI
import shlex

app = FastAPI()

def escape_shell(input_str):
    safe_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.
	\ ')
    return ''.join(c for c in input_str if c in safe_chars)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output and proper command argument handling
    host = escape_shell(host)
    subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, shell=False)
    return {"status": "completed"}