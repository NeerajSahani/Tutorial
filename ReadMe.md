E:\Notes\Django\Django Projects>django-admin startproject Dummy

E:\Notes\Django\Django Projects>cd Dummy


E:\Notes\Django\Django Projects\Dummy>git init
Initialized empty Git repository in E:/Notes/Django/Django Projects/Dummy/.git/

E:\Notes\Django\Django Projects\Dummy>git config --global user.name

E:\Notes\Django\Django Projects\Dummy>git config --global user.name "NeerajSahani"

E:\Notes\Django\Django Projects\Dummy>git config --global user.email "Neerajsahani9@gmail.com" 

E:\Notes\Django\Django Projects\Dummy> git remote add origin https://github.com/NeerajSahani/Tutorial.git

E:\Notes\Django\Django Projects\Dummy>git remote -v
origin  https://github.com/NeerajSahani/Tutorial.git (fetch)
origin  https://github.com/NeerajSahani/Tutorial.git (push)

E:\Notes\Django\Django Projects\Dummy>git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Dummy/
        manage.py

nothing added to commit but untracked files present (use "git add" to track)

E:\Notes\Django\Django Projects\Dummy>git add .

E:\Notes\Django\Django Projects\Dummy>git commit -m "Initial"
[master (root-commit) 5c8a70a] Initial
 6 files changed, 198 insertions(+)
 create mode 100644 Dummy/__init__.py
 create mode 100644 Dummy/asgi.py
 create mode 100644 Dummy/settings.py
 create mode 100644 Dummy/urls.py
 create mode 100644 Dummy/wsgi.py
 create mode 100644 manage.py

E:\Notes\Django\Django Projects\Dummy>