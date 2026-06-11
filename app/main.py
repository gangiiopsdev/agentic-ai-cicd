from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', '-c', '1']
app = FastAPI()
@app.get('/')
def home():    return {"message": "Agentic Self-Healing Pipeline"}
@app.get('/ping')
def ping(host: str):    try:
        # Validate the host input to prevent command injection
        if not host.isalnum():
            raise ValueError("Invalid host")
        result = subprocess.run(generate_ping_command + [host], check=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    except ValueError as ve:
        return {"status": "error", "message": str(ve)}