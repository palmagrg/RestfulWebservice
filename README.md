# RestfulWebservice
Restful Webservice using Python Flask and Container
A docker container running flask python environment shows a good RESTful API example

Created a RESTful Web service that displays data of Skin Care product  in JSON format using four get routes:

I have used two JSON file. 


Dockerimage to run unoconv as a webservice using Flask and Flask-RESTful.

If you prefer a pre-build version it is available from hub.docker.com just do a regular pull

$ docker pull jordanorc/docker-unoconv-flask

Build the image using command: 

docker build -t docker-unoconv-flask .

Run the Docker container using the command: 

docker run -d -p 8000:8000 --name unoconvv jordanorc/docker-unoconv-flask

