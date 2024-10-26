# Test Credentials

```
// Test User Account

username:  test
password:  TestTest$1

```

# Instructions    

- DEMO Video - [Google Drive](https://drive.google.com/file/d/1f7LIGofwd5p8jTvhb9BVMBtC6MNggrEx/view?usp=sharing)

- Requirement Doc : [Google Doc](https://docs.google.com/document/d/1RzjyOrZkwwin_Ax0873stRanf0hr9XFmvAR-YE-MACM/edit)    

After cloning this repository, you need to initiate a virtual environment. Then install necessary packages within it.

1. Go to project directory
```console
cd phitron-django-004
```
Here `library_management_project` is the project folder, where the `settings.py` is the root settings file for the whole project, `urls.py` is the main url pattern handler. (CEO Shaheb 😉)    


2. Run the command given below to create a virtual environment within the .venv directory
```console
# For Linux/MacOS
python3 -m venv .venv
```

```console
# For Windows
python -m venv .venv
```
**You need to do this once, after cloning the project. .venv folder is ignored within .gitignore file**    


3. Now run the command below to activate the virtual environment.
```console
# For Linux/MacOS
source .venv/bin/activate
```

```console
# For Windows
.\.venv\Scripts\activate
```


4. Now run this once to install all the packages
```console
pip install -r requirements.txt
```


5. You are good to go. To start the development server, simply run
```console
python manage.py runserver
```
**Important [❗]: The server no longer runs on the default port `8000`. Instead, it runs on port `10000` since render supports this port. Simply open `http://127.0.0.1:10000` to se the development server**

**Important [❗]: manage.py file is modified to run `10000` as the default port.**

**Make sure you are within the right directory by entering `ls` or `dir` command to check if manage.py exists**    


# Solve Deploy Issue
- Solved deploy related issue by following this blog below, and set the default port 10000 for render specific platform rule 
    - [GeekForGeeks](https://www.geeksforgeeks.org/change-the-django-default-runserver-port/)
- Read Render Documentation about Open ports for Web Services
    - [Render Doc](https://docs.render.com/web-services?_gl=1%2Addqpg9%2A_gcl_au%2AMTc0NjU2MjE3Ny4xNzI2OTA0NjA3%2A_ga%2AMTI1MzYwNDY3Mi4xNzE5MDM4Mjg0%2A_ga_QK9L9QJC5N%2AMTcyOTg4NDA4NS43LjEuMTcyOTg4NjUyNS41OS4wLjA.#port-binding)
