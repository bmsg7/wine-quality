# wine-quality
MLOPS E2E Project MLflow Docker CI/CD AWS

## Prerequisites-
 - Github account
 - VS Code Setup in your system

## Project Setup
 - Login to github. Click on new to Create a new Repository
 - Fill the necessary details (Repo name, add readme, Python .gitignore)
 - Click on Code, to see the new repository created
 - Click on the green button (code) to Copy the link to clone the repository into your local machine:
      - Create a new folder in your system and click right click to open terminal in that location
      - After terminal get’s open execute the following commmand git clone <REPO_LINK_COPIED_IN_PREVIOUS_STEP>
 `git clone https://github.com/bmsg7/wine-quality.git`
      - On the same opened terminal cd to the project folder and then print `code .`
  
  ## Building Project
  1. **Virtual Environment creation** :
     - First task we’ll create a new environment. For that go to Terminal and click on the new terminal. Execute the below command in the terminal
`conda create -p ./env python=3.8 -y`
     - activate the virtual environment. `conda activate ./env`. This will activate the virtual Environment
  2. **Project Structure** : We’ll create a template.py file to where we’ll write all the necessary files and modules for our project. 
     -  template.py : This is the basic Structure of Project that everyone follows in industry. We’re using logging to find out the root cause of Bugs in the future. Open the Terminal again `(Press ctrl+~)` and run command `python template.py`. All the files and modules will automatically get created. Also in Terminal you’ll be able to see that We’re able to see each and every logs or flow of the code.

     -  Commit changes or new file/folder created 


