# MLOps-ComputerVision

This repository contains an end-to-end deep learning project that leverages MLOps tools such as DVC (Data Version Control) for managing data and GitHub Actions for continuous integration and continuous deployment (CI/CD). The project also uses Docker for containerization. Below are the steps to set up the project.

## Tools and Technologies

- **DVC (Data Version Control)**: DVC is used for versioning and managing data.

- **Docker**: Docker containers are employed for environment consistency and reproducibility.

- **Flask**: Flask API that serves as the backend for the web app. The API provides endpoints for various functionalities, such as data processing and model predictions.

- **GitHub Actions**: GitHub Actions are used for continuous integration and continuous deployment (CI/CD) of the project.

- **Azure**: Mention Azure if it's part of your deployment process.

## Dataset

You can download the Tuberculosis (TB) Chest X-ray dataset from [Kaggle](https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset). 

## Project Setup

Follow these steps to set up the project on your local machine:

### Clone the repository:

```
$ git clone git@github.com:thiphan94/MLOps-ComputerVision.git
```
### Create a Conda Environment  
```
$ conda create -n cnn python=3.8 -y
$ conda activate cnn
```

### Install Requirements 
```
$ pip install -r requirements.txt
```
### Run the Application
```
$ python app.py
```
```
$ open up the local host and port
```

### DVC 
Initialize DVC:
```
$ dvc init
```

Reproduce the data pipeline:
```
$ dvc repro
```

View the DVC pipeline DAG (Directed Acyclic Graph):
```
$ dvc dag
```

## Azure CI/CD Deployment with GitHub Actions

### Run the following terminal commands:
```
$ docker build -t tuberculosisapp.azurecr.io/tuberculosis:latest .
$ docker login tuberculosisapp.azurecr.io
$ docker push tuberculosisapp.azurecr.io/tuberculosis:latest
```

### Deployment Steps
The deployment steps include:

    Building the Docker image of the source code.

    Pushing the Docker image to the respective container registry (AWS ECR or Azure Container Registry).

    Launching the web app server in Azure Web App service.

    Pulling the Docker image from the container registry to the deployment target and running it.


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml

## Contributing
If you want to contribute to this project, please fork the repository and create a pull request. We welcome contributions and improvements!

## License
This project is licensed under the MIT License.