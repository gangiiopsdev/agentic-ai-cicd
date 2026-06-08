from fastapi import FastAPI
import subprocess
git_url = "https://github.com/user/repo.git"
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or 'localhost' in host or '127.0.0.1' in host:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    else:
        return {"status": "failed", "error": "Invalid host"}

@app.get("/clone")
def clone_repo(repo_url: str):
    if not repo_url or 'https://github.com/user/repo.git' == repo_url:
        output = subprocess.check_output(['git', 'clone', repo_url], stderr=subprocess.STDOUT, timeout=60)
        return {"status": "completed", "output": output.decode()}
    else:
        return {"status": "failed", "error": "Invalid repository URL"}