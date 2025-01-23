# Initializing a repository

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://link
git push -u origin main

#Indexing
git add . 

#Restoring indexed files
git restore (--staged) filename.ex

#Commiting
git commit -m "comment"
#Pushing
git push

#Checking status of repository
git status


#Switching different branches
git checkout <branch-name>
git switch <branch-hame>

#Merging branches
git merge <branch-name>

# Retrieve updates from the remote repository without merging them into local branch.
git fetch

# Creating tags for branch
git tag <tag-name>

#Pushes the tag to the remote repository.
git push origin <tag-name>

#To observe commit history log
git log
