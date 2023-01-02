import random
from datetime import timedelta
from datetime import datetime
from git import Repo
from git.Actor import actor

repo_path = '/path/to/repo'
repo = Repo(repo_path)

# Generate a random number of days between 0 and 25
num_days = random.randint(0, 25)

# Subtract the random number of days from the current date
commit_date = (datetime.now() - timedelta(days=num_days)).strftime('%Y-%m-%d %H:%M:%S')

# Create a file in the repository
with open(f'{repo_path}/test.txt', 'w') as f:
    f.write('test')

# Add the file to the repository
repo.index.add(['test.txt'])

# Create the commit
author = actor.Actor('Aman Khadka', 'amulifts@gmail.com')
committer = actor.Actor('Aman Khadka', 'amulifts@gmail.com')
repo.index.commit('Commit message', author=author, committer=committer, author_date=commit_date, commit_date=commit_date)

# Push the commit to the repository
origin = repo.remote(name='origin')
origin.push()
