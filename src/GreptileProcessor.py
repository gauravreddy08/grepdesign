import requests
from dotenv import load_dotenv
import os
import urllib.parse
import time

class Greptile():
    def __init__(self, repository, remote='github', branch='main', reload=True, notify=True):

        load_dotenv(override=True)

        self.headers = {
            "Authorization": f"Bearer {os.environ['GREPTILE_API']}",
            "X-GitHub-Token": f"{os.environ['GITHUB_API']}",
            "Content-Type": "application/json"
        }

        self.repository = repository
        self.remote = remote
        self.branch = branch

        self.repositoryId = urllib.parse.quote(f"{self.remote}:{self.branch}:{self.repository}", safe='')

        self.indexed = False
        self._index(reload=reload, notify=notify)
    
    def _index(self, reload=True, notify=True):

        response = self.get_info()
        if response.status_code==200:
            status = response.json().get('status', '')
            if status == 'completed':
                self.indexed = True
                print(f"[INFO] Repository {self.repository} is already indexed.")
                return
            else:
                print(f"[INFO] Repository is currently being {status}. Waiting for completion...")
                self._wait_for_completion()
                return
        
        print(f"[INFO] Indexing {self.repository}...")

        url = "https://api.greptile.com/v2/repositories"

        payload = {
            "remote": self.remote,
            "repository": self.repository,
            "branch": self.branch,
            "reload": reload,
            "notify": notify
        }

        response = requests.request("POST", url, json=payload, headers=self.headers)

        if response.status_code==200:
            print(f"[INFO] Indexed {self.repository} repository sucessfully.")
        else:
            print(response.content)
            raise Exception(f"({response.status_code}) Error indexing repository: {response.content}") 
    
    def get_info(self): 
        url = f"https://api.greptile.com/v2/repositories/{self.repositoryId}"
        return requests.get(url, headers=self.headers)
    
    def _wait_for_completion(self):
        while True:
            response = self.get_info()
            if response.status_code == 200:
                status = response.json().get('status', '')
                if status == 'completed':
                    self.indexed = True
                    print(f"[INFO] Repository {self.repository} indexing completed successfully.")
                    break
            else:
                raise Exception(f"[ERROR] Failed to retrieve repository info. Status code: {response.status_code}")
            
            print(f"[INFO] Still processing. Rechecking in 5 seconds...")
            time.sleep(5)
    
    def search(self, query, stream=False, genius=False):

        if not self.indexed: self._wait_for_completion()

        url = "https://api.greptile.com/v2/query"

        payload = {
            "messages": [
                {
                    "id": "1",
                    "content": str(query),
                    "role": "user"
                }
            ],
            "repositories": [
                {
                    "remote": self.remote,
                    "branch": self.branch,
                    "repository": self.repository
                }
            ],
            "stream": stream,
            "genius": genius
        }

        response = requests.request("POST", url, json=payload, headers=self.headers)

        if response.status_code==200:
            return response.json().get('message')
        else:
            print(response.content)
            raise Exception(f"Error querying repository {response.status_code}") 
    

if __name__ == "__main__":
    pass