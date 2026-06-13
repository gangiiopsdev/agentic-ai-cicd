from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Implement your sanitization logic here
    return 'ping '

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(sanitize_input(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}