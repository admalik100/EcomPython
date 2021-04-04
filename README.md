# EcomPython

<h2> Overview </h2>
<p>This is a prototype project for GUI automation for Ounass website.
This project makes use of python to develop framework for automation.
Currently all tests are created in a **UNIT Test** framework of python.</p>


<h2>How to</h2>
<p>you'll need python installed and present in the system that you want to run the project on. Python version used for development of this framework is "Python 3.9"</p>
<p>The project contains a "requirement.txt" file that contains all dependencies required to run this project.
To run the project simply run either "pip install -r requirment.txt" or 
"pip3 install -r requirement.txt", depending on whether you have pip or pip3 available.</p>
<p>The above mentioned command will install all the required packages.
After installing these packages, to run the project cd into main directory i.e. EcomPython and run the following command: "python3 -m Models.Test_Main.py" 
(python3 or python which ever you have installed and available)
This command may not function properly , a work around is mentioned below</p>
<p>Currently the chromedriver path and reports path is mentioned in CheckOut.py and FbLogin.py as "../Drivers/chromedriver" , this seems to not be recognised by terminal. Kindly change the paths to complete path.
eg "/Users/mac/Documents/EcomPython/EcomPython/Drivers/chromedriver"</p>

<h2>Bugs</h2>
<p>Currenlty Chromedriver paths and reports paths are not being recognised by terminal unless absolute path is provided.
</p>

<h2>Improvements and Fixes</h2>
<p>Clean Git repo, maintained on github to remove the issues with contributors.
Clean commit history.
Code refactored/cleaned.</p>

<h2>Upcoming features</h2>
<p>The next release scheduled will improve on POM (Page Object Model) implementation.Currenlty the structure exists yet it is not implemented properly.
More modules will be covered.
Docker and jenkins implementation.</p>