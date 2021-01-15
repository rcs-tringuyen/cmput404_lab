# Lab 1: Virtualenv &amp; cURL

## Git and GitHub
- Make a GitHub account or log in to your existing GitHub account.

### Question 1: What is your GitHub URL?

## virtualenv
- Create a new directory for this lab (mkdir).
- cd into the created directory and initialize a new git repository (git init).
- Try installing requests.
- `pip install requests`

- Make a Python script that prints out the version of the requests library.

### Question 2: What version is the requests library installed on the system?

- Create a virtualenv.
- `virtualenv venv --python=python3`
- Activate the python virtual environment.
- `source venv/bin/activate`
- Try installing requests into your virtual environment.

- Run your Python script that prints out the version of the requests library in your virtualenv.

### Question 3: What version is the requests library installed in the virtualenv?

- Open a new terminal.
- Run the script in your new terminal.

### Question 4: What is the difference between the virtual environment and the not virtual environment python?

## curl
- Use curl to get the Google homepage: http://google.com/
- This time, use curl -i to get the Google homepage.

### Question 5: What status code is returned for http://google.com ? What URL must you visit to get a 200 status code?

- Curl the Google home page with -iL and examine the headers.
- Curl the Google Teapot page: https://www.google.com/teapot

### Question 6: What status code is returned for http://google.com/teapot? Is it the one returned by curl -i or curl -iL? What happens when you curl http://www.google.com/teapot?

- Modify your Python script to GET the Google homepage.
- Try `curl -i https://webdocs.cs.ualberta.ca/~hindle1/1.py`
- Try it again `curl -i -X POST -d "X=Y"`

### Question 7: What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py when you used -X POST? What is this method useful for?

- Commit your Python script and push it to GitHub.
- Find the raw URL to your Python script on GitHub.
- Modify your Python script so that it downloads itself from GitHub and prints out its own source code from GitHub.
- Push the new version of your Python script to GitHub.

### Question 8: What is the raw URL to your Python script on GitHub?

