from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')</code>
</div>
<div class="source-code-line"><code>def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid input"}

    try:
        result = subprocess.run(['ping', subprocess.list2cmdline([host])], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}