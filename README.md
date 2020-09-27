This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### Background:
Hi, My name is Arnav Sarin. I worked on this project with **React** for FRONT-END and **Python** as the BACK-END. I made this app primarily to learn how to create a **NAIVE BAYES MODEL** to detect COVID based on patient data, play with **GOOGLE's SPEECH TO TEXT API** and learn React. At current the application converts speech to text and uses the text to determine where it should scroll the page. The user is also able to enter patient information from which a NAIVE BAYES MODEL in the BACK-END will determine if the patient has COVID or is Healthy. The BACK-END model is hosted on an ASGI server known as **UVICORN (FAST API)**. The FRONT-END sends a post request to the NAIVE BAYES MODEL giving it the patient information on which its run. The training data for the NAIVE BAYES MODEL is a CSV file found from Kaggle. 

***Here is a link to the demo video showing how the project works.***
https://youtu.be/jBmRKdcB0Xw 



### Tech Stack:
Bootstrapped with React (JS,HTML,CSS), Python



### SET UP:
To start the WEB APP, use: 'npm start' in the FRONT-END terminal

To start the ASGI server, use: 'uvicorn naivebayes:app --reload' in the BACK-END terminal

***Additional Information:*** I ran this in Python v. 3.7.3 and used pip3 to install any additional libraries for the BACK-END. I did not include the node_modules folder in the FRONT_END. Google's speech to text API only works on chrome.



### FUTURE UPDATES: 
1. Resizing elements in the web app to adjust based on screen size.
2. Improving my dataset to one that is more accurate. 
3. Playing with more machine learning algorithms. Ideally I would like to work with a heart disease dataset. I would also like to learn other algorithms perhaps Computer Vision related or NLP related. 
4. Improving the UI for easier access/use. 
5. Using random forests for more accurate results. 
