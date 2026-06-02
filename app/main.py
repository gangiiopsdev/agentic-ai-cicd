from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"`
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and validate input
        if '&&' in host or '|' in host or ';' in host or '`' in host:
            raise ValueError("Invalid input detected")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}