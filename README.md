1.	Make a directory in your terminal called flask-boilerplate and cd into it.
2.	Run git init.
3.	Run git s to check if it worked.
4.	Make .gitignore file.  Just copy and paste from another project. Cp = the command to copy in terminal
5.	Make a setup.py.  Just copy and paste from another project.  Maybe from the flaskr project.
Setup(
  change the name=‘flask-boilerplate’,
  version=‘0.0.0’,
  pacakages=find_packages(),
  include_package_date=True
  zip_safe=False
  install_requires = [
    ‘flask’,
  ],
  extras_require={
    ‘test’: [
      ‘pytest’,
      ‘coverage’,
    ],
  },
)
6.	Set up virtual environment python3 -m venv venv.  This is still in the flask-boilerplate directory.
7.	Run source venv/bin/activate to turn venv on
8.	Run which python to see if python is being ran in venv. In venv terminal
9.	Run python –version to see which version of python is being ran in venv. In venv terminal
10.	Run pip install -e .  To look for a setup.py file in the directory. Install required dependencies. In venv terminal
11.	Run pip install -e ‘.[test]’ to install all of our extras that we as developers need. In venv terminal
12.	Run export FLASK_APP=flask_boilerplate in venv terminal
13.	Run export FLASK_ENV=development in venv terminal
14.	Run git status
15.	Run mkdir flask_boilerplate in venv terminal & cd into it
16.	Then create __init__.py file in the directory in venv terminal
a.	From flask import Flask
b.	Def create_app():
      app = Flask(__name__)

      @app.route(‘/’)
      def index():
	      return ‘Hello, World!’

    return app
    
17.	Run flask run
18.	Type 127.0.0.1:5000 into browser to see if everything runs.
