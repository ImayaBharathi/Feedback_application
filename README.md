# Feedback_application for H20

This is a feedback application having options for rating, comment and a file submission. 

# Prerequisite

* [Docker Compose]
* [Docker]
* [Ports] : 3306,5000 need not be occupied
* Provide realpath of git folder location on docker-compose.yml file
 use the below command in terminal inside git folder to find the absolute path
```sh
$ realpath .
```

# Command For Startup

Run the below command in terminal inside the cloned repository

```sh
$ docker-compose up --build
```
