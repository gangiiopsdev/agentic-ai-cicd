from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def validate_host(host: str):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):