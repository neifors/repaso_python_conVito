# Git commands:

1. Initiate git repository in local
   - **git init** on the desire repository
   #####
2. Basic commands:
   - **git status** to see the status of your selected branch
   - **git add (file)** to transfer your files from local repository to staging area
     - **git add -A** All files transfered
   - **git commit -m "your message"** to transfer your files from staging area to the git directory (comment always required)
   - **git checkout (branch)** Change between branches
   #####
3. Link between remote and local repository
   - **git remote add origin (github/...)**
   #####
4. Push commands
   - **git push origin (branch)** transfer from local to remote
     - **git push origin (branch) --force** to force it
   #####
5. Pull commands
   - **git pull origin (branch)** transfer from remote to local
   - **git clone (link)** when local repository is empty you can download it all from remote
   #####
6. Create branch
   - **git branch (name_of_branch)**
   #####
7. Merge master/develop from local to remote
   - If you want to merge your develop branch into master
     - **git checkout master** you have to be on the branch you want to make the merge, in this case, master
     - **git merge (branch_to_merge)** if rebase instead of merge, it will rebase
     - **git push origin master**
   #####
8. Pull request

   - **git request-pull (branch_to_merge/rebase) (url_of_repository) (branch_where_to_merge)**

   #####

9. Change remote
   - **git remote set-url origin https://github.com/USERNAME/REPOSITORY.git**
   - **git remote -v**
   
10. Diff
	git branch -a to show all branches (local & remote)
	git diff branch branch
	
11. git stash
