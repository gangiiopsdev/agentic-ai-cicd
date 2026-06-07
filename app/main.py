from fastapi import FastAPI
import subprocess
git_url = "https://github.com/user/repo.git"
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

@app.get("/clone")
def clone_repo(repo_url: str):
    try:
        output = subprocess.check_output(['git', 'clone', repo_url], stderr=subprocess.STDOUT, timeout=60)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}