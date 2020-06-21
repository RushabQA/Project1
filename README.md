**The Wonderful World Of Food App**

**Contents**

- Brief
  - Additional Requirements
  - My Approach
- Architecture
  - Database Structure
  - CI Pipeline
- Project Tracking
- Risk Assessment
- Testing
- Known Issues
- Future Improvements
- Authors

**Brief**

The main brief of this project was to create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training. The goal of the app is to allow a user to create, read, update and delete an entry they have made.

**Additional Requirements**

Additional requirements to ensure an efficient plan, a faultless build and execution:

- A Trello board for project tracking
- An entity relationship diagram that consists of at least two tables that model a relationship
- Clear documentation that shows the project in the design phase, application architecture and a detailed risk assessment
- A functional CRUD application created using python
- Testing
- A fully functioning front-end website
- Use of a version control system through a CI server (Jenkins)

**My approach**

The application I chose to create is a food app, in essence it is a giant cookbook which allow users to upload and share their own tried and tested recipes as well as browse ones that already exist. 
A user will be allowed to create an account, which will then allow them to create, read, update and delete recipes. However, you can still browse through the recipes without creating an account. A user will first need to assign a cuisine/region to their dish before they add their creation. The following information would then be needed to create and add a recipe:

1. The Recipe Name
2. Meal type _(breakfast, lunch, dinner, snack)_
3. Dietary Requirements _(vegan, vegetarian, meat)_
4. Difficulty _(easy, medium, hard)_
5. Number of Servings
6. Ingredients
7. Method
8. Cuisine

Additionally, I would have liked to add a process that allows the user to upload a photo showing what the dish looks like after it has been prepared. Also, a search bar which would allow a user to search for a particular recipe either by name or browse by cuisine.

**Architecture**

_Database Structure_

I have created an entity relationship diagram to show the structure of my database and the relationships taking place between the tables.

The ERD above shows my database models a 1 mandatory to many optional relationship between User and Recipe and a one to many relationship between cuisine and recipe. While the primary and foreign key allow the tables to be linked.

I had also hoped to add another table to the database which would store images of the dish that users create.

**CI pipeline**

The continuous integration pipeline allows for an efficient, streamlined and autonomous process of development and deployment of an application. Thus, reducing the time between when a project is being updated and going live.

The process is as follows:

- A trello board is used for project tracking
- Code is developed in python on my local machine
- A flask application is deployed on the virtual machine which connects to a SQL server to access the database I created.
- Unit testing such as &quot;pytest&quot; can be done to validate that each unit of software performs as designed.
- It can then be pushed and pulled to a git version control system (GitHub)
- It will then automatically push the new code to Jenkins via a webhook in order to automate the process of updating the environment
- Further tests can be carried out on the app here.
- The application is also created with debugger mode active, which allows for dynamic testing.

**Project Tracking**
My Trello board: https://trello.com/b/7I7DiCwU/my-app

I used trello to track the progress of my project from planning all the way to testing and completion. I have also added a priority system (low, medium, high) that indicates the importance of each individual process. High priority being the processes where I should most of my time on to complete and low being can look into in my spare time.

**Risk Assessment**

I have outlined potential risks, their impacts and mitigation techniques that I may need if my application is breached.
file:///C:/Users/rn_28/Documents/Risk%20Assessment.pdf

**Testing**

I used pytest to run unit tests on my application. These are designed to test a function. If the test result returns the expected result, the test passes. Jenkins was used to provide information on which tests have passed and which have failed through the console output. A Debugger mode was also active throughout development to allow for dynamic testing.


As the diagram above shows I had 55% coverage, but I had a few failed tests unfortunately. As my front-end application is working seamlessly, I must assume the failed tests are a result of errors while writing each test.

**Known Issues**

There are currently a few issues with my unit testing and coverage. Also, my CI integration with Jenkins is not fully functional as the build process is still constantly running without and progress.

**Future Improvements**

I have a few ideas and improvements I want to implement in the future for my project.

- Firstly, I would like to include an option where a user can post pictures of what their dish looks like as well as videos of the preparation.
- Secondly, I would like to include a search bar which would allow a user to seamlessly look for a certain recipe, either by searching its name or cuisine type.
- Thirdly I would like to include a ratings system (thumbs up and thumbs down) that would allow other users to show their feelings towards a dish.
- I would also like to add more unit tests to achieve a better coverage to ensure that all aspects of my application and database are being tested.
- Finally, I would like to implement a better front-end design for my application, thus making it aesthetically nicer looking.

**Authors**

Rushab Shah
