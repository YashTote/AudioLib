
# Project Title

Hey! Welcome to the Audio Library React-Django application. This is a audio Library that allows you to ADD-PLAY and DOWNLOAD the audio files.
  
**Setting up the Project**

 Clone this repository using the link ` https://github.com/YashTote/AudioLib.git `. Enter the AudioLib directory `cd AudioLib`. You might see this: 
 ```
 audiofile-react 
 saveAudio
 requirements.txt
 ```
 In order to start the development version of the AudioLib application, we need a virtual environment. Make sure you have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed for the Django backend as well as [NodeJs](https://nodejs.org/en/download/current) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) for the React frontend. 
 
 Now in the same directory we need a [virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) in order to install backend specific dependencies. It is recommended to use the official [Python](https://www.python.org/downloads/) version  only instead of using one from third party python version managers ex : pyenv etc. This makes sure that the project runs smoothly.

**RUN following to start the backend server:**
 ```
 pip install virtualenv
 python3 -m venv env
 source env/bin/activate
 
 ```
 This starts our virtual environment and we are ready to install the necessary dependencies.

 ```
 pip install -r requirements.txt

 ```

 After the dependencies are sucessfully installed `cd saveAudio` and run `python3 manage.py createsuperuser`, enter the necessary details in order to access the SQLite database admin panel. Now run `python3 manage.py runserver`. 
 
> **Note**
> Make sure your server runs on [localhost:8000](http://localhost:8000/) only. Failure to do this will cause dashboard to connect with the front end. Or else edit the fetch addresses in the react frontend to your custom version of django server.
 
 > [!NOTE]
 > If you face the _sqlite3() error head to [this](https://www.codethebest.com/python-package-errors/modulenotfounderror-no-module-named-sqlite3-solved/)

**For starting the frontend server :**

In a new terminal window head to the audiofile-react directory and run :
```
npm install
npm run dev
```


**Using the application**
