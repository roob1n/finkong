# Finkong
_Manage your finances like a Kong!_

![Finkong Logo](./app/static/images/finkong-logo-small.png)

## About the project
Finkong is an finance, budget and expense management application that is based on the micro web framework [Flask](https://flask.palletsprojects.com/) and was built as a group project in the Software Engineering (SWEN) module.

**Implemented features:**
- User Registration
- Login

**Planned features:**
- Account creation
- Expense tracking
- Budget creation

## Project setup & getting started

Create a virtual environment first and active it. Then install all dependencies, including Flask, from the `requirements.txt`.

```
pip install -r requirements.txt
```

### Database
Next create the database. For simplicity, this project uses SQLite, but feel free to exchange it with any other DB system. Then seed some test data into the database. 

```
flask --app app db-init
flask --app app seed-test
```
This creates a user `admin` with password `admin`, as well as some accounts and positions, so you can explore the application. Please ensure to delete the test data before deploying to production. 

### Run the application
Once the database has been set up, you can run the application using:
```
flask --app app run
```

This will start the local dev server and you can access the Finkong application in your browser under `http://127.0.0.1:5000/`.

## Authors
Finkong is developped by:
- [martn39](https://github.com/martn39)
- [roob1n](https://github.com/roob1n)