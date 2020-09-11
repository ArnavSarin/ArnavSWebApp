import React from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
import './App.css';
  


/*BUGS: TYPING COVID DETECTION DOES NOT TAKE YOU DOWN TO THE CORRECT SPACE. ONLY SPEAKING WORKS */

  function App(){

    const { transcript, resetTranscript } = useSpeechRecognition()

    SpeechRecognition.startListening({continuous : true, language: 'en-US'})

    if (!SpeechRecognition.browserSupportsSpeechRecognition()) {
      console.log("This browser does not support speech recognition.")
      return null
    }


    // const Search = (searchquery) =>{
    //   searchquery = searchquery.transcript
    //   searchquery = searchquery.toLowerCase()
    //   console.log(searchquery)
    //   if(searchquery==="covid detection"){
    //     var div = document.getElementById("target")
    //     div.scrollIntoView();
    //     console.log("Got here");
    //   }    
    // }

    const Search = () =>{
      var doc = document.getElementById("fname")
      var searchquery = doc.value
      searchquery = searchquery.toLowerCase()
      console.log(searchquery)
      if(searchquery==="covid detection"){
        var div = document.getElementById("target")
        div.scrollIntoView();
        console.log("Got to COVID DETECTION");
      }    
      if(searchquery==="results"){
        var div = document.getElementById("Results_Val")
        div.scrollIntoView();
        console.log("Got to RESULTS");
      }    
    }

  

    const SubmitCovid = (check) =>{

        
        console.log("got here")
        var fever = document.getElementById("Fever")
        console.log(fever.value)
        var body_pain = document.getElementById("BodyPain")
        console.log(body_pain.value)
        var age = document.getElementById("Age")
        console.log(age.value)
        var runny_nose = document.getElementById("RunnyNose")
        console.log(runny_nose.value)
        var difficult_breathing = document.getElementById("DifficultyBreathing")
        console.log(difficult_breathing.value)

        if(check){

          //formatting entries for post request 
          var fever_float = parseFloat(fever.value)
          fever_float = Math.round(fever_float)
          if(fever_float<=98.0){
            fever_float=98.0
          }else if(fever_float>=102.0){
            fever_float=102.0
          }

          
          console.log("Fever_float: ")
          console.log(fever_float)

          var body_pain_val = body_pain.value.toLowerCase()
          if(body_pain_val==="yes"){
            body_pain_val = 1.0
          }else if(body_pain_val==="no"){
            body_pain_val = 0.0
          }

          console.log("Body_pain_val: ")
          console.log(body_pain_val)

          var age_float = parseFloat(age.value)
          if(age_float>=0.0 && age_float<19.0){
            age_float = 1.0
          }else if(age_float>=19.0 && age_float<31.0){
            age_float = 2.0
          }else if(age_float>=31.0 && age_float<46.0){
            age_float = 3.0
          }else if(age_float>=46.0 && age_float<61.0){
            age_float = 4.0
          }else if(age_float>=60.0){
            age_float = 5.0
          }

          console.log("Age_float: ")
          console.log(age_float)

          var runny_nose_val = runny_nose.value.toLowerCase()
          if(runny_nose_val==="yes"){
            runny_nose_val = 1.0
          }else if(runny_nose_val==="no"){
            runny_nose_val = 0.0
          }

          console.log("Runny_nose_val: ")
          console.log(runny_nose_val)

          var difficult_breathing_val = difficult_breathing.value.toLowerCase()
          if(difficult_breathing_val==="yes"){
            difficult_breathing_val = 1.0
          }else if(difficult_breathing_val==="no"){
            difficult_breathing_val = 0.0
          }else if(difficult_breathing_val==="unsure"){
            difficult_breathing_val = 2.0
          }

          console.log("Difficult_breathing_val: ")
          console.log(difficult_breathing_val)

          //POST REQUEST
          let json_data = JSON.stringify({
            developer_data : "yes",
            inp_fever: fever_float,
            inp_body_pain: body_pain_val,
            inp_age: age_float,
            inp_runny_nose: runny_nose_val,
            inp_diff_breath: difficult_breathing_val
          });
          var request = new XMLHttpRequest();
          request.open('POST', 'http://127.0.0.1:8000', false);
          request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
          request.send(json_data);
          var json_response = request.responseText;
          var response_val = JSON.parse(json_response);
          var results_elem = document.getElementById("Results")
          results_elem.innerHTML = "Patient is " + response_val["patient"]

          //RESETTING ALL VALUES 
          fever.value = ""
          body_pain.value = ""
          age.value = ""
          runny_nose.value = ""
          difficult_breathing.value = ""
        
        }

    }


    return (
      <form>
         <div className="Big_Container">

          <div className="Small_Container_1">
           <h1>Arnav Sarin's WEB APP</h1>
          </div> 

          <div className="Small_Container_2">
            <label htmlFor="fname">
            Search:
            <input type="text" id="fname" name="name"  defaultValue={transcript} placeholder="Johnny Appleseed"/>
            </label>
          </div>

          <div className="Small_Container_3">
            {/* <input type="submit" value="Submit" id="submitbutton" onClick = {Search({transcript})}/> */}
            <button type="button" id="Submit" className="Submit" onClick = {() => Search()}> Submit </button>
          </div>

          <div className="Small_Container_6">
            <button id= "Reset" onClick={SpeechRecognition.stopListening.bind()} className="Reset">Reset Mic Button</button>
          </div>

          <div className="Small_Container_7">
            <p className="Instructions">Instructions: The text field can be filled by either typing or speaking. To fill the text field by speech just start talking into the mic. If you would like to reset the text field, click the reset mic button.</p>
          </div> 

          
          <div className="Small_Container_4" id="target">
              <p className="CovidHeader">COVID DETECTION SURVEY: NAIVE BAYES</p>
          </div>

          <div className="Small_Container_5" >
              <button id="Submit2" type= "button" onClick= { () => SubmitCovid(true) } className="Submit2">Submit Covid Results</button>
          </div>


          <div className="Small_Container_8_Title">
              <p className="FeverTitle">What is your temperature? (98-105 degrees)</p>
          </div>

          <div className="Small_Container_8">
              <input type="CovidTextField" id="Fever"  placeholder="98.1"/>
          </div>

          <div className="Small_Container_9_Title">
              <p className="BodyPainTitle">Are you experiencing body pain? (yes/no)</p>
          </div>

          <div className="Small_Container_9">
              <input type="CovidTextField" id="BodyPain" placeholder="yes"/>
          </div>

          <div className="Small_Container_10_Title">
              <p className="AgeTitle">Enter Age...</p>
          </div>

          <div className="Small_Container_10">
              <input type="CovidTextField" id="Age" placeholder="27"/>
          </div>

          <div className="Small_Container_11_Title">
              <p className="RunnyNoseTitle">Do you have a runny nose? (yes/no)</p>
          </div>

          <div className="Small_Container_11">
              <input type="CovidTextField" id="RunnyNose" placeholder="yes"/>
          </div>

          <div className="Small_Container_12_Title">
              <p className="DifficultBreathingTitle">Are you having difficulty breathing? (yes/no/unsure)</p>
          </div>

          <div className="Small_Container_12">
              <input type="CovidTextField" id="DifficultyBreathing" placeholder="unsure"/>
          </div>

          <div className="Small_Container_13_Title">
              <p className="ResultsTitle">RESULTS</p>
          </div>

          <div className="Small_Container_13" id="Results_Val">
            <p className="HealthyVsInfected" id="Results">Results Not Submitted</p>
          </div>

        </div>
      </form>
      

    );

}





export default App;
