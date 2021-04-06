# repo to learn flask-gui
learning from the [the-flask-mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

# setting up the env
## create virtual env
```bash
python3 -m venv venv
# connect to virtual env
source venv/bin/activate
```

## installing packages
```bash
pip install -r requirements.txt
# if you have installed new packages and need to save them, you can use the following
pip freeze > requirements.txt
```

# Running the server
```bash
# Flask needs to be told how to import it, by setting the FLASK_APP environment variable
export FLASK_APP=microblog.py
# start server
flask run
```
