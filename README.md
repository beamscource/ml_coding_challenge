# ML coding challenge

Your challenge is to create a system that can identify whether a picture is a boot, a shoe or a sandal.  
By doing so, you need to complete the following tasks:

:arrow_forward: Build the model
  - Since the dataset contains only a limited number of samples, please focus on just creating a simple model with acceptable performance, it doesn't need to be perfect
  - You are free to choose whatever approach you deem relevant to achieve this task

:arrow_forward: Create a backend service for issuing predictions
  - We've provided a simple REST-Api (`app.py`) which has a `/score`-Endpoint that should be used for getting predicitons
  - Right now this endpoint is just an empty shell that is calling an internal function just to return some dummy data without any regard to the actual Data
  - To complete this task you need to extend the `/score` endpoint, it should take an image file and return the predictions of your model whether it's a boot, shoe or sandal

:arrow_forward: Create a small frontend application with streamlit
  - Please create an interface in which you can upload an image
  - The uploaded image should then be passed to the backend API
  - Once you got the predictions visualize the results




## Setup

To install all dependencies:

```
pipenv install
```


To start the application:

```
honcho start
```
