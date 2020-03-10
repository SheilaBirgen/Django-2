## InstaPic
### Description
InstaPic is a platform where users can upload  their photos and add caption to the photos for friends  to view, like and comment on the photos.Users can also follow each other, see their profile with all the photos they've posted and see their friends photos on their timeline too.

### Installation Process
##### Download any text editor of your choice, either Sublime, Visual-Studio-Code or Atom.
##### Install your preferred version of python
  - ```sudo apt-get install python3.7```.
  - ```python --version``` to confirm that python has been installed.
##### Open the command-line and run the following command to open a directory:
  - ```cd your preferred directory``` => ```cd Desktop```
##### Git clone the project on your current directory by:
  - ```https://github.com/SheilaBirgen/Django-2```.
##### Move to your project directory:
- ```cd Django-2```.
##### Open the project on your terminal:
  - ```atom . or code .``` , according to the type of your text editor.
##### Install virtual environment using python:
  - ```python3.7 -m venv virtual```, check your project to confirm you have a folder called virtual,
  - then activate it by running ```source virtual/bin/activate```
##### To install the packages in the ```requirements.txt file```,
  - ```pip install -r requirements.txt```  That will install all packages including Django.
##### To open python shell:
  - ```python3.7``` ,
  - ```import django```
  - And lastly ```django.get_version()``` to see and confirm the version of django installed.
  - You can then ```ctrl z``` to get out of the shell,
##### After ensuring you have all the above
  - ```python3 manage.py runserver``` to run the project.
  - Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.

## Technologies Used

- dj-database-url==0.5.0
- Django==1.11
- django-bootstrap3==12.0.3
- django-heroku==0.3.1
- Pillow==7.0.0
- psycopg2==2.8.4
- python-decouple==3.3
- whitenoise==5.0.1

## Known Bugs
There are no known bugs at the moment

## Support and contact Details
You can reach out to me through the github account SheilaBirgen
or on my email as jeronobergen@gmail.com

## License
@2019 Sheila Birgen 
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)