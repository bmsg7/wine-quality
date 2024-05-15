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
## Utils Module
In the "utils" part of our code, we put things that we use a lot in different places. For example, if we keep reading information from a YAML file and using it everywhere, instead of doing the same thing in many places, we can just write one function read_yaml it once in a file called "utils/common.py." 
This way, we can easily reuse that piece of code wherever we need it in our project. It helps keep things organised and saves us from writing the same code over and over again.
### Basic functions
Other Function are there such as:
1. create_directories: Creates directories specified in the input list. It also logs the creation of each directory.
2. save_json: Saves data as a JSON file at the specified path.
3. load_json: Loads data from a JSON file and returns it as a ConfigBox object.
4. save_bin: Saves binary data to a file using the joblib library.
5. load_bin: Loads binary data from a file using the joblib library.
6. get_size: Retrieves and returns the size of a file in kilobytes.

## Workflow
For creation of each and every module we’ll follow below Workflow.
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py
### Config.yaml
The config.yaml file organises key paths for various stages in a data science pipeline. It specifies locations for data ingestion, validation, transformation, model training, and evaluation, making it easy to manage and track artefacts. Adjust paths as needed for your project.
As and when we’ll keep on adding pipelining we’ll keep on updating the artefacts into the config.yaml.
1. Data Ingestion pipeline : this step require two changes:
   - Update config.yaml: add data_ingestion section with the values we need.
   - Create a data_ingestion.ipynb:  this file where we’ll be writing all the code after that we’ll integrate the code into the final project. Do your research and as per the need create all the necessary classes and methods in research/01_data_ingetion.ipynb.
   To run your notebook with the conda python environment in VSCode, select the kernel from the upper right menu and choose "env" (conda environment). Alternatively, from your terminal, run `jupyter notebook research/data_ingestion.ipynb` and then open the link from the logs or http://localhost:8888/notebooks/data_ingestion.ipynb from your browser

   - Step-0 Update config/config.yaml with the content:
   - Step-1 Create a data_ingestion.ipynb file  where we’ll be writing all the code after that we’ll integrate the code into the final project
   - Step-2 Do your research and as per the need create all the necessary classes and methods in research/01_data_ingetion.ipynb.
   - Now we’ll convert this into modular coding. We’ll follow the same workflow in order to updating the files
   - Update the src/mlProject/entity/config_entity.py Module(Copy paste from ipynb file)
   - Update config/configuration.py in src with all the configmanager
   - Now we’ll update the component folder. Create new file data_ingestion.py and copy paste all the ingestion related code
   - For checking, let’s Try to execute Code from main.py file.Import all the component to main.py
2. Open the terminal and execute python main.py. You’ll be able to see data ingestion pipeline will get completed
Note:- if python main.py giving some issue try running with python3 main.py








