from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}

# Additional recommendations:
# - Use a whitelist of allowed hosts instead of accepting arbitrary input.
# - Implement proper error handling and logging for better security monitoring.