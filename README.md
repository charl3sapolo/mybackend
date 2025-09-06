WELCOME TO A INVENTORY AND RECEIPT GENERATING API
FEATURES
  **Allows you to register a company**
  **Allows you to store items**
  **Allows you to generate a receipt**

HOW TO RUN THE PROJECT(CURRENTLY IN DEV)
1. Pull from the repository
2. Make sure you have python installed in your system
3. Create a virtual enviroment using the following command in your terminal
  >py -m venv .venv
  Or if using VSCode press "Ctrl+shift+p" to access command palette and search for "Create environment"
  afterwards select ".venv" to create a virtual environment automatically
4. Make sure to have Docker installed in your system since it uses docker containers to run the project
5. In the root directory of the project use the command
   >docker compose up
   to run the project
6. If you were to make changes to the project, save them and then use the command
   >docker build -t charles/mydjangoend .
   to build the project with the given changes

Feel free to add anything of value :)
