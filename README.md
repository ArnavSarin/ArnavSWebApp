This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### Background:
Hi, My name is Arnav Sarin. I worked on this project with REACT for FRONT-END and Python as the BACK-END. I made this app primarily to learn how to create a NAIVE BAYES MODEL to detect COVID based on patient data, play with GOOGLE's SPEECH TO TEXT API and learn REACT. At current the application converts speech to text and uses the text to determine where it should scroll the page. The user is also able to enter patient information from which a NAIVE BAYES MODEL in the BACK-END will determine if the patient has COVID or is Healthy. The BACK-END model is hosted on an ASGI server known as UVICORN (FAST API). The FRONT-END sends a post request to the NAIVE BAYES MODEL giving it the patient information on which its run. The training data for the NAIVE BAYES MODEL is a CSV file found from Kaggle. 

***Here is a link to the demo video showing how the project works.***
https://youtu.be/jBmRKdcB0Xw 



### Tech Stack:
Bootstrapped with React (JS,HTML,CSS), Python



### SET UP:
To start the WEB APP, use: 'npm start' in the FRONT-END terminal

To start the ASGI server, use: 'uvicorn naivebayes:app --reload' in the BACK-END terminal

***Additional Information:*** I ran this in Python 3 and used pip3 to install any additional libraries for the BACK-END. I also did not include the node_modules folder. 



### FUTURE: 
Future updates I hope to add are the ability to resize the elements in the web app to adjust based on screen size. I will also work on changing my dataset to one that is more accurate. I hope to add more algorithms to this WEB APP in the future. 
