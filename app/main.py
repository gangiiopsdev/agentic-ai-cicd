from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum())

app = FastAPI()

@app.get="/)
async def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        # Use check_output to avoid shell=True and mitigate risks
        subprocess.check_output(f'ping -c 1 {sanitized_host}', shell=False, text=True)
        return {"status": "completed", "response": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}