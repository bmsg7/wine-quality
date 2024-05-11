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

     -  Commit changes for new file/folder created
  3. **Adding Setup file** : Before that we need to set up setup.py :
     - Update setup.py file and enter the information mentioned below correctly
       ```
       REPO_NAME = "End_to_end_MLOPS_project"
       AUTHOR_USER_NAME = "Somesh"
       SRC_REPO = "mlProject"
       AUTHOR_EMAIL = "chitranshisomesh@gmail.com"
       ```
       We utilise setup.py to ensure that all modules are installed as a package. This ensures that there are no issues when importing from any location. In this case, we are creating 'src' as a package.
   4. **Adding required Libraries** : Add necessary libraries into requirement.txt. Open the Terminal and execute `pip install -r requirement.txt`. All the mentioned libraries will get installed in the environment.
   5. Commit changes for new project setup and libraries has been added 

## Logging Module
Setting up logging Module. First of all we’ll set up our logging module(Refer src/mlProject/__init__.py)
  1. Add a file src/mlProject/__init__.py
  2. Copy the file content from this source
