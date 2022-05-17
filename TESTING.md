# **Testing** 

* [Validation](#Validation)
* [Functionality Testing](#functionality-testing)
    * [User Story Evaluations](#user-story-valuations)
* [Automated Testing](#automated-testing)
* [Bug Fixes](#bug-fixes)
* [Known Bugs](#known-bugs)


## Functionality Testing



### User Story Evaluations

As part of my functional testing I reviewed my intial user stories. For quick reference I have highlighted the completed user stories in <span style='color:#28a745;'>green</span>, those that are not implemented in <span style='color:#dc3545;'>red</span>, and features that have some implementation in <span style='color:#ffc107;'>yellow</span>.

I have also included a brief summary of how each user story was implemented or why I chose not to add the feature. 

#### **Users should be able to create an account so their settings can persist over multiple sessions.** 
* <span style='color:#28a745;'>As a user I can create an account so that my ingredient selections are saved between sessions</span>

    __*I used allauth to create a robust account management system and I linked this to a user data model allowing the user data to persist inbetween sessions*__

* <span style='color:#28a745;'>As a user I can log out and in so that my account is secure</span>

    __*I used all auth's built in templates to create a logout page that is easily accesiable from all pages*__

* <span style='color:#dc3545;'>As a user I can delete my account so that if I am no longer using the service I don't have any information stored on the app</span>
    
    __*I have yet to implement a delete account function as it was not nesesary for the app to function. This is a feature that will potentially be developed later*__

* <span style='color:#28a745;'>As a user I can add an email address to my account so that I can recover my account if I forget my password</span>

    __*There is a password reset feature included in the allauth libary.*__

* <span style='color:#dc3545;'>As a user I can change my account details so that I can increase security</span>

    __*Users can change some of their account details but I haven't implemented the functionality to completly change all details yet as it made more sense to focus more on core app functionalty.*__

#### **Users should be able to get cocktail recommendations based on what ingredients they have.**

* <span style='color:#28a745;'>As a user I can get a randomly generated drink recommendation that I can make with ingredients that I have so that I can use the app to make a drink</span>

    __*The app will only recommend drinks if the user has all the ingredients.*__
* <span style='color:#28a745;'>As a user I can reject the recommended drink so that I can have a drink that better suits my tastes</span>

    __*The app prompts users to reject or accept a drink when generating a recipe.*__

* <span style='color:#ffc107;'>As a user I can rate drinks so that I not suggested drinks that I didn't like</span>

    __*Users can add a recipe to a disliked list. Though at the moment the app doesn't filter out the drinks the user has disliked. In future I would like to add a disliked filter but at the moment it falls outside of core app functionality.*__

#### **Users should be able to submit their own cocktail recipies.** 

* <span style='color:#28a745;'>As a user I can submit my own recipes so that I can share my knowledge

    __*There is a user submitted cocktail form easily accesable from the main page.*__

* <span style='color:#dc3545;'>As a user I can get email notifications when my recipes are approved/ rejected so that can keep track of my submissions</span>

    __*Implementing an email system became too difficult to implement in the timeframe I had and did not impact on the core functionality of the app.*__
* <span style='color:#28a745;'>As a admin I can approve user submitted cocktails so that I can maintain quality recipes</span>    

    __*Admins have access to the approval page from their accounts page where they can quickly approve recipes without having to go to the admin page.*__

* <span style='color:#28a745;'>As a admin I can automatically update ingredient list when approving user submitted recipes so that reduce data entry time</span>

    __*When approving user generated cocktails any ingredients are automatically added to the correct database.*__
* <span style='color:#dc3545;'>As a admin I can get emails letting me know when a recipe is submitted so that I can approve recipes quicker</span>

    __*Implementing an email system became too difficult to implement in the timeframe I had and did not impact on the core functionality of the app.*__

* <span style='color:#ffc107;'>As a admin I can modify user submissions so that I can ensure a base level quality for all recipes</span>

    __*An admin approval system was implemented but at the moment it only allows minor changes to recipes. More detailed changes are able to be implemented from the admin panel. As this only impacted on the site admin and did not negaitivly impact on the user expeiance it was deemed low priorty.*__

#### **Users should be able to easily update their ingredients.**

* <span style='color:#28a745;'>As a user I can select which ingredients I have so that I am only suggested drinks that I can make</span>

    __*Users can update modifiers and ingredients. Whenever a new recipe is called for the app checks the users ingredients/ modifiers and cross references it with the recipes to only offer drinks the user can make.*__

## Automated Testing

I created a series of Jest test suites to ensure that my javascript files worked as expected. 

I also created unitest test suites for the dob_check functions and the new_recipe functions.

All test files are included in the repo. 

<span style='color:#dc3545;'> **Note;** when running the unitest tests the database needs to be changed in the project_drinkr settings.</span> 

To set up the database for testing you have to comment out the working database and add back in the test database. This will allow you to run the unit tests. 

Once the tests have been run you will need to reverse any changes you made to the setting files. 

I have included some images showing how the settings should look when testing or in production 

#### **Production;**

![database change 1](./static/images/database-change-1.png) 

#### **Testing;**

![database change 2](./static/images/database-change-2.png) 
