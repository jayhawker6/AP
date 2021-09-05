# INFO

This file contains completed assignments in their respective folders.

## Branches

- Branches that are open are either still assignments being worked on or assignments that are not yet properly formatted to merge into main. Once all code for a given assignment is done it is formatted and then pulled onto main.
- Once all assignments for a given unit are done a branch is created with all the files kept safe while all folders for that unit are placed in a respective unit folder. Once done, the temporary branch is deleted.

## In the case of a de-sync

In the case of branches sticking on git and still showing on remote after merging, check github to make sure all your changes are there, and then close vscode and kill git using the following via command prompt:

```cmd
 taskkill /IM git.exe /T /F 
```

Once this is done then delete the local repository folder using file explorer. Open a new workspace in VSCODE, remove the folders that are now gone from that workspace, and to to ***SOURCE CONTROL > CLONE REPOSITORY > CLONE REPO FROM GITHUB***, and make a file named AP in your repo folder and clone to the folder named AP. All branches should now be synced to correct remote and git will no longer have a ghost repo with ghost branches. All files will be taken from remote repo and everything will sync again.

## Other information

- The following extensions are used, **Bold for required**:
  - **Python for VSCODE**
  - **Pylance**
  - *Git Graph*
  - **GitLens**
  - Docker
  - **GitHub Repositories**
  - **Python Indent**
  - *Snippet*
  - *Jupyter*
  - *Markdownlint*
