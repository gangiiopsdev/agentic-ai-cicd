from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_clone_repo(repo_url):
    # Validate the repository URL before cloning
    if not repo_url.startswith('https://github.com/'):
        raise ValueError('Invalid repository URL')
    try:
        subprocess.run(['git', 'clone', repo_url], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Failed to clone repository: {e}')

@app.post('/clone_repo/')
def clone_repo(repo_url: str):
    safe_clone_repo(repo_url)