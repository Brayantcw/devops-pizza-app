# DevOps Pizza App

Welcome to the DevOps Pizza App repository! This application showcases DevOps practices within a pizza ordering and delivery system.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Future Improvements](#future-improvements)
- [Iac](#iac)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This guide provides instructions for installing and running the DevOps Pizza App.

## Installation
To run the application locally, follow these steps:

### Install Tools
Ensure you have the following tools installed:
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Docker Desktop](https://docs.docker.com/desktop/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download)
- [Helm](https://helm.sh/docs/intro/install/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Install Application
- Clone the  repository using: 
  ```
  git clone https://github.com/alezanper/devops-pizza-app
  ```
- Start minikube:
  ```
  minikube start
  ```
- Install the application using helm:
  ```
  helm install helm-mypizzapp ./helm-mypizzapp
  ```
- Test the application locally by forwarding the port:
  ```
  kubectl port-forward service/helm-mypizzapp 8080:8080
  ```
- Validate the application on a web browser
  ```
  http://localhost:8080/myapp/
  ```

## Usage
Once installed, the application offers the following features:

### Features
1. **Create Orders**: Users can place orders by specifying the type of pizza and leaving a message.
- URL: `http://localhost:8080/myapp/`

2. **View Orders**: Administrators can view and validate incoming orders.
- URL: `http://localhost:8080/myapp/display_data/`

## Future Improvements
In future versions, the following improvements can be made:
- Implement user authentication with separate views for users and administrators.
- Deploy the application to a Kubernetes cluster in a cloud environment like Amazon EKS. As example I added a module and the basic terragrunt file to deploy a eks cluster. Please refer to IAC section for further details

## Iac
- The application can be installed on an EKS cluster. Since I don't have an AWS account to test it, I decided to generate the basic templates (Terraform module and Terragrunt file for EKS) as examples.
- Using Terraform/Terragrunt and a GitHub workflow, the Terragrunt plan and apply can be configured to deploy an EKS cluster. A similar process can be used to add a Helm release module for deploying the application.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests.

## License
This project is licensed under the [MIT License](LICENSE).