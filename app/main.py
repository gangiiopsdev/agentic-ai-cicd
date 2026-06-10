from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()} 
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

# Sanitize user input
import re
def sanitize_input(input_str):
    if not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", input_str):  # Example regex for email validation
        raise ValueError("Invalid input")

@app.get("/ping")
def ping(host: str):
    try:
        sanitize_input(host)
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()} 
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}