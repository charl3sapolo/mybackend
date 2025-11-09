# AN INVENTORY API FOR AN e-COMMERCE BUSINESS

This is a python based api in development, not yet hosted which includes some tables for storing data in database tables.
Framework used for the development is *Django* together with the built in `sqlite3` database.

## HOW TO RUN THE PROJECT

Running this project will involve some prerequisites which include;

- `Python` installed on your machine
- `Docker Desktop` installed too

## STEPS FOR RUNNING THE PROJECT

1. Pull this repository from github to you desirable location on your machine using the `git pull username\repo` command
2. After wards navigate to the sitebackend directory

>[!IMPORTANT]
>Activate the virtual environment before running the proceeding scripts since it's a python application

3. Run the `docker compose up` command on the terminal to start a container for the project

>[!TIP]
>Make sure the docker engine is up and running for this to work, this can be seen in your docker desktop tab

4. If you were to make changes on the code, make sure to re-build the image using the `docker build -t charles/mydjangoend .` which the _mydjangoend_ is the image name.
