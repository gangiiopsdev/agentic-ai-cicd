from fastapi import FastAPI
import subprocess
def clone_repo(repo_url):
    args = ['git', 'clone', repo_url]
    subprocess.run(args, check=True)