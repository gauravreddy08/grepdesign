from git import Repo
import os
import re
import shutil

class Repository():
    def __init__(self, repository):
        self.localDir = 'local'
        self.repository = repository

        # Check if the repository already exists
        if os.path.exists(self.localDir):
            shutil.rmtree(self.localDir)
    
        os.makedirs(self.localDir)
        self.clone()
    
    def clone(self):
        url = f"https://github.com/{self.repository}.git"
        self.gitrepo = Repo.clone_from(url, self.localDir)
    
    def push_changes(self):
        self.gitrepo.git.add(all=True)

        commit_message = "Edited files via @greptile"
        self.gitrepo.index.commit(commit_message)

        origin = self.gitrepo.remote(name='origin')
        origin.push()

        print(f"[INFO] Pushed changes to GitHub ({self.repository})")
        return "Pushed changes to GitHub"
    
    def _normalize_whitespace(self, text):
        return re.sub(r'\s+', ' ', text).strip()
    
    def write_file(self, filepath, old_code, updated_code):
        
        if filepath.startswith('/'): filepath = filepath[1:]

        filepath = os.path.join(self.localDir, filepath)

        if not os.path.exists(filepath):
            return f"{filepath} does not exist."
        
        with open(filepath, 'r') as file:
            content = file.read()

        old_code = self._normalize_whitespace(old_code)
        updated_code = self._normalize_whitespace(updated_code)
        content = self._normalize_whitespace(content)

        if old_code in content:
            updated_content = content.replace(old_code, updated_code)
            
            with open(filepath, 'w') as file:
                file.write(updated_content)
            
            print(f"[INFO] Making changes to '{filepath}'")
            return f"Made changes to '{filepath}' sucessfully."
        else:
            print(f"[INFO] Could not make changes to '{filepath}'")
            return f"Could not find {old_code} in {filepath}"

if __name__ == '__main__':
    rep = Repository('gauravreddy08/test1')
    rep.push_changes()

    




