# FastApi_DockerCompose

## Project Overview

This is a FastAPI project that now includes a frontend interface, enhancing the user experience and interaction. The project utilizes Docker Compose for seamless local deployment and Minikube for Kubernetes deployment, making it more scalable and reliable. 

The project follows a structured approach centered around the concept of "projects". Each project is characterized by a name, description, status, and an associated PDF file. The project leverages PostgreSQL as its database and Docker Compose to efficiently manage services, including volumes for storing the PDF files.

For Kubernetes deployment, we use Minikube, a tool that runs a single-node Kubernetes cluster in a virtual machine on your personal computer. This allows for testing the Kubernetes deployment in a local environment before moving to production.

The addition of a frontend interface provides a more intuitive way for users to interact with the projects. It is designed to be user-friendly, providing easy access to the project's features and functionalities.

## Reqiuirement
### Running local 
[Docker](https://www.docker.com/products/docker-desktop/) needs to be installed
### Running in Minikube
[Minikube](https://minikube.sigs.k8s.io/docs/start/) needs to be installed
<!-- [ArgoCd](https://argo-cd.readthedocs.io/en/stable/getting_started/) -->

## Project Structure


## Running the Project
Before running the project, you need to set up the following environment variables:

- `DB_USERNAME`: The username of the database.
- `DB_PASSWORD`: The password of the database.

To run the project locally, use Docker Compose:

```
docker-compose up
```
Then fast api swagger ui can be accessed at ```localhost:8000/docs```

To run the project in Minikube:
```
sh minikube_deploy.sh
```
Then to accesss the frontend :
```
minikube service frontend-service
```



