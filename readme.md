# EC2 Reporter 

## Dependencies

### Backend (Python 2.7)

1.) Flask: http://flask.pocoo.org/ 

2.) boto3: https://boto3.readthedocs.io/en/latest/

### Front-End 

1.) Angular 1.6: https://docs.angularjs.org/guide

2.) Google MDL: https://getmdl.io/

## Instructions 

### Normal

1.) Open terminal navigate to containing folder. 

2.) With flask installed run "flask run"

3.) Navigate to localhost:5000 in your browser

### Container

VIA: https://github.com/tiangolo/uwsgi-nginx-flask-docker

#### NOTE: Will run with the container images default python 3.5 - Code is functional on 2.7

1.) docker build -t ec2-reporter .

2.) docker run -d --name ec2Reporter -p 80:80 ec2-reporter

3.) Navigate to localhost
