import os

os.system('git status')
os.system('git add .')
message = input('Enter message:  ')
os.system(f'git commit -m"{message}"')
os.system('git push')