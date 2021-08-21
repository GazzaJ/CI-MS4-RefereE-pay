![W3 Recipes](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/readme-header_1.jpg "W3Recipes")
# [**Testing & Bug Fixes**](https://ci-ms3-w3recipes.herokuapp.com/)
This document records all of the manual testing conducted on the W3Recipes app', and also lists the bugs and fixes recorded during the development of the app'.
The philosophy I have used throughout this build is to code, review and test each part of the website as I progressed, relying heavily on Google Dev tools throughout, for first pass testing.
______
## Table of contents
1. [User Story Testing](#user-story-testing)
2. [Functionality Testing](#functionality)
   - [Navigation Testing](#first-navigation)
   - [Registration / Log-in](#registration)
   - [Recipe Search & View](#recipes)
   - [Adding a Recipe](#add-recipe)
   - [Manage Recipes](#manage)
   - [Edit a Recipe](#edit-recipe)
   - [User Profile](#user-profile)
   - [Edit Profile](#edit-profile)
   - [Delete a Recipe](#delete-recipe)
3. [Appearance Testing](#appearance)
4. [Code Quality & Validation](#code-validation)
5. [Usability Testing](#usability)
6. [Responsiveness Testing](#responsiveness)
7. [Performance Testing](#performance)
8. [Security Testing](#security)
9. [Bugs & Issues](#bugs)  

______

### **User Story Testing** <a name="user-story-testing"></a>
The following testing has been carried out to validate how the website addresses each of the user stories:
|User Story|Description|Testing|
|:--------:|-----------|-------|
| 1 |_As a_ **first time visitor**, _I need to_ **understand the purpose of the site**, _in order to_ **consider exploring the site further**|The landing page explains the purpose of the site in both text and imagery. instances of a recipe card and the world map from the dashboard have also been included |  

![User Story 1](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-1.jpg)
![KM Feedback](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/km-feedback-2.jpg)


|User Story|Description|Testing|
|:--------:|-----------|-------|
| 2 |_As a_ **first time visitor**, _I need to_ **quickly and easily register on the site**,  _in order to_ **fully interact with the site**| There are three links on the Landing page from which any first time user can access the registration page. The registration process is very simple and only requires a username and password |  

![User Story 2](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-2.jpg)
![KM Feedback](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/km-feedback-1.jpg)


|User Story|Description|Testing|
|:--------:|-----------|-------|
| 3 |_As a_ **first time visitor**, _I need to_ **easily access the recipe collection**, _in order to_ **search for a recipe worth making**| Once signed-up a new user can easily navigate to the main recipes page, using the navbar, where they have the ability to browse, filter and search the recipes and choose which recipe they would like to see in more detail.|  

![User Story 3](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-3.jpg)


|User Story|Description|Testing|
|:--------:|-----------|-------|
| 4 |_As a_ **returning user**, _I need_ **an interface where I can upload and save my recipes**, _in order to_ **share my favourite recipes with other site users**| An **"Add Recipe"** page has been provided and is clearly indicated on the navbar. This redirects the user to an intuitive form where they can input pre-defined recipe criteria like ingredients and preparation steps |  

![User Story 4](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-4.jpg)  


|User Story|Description|Testing|
|:--------:|-----------|-------|
| 5 |_As a_ **returning user**, _I need to_ **have the ability to edit or delete a recipe I have uploaded** _in order to_ **make changes to, or remove an out of date or incorrect recipe**| Returning users can use the Manage Recipes page to either edit or delete previously uploaded recipes. Access is restricted to their own recipes |

![User Story 5](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-5a.jpg)  
![User Story 5](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-5b.jpg)
![User Story 5](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-5c.jpg)

|User Story|Description|Testing|
|:--------:|-----------|-------|
| 6 |_As a _ **site owner**, _I need to_ **ensure some basic access control to edit and delete functionality**, _in order to_ **prevent unauthorised editing or deletion of user uploaded data**|Users are only able to view their own recipes on the Manage Recipes page. Users will be redirected to the Manage Recipes Page if they try to manipulate a URL from a Full Recipe view to an Edit Recipe view|

![User Story 6](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-6a.jpg)  
![User Story 6](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-6b.jpg)  


|User Story|Description|Testing|
|:--------:|-----------|-------|
| 7 |_As a _ **site owner**, _I need to_ **have a unique feature which generates some competition, _in order to_ **encourage users to post new recipes**.| One of the key drivers with W3Recipes is to to try and fill in the map of the world by uploading recipes from as many countries as possible. The maps are displayed on the Landing page and in a Dashboard Page| 

![User Story 7](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-7.jpg)
![Dashboard feedback](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/toto-feedback.jpg)
  
______

### **Functionality Testing** <a name="functionality"></a>
The following tables capture the functional testing performed on the web-app to ensure it works as desired. I have tested on the listed browsers only, using Windows version 1909 (OS Build 18363.1500), and have not conducted any backward compatibility testing in older browser versions.  

#### **First Time Navigation Testing** <a name="first-navigation"></a>
Tests the initial navbar selections _( Home | Sign-up | Log-in )_ and various anchor links provided to assist users navigating between pages.

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|   001  | Sign-up Link on Navbar |Correctly navigate to sign-up page | Opens Sign up/registration page | **PASS** | **PASS** |
|   002  | Sign-up Link on Log-in Page |Correctly navigate to sign-up page| Opens Sign up/registration Page  | **PASS**  | **PASS** |
|   003  | Sign-up Link on Landing Page |Correctly navigate to sign-up page| Opens up the Sign-up Page | **PASS** | **PASS** |
|   004  | Sign-up anchor link on the base of the landing page |Correctly navigate to sign-up page| Opens the Sign-up Page | **PASS** | **PASS** |
|   005  | Log-in Link on Navbar |Correctly navigate to Log-in Page | Redirects user to Log-in Page | **PASS** | **PASS** |
|   006  | Log-in Link on Sign-up Page |Correctly navigates to Log-in Page | Redirects user to Log-in page | **PASS**  | **PASS** |
|   007  | Home Link on navbar |Correctly redirects users to the Home Page | Redirects to Home Page | **PASS** | **PASS** |
|   008  | Brand Logo on navbar |Correctly redirects users to the Home Page | Redirects to Home Page | **PASS** | **PASS** |

___

#### **Registration/Log-in Testing** <a name="registration"></a>
Testing the registration process required to Sign-in and create a new account; as well as for returning users to Log-in to their existing account. The app should provide feedback to the user in cases where incorrect inputs are provided. 

|   Test   | Purpose         | Desired Result | Actual Result | Chrome v 87.0.4280.88 | Firefox v 84.0 (64-bit) |
|:--------:|-----------------|----------------|---------------|:------:|:-------:|
|   001    |Username - special Characters not allowed | Indicate requirements not met  | Input box turns red and tooltip provides feedback | **PASS** | **PASS** |
|   002    |Password - special Characters not allowed | Indicate requirements not met  | Input box turns red and tooltip provides feedback | **PASS** | **PASS** |
|   003    |Minimum Character limit (5) | Indicate requirements not met | Input box turns red and tooltip provides feedback | **PASS** | **PASS** |
|   004    | Max character limit (15) | Indicate requirements not met | User input is limited to 15 characters | **PASS** | **PASS** |
|   005    |  Username already taken | Let user know username it's taken | User Redirected to Sign-up page with a Flashed message | **PASS** | **PASS** | 

![Username taken](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/username-taken.jpg)

|   Test   | Purpose         | Desired Result | Actual Result | Chrome v 87.0.4280.88 | Firefox v 84.0 (64-bit) |
|:--------:|-----------------|----------------|---------------|:------:|:-------:|
|   006    | Username or password too short | Indicate requirements not met | Input box turns red and tooltip provides feedback | **PASS** | **PASS** |
|   007    | Incorrect Username  | Inform user of issue | User Redirected to Log-in page with a Flashed message | **PASS** | **PASS** |
|   008    | Incorrect Password  | Inform user of Issue | User Redirected to Log-in page with a Flashed message | **PASS** | **PASS** |

![Incorrect Log-in](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/incorrect-login.jpg)

|   Test   | Purpose         | Desired Result | Actual Result | Chrome v 87.0.4280.88 | Firefox v 84.0 (64-bit) |
|:--------:|-----------------|----------------|---------------|:------:|:-------:|
|   009    | Successful Sign-up  | User redirected into web-app with Success message displayed | User is taken to Profile page with Welcome message displayed | **PASS** | **PASS** |
|   010    | Successful Log-in  | User redirected into web-app with Success message displayed | User is taken to Recipes page with Welcome message displayed | **PASS** | **PASS** |  

![Sign-up Success](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/success-login.jpg)

____


#### **Recipe Search & View (READ)** <a name="recipes"></a>
This section documents the testing performed to validate the ability of the user to view the recipe collection, filter by country and perform a text search. Clicking the Floating Action Button on each recipe should also reveal the full recipe details.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Navigate to Recipe Page| Recipes ;ink on Navbar correctly redirects users to Recipes Page| Navbar link functions correctly and redirects users to the Recipes Page| **PASS** | **PASS**|
|  002   |  Latest First  | Display recipes in reverse chronological order | Recipes are sorted, newest to oldest | **PASS** | **PASS** |
|  003   |  Recipe Filter  | Returns results based on user selected country | Correctly filters recipes and only returns matching recipes | **PASS** | **PASS** |
|  004   |  Recipe Filter  | Filter options available after initial search | The Filter function can be used again and again based on different countries | **PASS** | **PASS** |  

![Country Filter](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/country-filter.jpg)  
![Filter Results](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/filtered-results.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  005   | Recipe Search   | Returns results based on user text input | Recipes displayed based on matching text | **PASS** | **PASS** |

![Recipe Search](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/search-results.jpg)
> **The recipe country filter and text search are not able to be used together in this first release of the app.**

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  006   | Recipe Display   | Correctly display the selected recipe in full | Full recipe displayed for respective recipe cards | **PASS** | **PASS** |
|  007   | Pagination | Limits display to 6 recipes | Six recipes displayed per page (where applicable) | **PASS** | **PASS** |
|  008   | Pagination | Next and Previous Page arrows assist navigation through pages | Next and Previous page arrows work as desired | **PASS** | **PASS** |
|  009   | Pagination | Page numbers link to respective recipe page | Pagination page links correctly redirect users to the appropriate page of results | **PASS** | **PASS** |
|  010   | Return to main Recipes Page   | No requirement to use the back button | Users can navigate away from the full recipe page using navbar or "Back to Recipes" button at the bottom of the page | **PASS** | **PASS** |
____
   
#### **Add Recipe (CREATE)** <a name="add-recipe"></a> 
Tests to check the users ability to upload a new recipe to the collection, and validate process robustness.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Navbar link   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  002   | Manage Recipe link   | Link provided on Manage Recipes page results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  003   | Country Select   | Displays the list of countries in alphabetic order | List is displayed in the correct order. Users can scroll, or type the first letter of the country to navigate the list | **PASS** | **PASS** |
|  004   | Recipe Name   | Textbox functions as desired | Users can input a name. Feedback is provided if the name is <5 characters | **PASS** | **PASS** |
|  005   | Regex pattern matching on Recipe Name | No special characters or continuous spaces| Field highlights red and message displays on hover [BAD MATCH](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/add-name-bad.jpg) / [GOOD MATCH](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/add-name-good.jpg) | **PASS** | **PASS** |
|  006   | Recipe Category Select  | Displays the list of recipe categories | List displays and users can select the category appropriate for their recipe | **PASS** | **PASS** |
|  007   | Vegetarian / Vegan Switches | Switches are "off" by default and will toggle on when selected. | Switches toggle as desired and change colour to teal when "on" | **PASS** | **PASS** |
|  008   | Recipe Servings  | Displays a list of numbers from 1 - 30 | Correctly displays the list and is selectable | **PASS** | **PASS** |
|  009   | Recipe Image   | Adding a valid image URL results in image displaying below input field| Image displays if a valid URL [Good URL](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/good-recipe-url.jpg) | **PASS** | **PASS** |
|  010   | URL Regex pattern matching | Image URL must start with https//: | Input field turns red and message displayed on hover [Bad URL](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/bad-recipe-url.jpg) | **PASS** | **PASS** |
|  011   | Prep & Cooking Time   | Tooltip displays format | Tooltip provides suggested format to use |  **PASS** | **PASS** |
|  012   | Prep & Cooking Time Regex pattern matching | Does the input field highlight when the input is incorrect| Input field changes to red & message displays on hover. [BAD MATCH](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/bad-time-match.jpg) | **PASS** | **PASS** | MATCH](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/bad-recipe-url.jpg) | **PASS** | **PASS** |
|  013   | Recipe Description   | Users are able to add a description, but the input cannot be whitespace or special characters. | Description renders correctly, and does not allow special characters | **PASS** | **PASS** |
|  014   | Recipe Ingredient Input   | Users are able to add ingredients on new lines | Users are able to add as many ingredients as necessary. Tooltip advises users to enter each ingredient on a new lines | **PASS** | **PASS** |
|  015   | Recipe Method Input   | Users are able to add each new preparation step on a new line | Method input works as desired | **PASS** | **PASS** |
|  016   | Data Written to MongoDB   | Confirm new recipe data is written to MongoDB | New recipes appear as a new Recipes document within Mongo DB. All fields are populated if completed | **PASS** | **PASS** |
|  017   | Profanity Check  | Replace profanities in user input with ***  | Profanities are correctly replaced with *** | **PASS** | **PASS** |
|  018   | Full Recipe Page | The information renders correctly on the Full recipe Page | The selected fields render as intended on the Full Recipe page | **PASS** | **PASS** |

_____

#### **Manage Recipes** <a name="manage"></a>
This sections defines the testing performed on the Manage Recipes page, from which users can edit and delete their recipes. If the user has Admin rights they are able to view and interact with all recipes.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Navigation to Manage Recipes | Navbar should redirect users to the Manage Recipes page | The Navbar link functions correctly and redirects users to the Manage Recipes Page. | **PASS** | **PASS** |
|  002   | Profile Page Link | If user has uploaded recipes a link redirects users to the Manage Recipes Page | Link correctly redirects users to the Manage Recipes page IF they have previously uploaded at least one recipe | **PASS** | **PASS** |
|  003   | Recipe Quantity |Correct number of recipes displayed by user profile | The web app displays 6 recipes per page where appropriate | **PASS** | **PASS** |
|  004   | Pagination | Pagination limits to 6 recipes/page | This is probably more appropriate to the Admin view as I don't anticipate many users having more than 6 recipes initially. Functions correctly | **PASS** | **PASS** |
|  005   | Pagination | Previous and Next Pagination links work as desired | These buttons function as desired | **PASS** | **PASS** |
|  006   | Pagination | Page number links redirect users to the appropriate page | The page numbers correctly link to the appropriate page and redirect the user as desired | **PASS** | **PASS** |
|  007   | Recipe Cards | Recipe cards display correct information and are properly formatted | The recipe cards render the information as desired and are consistent with the main Recipe page for consistency | **PASS** | **PASS** |
|  008   | Recipe Edit Button | Recipe Edit Button redirects user to Edit Recipe Page | The Recipe edit button reveals when the FAB is hovered. It redirects users to the Edit Recipe page | **PASS** | **PASS** |
|  009   | Recipe Delete Button | Recipe Delete Button initiates the Deletion Process (see below for more detail) | The recipe Delete button reveals with the Edit Button when the FAB is hovered. It correctly initiates the delete process but does not directly delete the recipe | **PASS** | **PASS** |
|  010   | Add Recipe Link | Add Recipe link takes users to the Add Recipe Page | The link does take the user to the Add Recipe page | **PASS** | **PASS** |

_____

#### **Edit Recipe (UPDATE)** <a name="edit-recipe"></a>
The Edit Recipe page enables users to retrieve a previously uploaded recipe from the database and edit any of the data previously supplied. This section validates the functionality of this page.  

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Edit Recipe Form | Edit Recipe form displays correctly | The form displays and is almost identical to the Add Recipe form | **PASS** | **PASS** |
|  002   | Existing Data renders| Display existing recipe data from the database on the form | All of the existing data is rendered from the database into the form fields | **PASS** | **PASS** |
|  003   | Country of Origin | Country of Origin is populated and selectable | Country of origin dropdown functions and is selectable | **PASS** | **PASS** |
|  004   | Recipe Categories | Recipe Categories are populated and selectable | Category dropdown functions and is selectable | **PASS** | **PASS** |
|  005   | Recipe title is editable | User can change the recipe title | The user can edit and delete the recipe title  | **PASS** | **PASS** |
|  006   | Servings| Servings is populated and selectable  | Servings dropdown functions and is selectable | **PASS** | **PASS** |
|  007   | Vegan & Vegetarian switches | Function and become highlighted on Recipe card if selected | Switches function render correctly if changed | **PASS** | **PASS** |
|  008   | Recipe Image | Current recipe image displays from the start | The recipe image is visible when the page renders | **PASS** | **PASS** |
|  009   | New Recipe Image | Renders if a valid URL is supplied | The new image displays below the old image. New image saves to DB | **PASS** | **PASS** |
|  010   | Recipe Description | Description is editable and saves correctly | Users are able to edit part of, or completely delete the description and start again | **PASS** | **PASS** |
|  011   | Recipe Ingredients | Ingredients are editable and save correctly | Recipe ingredient lines are editable as required and changes save to DB | **PASS** | **PASS** |
|  012   | Recipe Method | Preparation steps are editable and save correctly | Recipe prep' steps are editable and changes save to DB | **PASS** | **PASS** |
|  013   | Confirmation of Upload | Provide confirmation of upload and redirect the user away from the Edit Recipe form | User is redirected to the manage Recipes page and a confirmation message  is flashed to the screen | **PASS** | **PASS** |

___

#### **User Profile (READ)** <a name="user-profile"></a>

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Navbar Link     | Profile link on navbar takes users to their profile page | The link in the navbar functions as desired the user profile page is rendered correctly with information stored in the DB | **PASS** | **PASS** |
|  002   | Render Information correctly | Display the information for the user stored in the DB | Basic information displayed for users who haven't edit their profile.  | **PASS** | **PASS** |

![Basic Profile](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/basic-profile.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  003   | Display email | Correctly displays email address if user chooses to subscribe | Email address is rendered below Town / City  | **PASS** | **PASS** |
|  004   | Display city | City name displays correctly if user chooses to supply it | City displays below profile image | **PASS** | **PASS** |
|  005   | Display image | Display default image until updated image is supplied. Display in Centre of form | Image displays correctly in the centre of the Profile form | **PASS** | **PASS** |

![Full Profile](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/full-profile.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  006   | Remove Email | Remove email if user unsubscribes | The email is no longer rendered on the Profile page and is cleared from database | **PASS** | **PASS** |

![Unsubscribed Profile](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/unsubscribed.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  007   | Edit Profile Button| Redirect the user to the Edit profile page | Users are correctly redirected to the Edit Profile page| **PASS** | **PASS** |
|  008   | Delete Profile Button | Opens up a Confirmation Modal - no deletion yet | Modal appears, Delete function not yet triggered | **PASS** | **PASS** |

![Profile Delete Modal](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/delete-profile.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  009   | Escape Route    | "Go Back" button cancels the delete process and returns the user to the Profile page | The button functions as desired, redirecting the user away from the delete process and back to safety on the Profile page | **PASS** | **PASS** |
|  010   | Confirm Deletion | Delete function executes and deletes the profile from the database. User is provided with confirmation | If the user choses to delete their profile their data is deleted and they are redirected to the home page | **PASS** | **PASS** |

![Profile Deleted](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/prof-del-good.jpg)
___

#### **Edit Profile** <a name="edit-profile"></a>

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Edit Profile Button | The Edit profile button on the Profile page directs the user to the edit profile page | The button does redirect the users to the appropriate profile page | **PASS** | **PASS** |
|  002   | Edit Profile image | Profile image updates correctly when new URL supplied |  | **PASS** | **PASS** |
|  003   | New Profile Image | New profile image displays if valid URL supplied | The new image displays below the old if a valid URL is supplied | **PASS** | **PASS** |
|  004   | City update | Users city is uploaded to database when supplied and new data rendered into profile| Information saves and renders correctly | **PASS** | **PASS** |
|  005   | Subscribed switch functionality | Switch status changes when selecting on and opens email entry input field | Switch functions correctly and email input field appears | **PASS** | **PASS** |

![Subscribed Off](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/subscribed-off.jpg)
![Subscribed On](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/subscribed-on.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  006   | Write to DB | The updated profile info saves to the DB | New or edited profile information correctly saves to the DB | **PASS** | **PASS** |  

___

#### **Delete Recipe (DELETE)** <a name="delete-recipe"></a>  
Testing to confirm correct functionality of the Delete function. Aspects of this testing are critical as I don't want to delete the incorrect recipes.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
| 001    | Navigate to Delete option | Delete button initiates recipe deletion | Clicking Delete correctly initiates the deletion process | **PASS** | **PASS** |

![Start Deletion](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/del-step1.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
| 002    | Prevent unauthorised Deletion | Delete function should only be available to ADMIN and the uploading user | The only recipes shown for users are those they have uploaded themselves | **PASS** | **PASS** |
| 003    | Check with user before deleting recipe | Deletion modal should appear, to confirm deletion | Modal appears with confirmation message and Recipe name displayed | **PASS** | **PASS** |

![Start Deletion](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/del-step2.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
| 004    | Provide escape route | Button provides way back to Manage Recipes | A "Go Back" button has been provided as an alternative to the Confirm Deletion option. redirects user to Manage recipes | **PASS** | **PASS** |
| 005    | Delete Correct Recipe | Ensure the correct recipe is deleted |Each recipe is linked by it's unique id, which is used when selecting or deleting recipes. Confirmation message includes the recipe name. **Checked in MongoDB** | **PASS** | **PASS** |
| 006    | Provide Confirmation of Deletion | Flash message should appear when user is redirected to Manage Recipes page | User is redirected and message is displayed | **PASS** | **PASS** |

![Start Deletion](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/del-confirmation.jpg)
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
| 007 | Only delete the selected recipe document when performing deletions | Confirm only recipe data is removed from the database on deletion. Ensure no other collections are affected by the Delete function. | Only selected document is deleted. No downstream effect; no other collections or documents affected| **PASS** | **PASS** |

To confirm the integrity of the deletion process I chose to deleted a recipe created to validate the profanity filter
The recipe exists in the MongoDB Atlas database prior to deletion.

![Recipe in Database](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/recipe-collection.jpg)

1. Delete the "**** Soup" from the Manage Recipes page
   - This recipe used document fields from other collections
     - User = Adminuser
     - Country = Canada
     - Recipe Category = Appetisers  

 If the deletion process works as desired each of these fields should remain post deletion.  
 
2. Delete confirmation modal appears to check Deletion - **PASS**

![Delete Check](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/confirm-delete.jpg)

3. Once confirmed the user is redirected to the Manage Recipes page - **PASS**
4. A Flash message appears at the top of the Manage Recipes page confirming deletion - **PASS**
5. The recipe no longer appears on the Manage Recipes page - **PASS**

![](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/deleted.jpg)

6. The Recipe has been deleted from the database - **PASS**

![](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/recipe-removed.jpg)

7. The integrity of the other collections has not been affected. - **PASS**

##### User Collection
![User Collection](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-collection.jpg)

##### Country Collection
![Country Collection](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/country-coll.jpg)

#####Recipe Collection
![Recipe Category Collection](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/recipe-category.jpg)

______
### **Appearance Testing** <a name="appearance"></a>
This web app was primarily developed on a Google Chrome browser, on a Windows Laptop. The app has been regularly tested on Firefox to check functionality. This section tests for any changes in appearance between the different browsers.  

|     Page     |  Desired Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------------:|----------------|-----------------------|-------------------------|
| Landing Page | Minimal visible difference | No visible difference | No visible difference |
| Sign-up Page | Minimal visible difference | No visible difference | No visible difference |
| Log-in Page  | Minimal visible difference | No visible difference | No visible difference |
| Recipes Page | Minimal visible difference | No visible difference | No visible difference |
| Add Recipe | Minimal visible difference | Dropdown list items slightly less sharp than Firefox | Some of the bold text does not appear as bold as in Chrome. Placeholder colour is lighter than Chrome |
| Manage Recipes | Minimal visible difference | No visible difference | No visible difference |
| Edit Recipe | Minimal visible difference | Dropdown list items slightly less sharp than Firefox | Minimal visible differences |
| Profile Page | Minimal visible difference | Profile image is less clear and less sharp | Profile image appears to have better contrast and sharpness |
| Edit Profile | Minimal visible difference | No visible difference | No visible difference |
| Dashboard Page | Minimal visible difference | No visible difference | No visible difference  |
______

### **Code Quality and Validation** <a name="code-validation"></a> 
Online tools have been used to validate the HTML, CSS, Python and JavaScript files to ensure they are free from errors, and comply with the latest standards. The results of these tests are documented below. 

#### **HTML Validation**
This section contains the results and any warnings or errors reported during HTML validation using the WC3 validator. 

|      Page       | Error / Warning | Comment  |
|-----------------|:---------------:|:--------:|
|  Landing Page   |       None      | **PASS** |
|  Matches        |       None      | **PASS** |
|  Match Detail   |       None      | **PASS** |
|  Edit Match     |       None      | **PASS** |
|  Add Match      |       None      | **PASS** |
|  Add Travel     |       None      | **PASS** |
|  Messages       |       None      | **PASS** |
|  Add Message    |       None      | **PASS** |
|  Clubs          |       None      | **PASS** |
|  Edit Club      |       None      | **PASS** |
|  Add Club       |       Nonne     | **PASS** |
|  Teams          |       None      | **PASS** |
|  Edit Team      |       None      | **PASS** |
|  Add Team       |       None      | **PASS** | 
| Add Competition |       None      | **PASS** |
|  Kit Bag        |       None      | **PASS** |
|  Checkout       |       None      | **PASS** |
| Checkout Success|       None      | **PASS** |
| Profile         |       None      | **PASS** |
| Sign-up         |       None      | **PASS** |
| Sign-in         |       None      | **PASS** |
| Log-out         |       None      | **PASS** |

#### **CSS Validation**
The following section contains the results and any warnings or errors reported during CSS validation using the WC3 validator.

|    CSS File     | Error / Warning |  Comment |
|:---------------:|:---------------:|----------|
|     base.css    |       None      | **PASS** |
|     home.css    |       None      | **PASS** |
|   matches.css   |       None      | **PASS** |
|  checkout.css   |       None      | **PASS** |
|  profile.css    |       None      | **PASS** |


|Test|Process|Result| Comment |
|----|-------|:----:|---------|
|CSS Beautifier| [CSS Auto Prefixer](https://autoprefixer.github.io/) | **CHECKED** | Output Used |
|Python Validation| Copy app.py code into [PEP8 Online](http://pep8online.com/)| **CHECKED** | No Errors Detected|
|Python Beautifier| Copy app.py code into Python Beautifier](https://www.tutorialspoint.com/online_python_formatter.htm)| **CHECKED** | |
|Javascript Validation| Copy script.js code into JSHint | **CHECKED** ||
|Javascript Validation| Copy script.js code into JSLint | **CHECKED** ||
|Website Spelling | URL input [Typosaurus](https://typosaur.us/) | **CHECKED** | Difficulty on pages requiring authentication so MS Word used or the Grammarly plugin when adding or editing a recipe |
| README file Spelling | Text copied into word | **CHECKED** |  |

____

### **Usability Testing** <a name="usability"></a>
I requested fellow CI students and former colleagues to test the website to gather their feedback on the User Experience and Interactivity. What follows are the comments I received in return:
|   User   | Feedback |
|:---------:|----------|
|  K. Moore | ![KM Feedback](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/km-feedback-1.jpg) |
|  K. Moore | ![KM Feedback](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/km-feedback-2.jpg) |
| K. Tanaka | ![Toto Feedback](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/toto-feedback.jpg) |
| E.Carroll | Verbal feedback - Nice concept, like the idea of sharing the recipes.
| E.Carroll | Verbal feedback - I think the map is a great feature, would be great to click on the map and see recipes for that country |
| E.Carroll | Verbal feedback - It was easy to upload a recipe. It would be better if you could upload you own recipe photo. I think most people are used to this |
| A.Sheward | First indicated the potential issue with the Materialize Select elements on iOS devices |
  
> **The vulnerability pointed out by Toto has been addressed and users are no longer able to delete a recipe by manipulating the web app URL.**
____

### **Responsiveness Testing** <a name="responsiveness"></a>
I have conducted continuous responsiveness testing, right up to the final submission, to ensure the website functions on different devices and in both portrait and landscape orientation, using Google Devtools and Responsinator.com.
This project has been deployed using Heroku and the website has been continuously reviewed on several real devices:
  - Samsung Galaxy S9
  - Samsung Tab A
  - HP Laptop with attached monitor

This helped me make changes and apply appropriate media queries to maintain responsiveness.

The table below contains lists the results of the Responsiveness testing and links to images compiled from Google Devtools. The Responsinator.com app was also used to test the web app.
 

|  Test  | Page | Responsiveness Image Link | Result |
|:------:|------|--------------------|--------|
|   001  |Landing Page|          |            |
|   002  | Matches    |          |            |
|   003  | Match Detail |        |            |
|   004  | Edit Match |          |            |
|   005  | Add Match  |          |            |
|   006  | Add Travel |          |            |
|   007  | Messages   |          |            |
|   008  | Add Message |         |            |
|   009  | Clubs      |          |            |
|   010  | Edit Club  |          |            |
|   011  | Add Club   |          |            |
|   012  | Teams      |          |            |
|   013  | Edit Team  |          |            |
|   014  | Add Team   |          |            | 
|   015  | Add Competition |     |            |
|   016  | Kit Bag    |          |            |
|   017  | Checkout   |          |            |
|   018  | Checkout Success |    |            |
|   019  | Profile    |          |            |

____

### **Performance Testing** <a name="performance"></a>
The website has been performance testing using the following tools:
 - Google Lighthouse (Desktop)
> Testing was performed in incognito mode as Google extensions can affect the results of the lighthouse testing.

![Landing Page Lighthouse](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/landing-lighthouse.jpg)

|    Page    | Performance | Accessibility | Best Practices | SEO  |
|:----------:|:-----------:|:-------------:|:--------------:|:----:|
|Landing Page|     97%     |       97%     |     100%       |  90% |
| Matches    |     95%     |       96%     |     100%       | 100% |
| Match Detail |   93%     |       95%     |      93%       |  90% |
| Edit Match |     96%     |       91%     |     100%       |  90% |
| Add Match  |     98%     |       93%     |     100%       |  90% |
| Add Travel |     98%     |       97%     |     100%       |  90% |
| Messages   |     95%     |       97%     |     100%       |  90% |
| Add Message |    96%     |       92%     |     100%       |  90% |
| Clubs      |     94%     |       97%     |     100%       |  80% |
| Edit Club  |     98%     |       85%     |     100%       |  80% |
| Add Club   |     98%     |       93%     |     100%       |  90% |
| Teams      |     98%     |       92%     |     100%       |  90% |
| Edit Team  |     98%     |       99%     |     100%       |  90% |
| Add Team   |     94%     |       97%     |      93%       |  90% |
| Add Competition |  98%   |       97%     |     100%       |  90% |
| Kit Bag    |     97%     |       97%     |     100%       |  90% |
| Checkout   |     87%     |       97%     |     100%       |  90% |
| Checkout Success |  96%  |       97%     |     100%       |  90% |
| Profile    |     97%     |       97%     |     100%       |  90% |

 - Google Lighthouse (Mobile)  

|    Page    | Performance | Accessibility | Best Practices | SEO  |
|:----------:|:-----------:|:-------------:|:--------------:|:----:|
|Landing Page|     85%     |       98%     |     100%       |  92% |
| Matches    |     79%     |       97%     |     100%       |  83% |
| Match Detail |   82%     |       97%     |     100%       |  92% |
| Edit Match |     78%     |       92%     |     100%       |  92% |
| Add Match  |     81%     |       90%     |     100%       |  92% |
| Add Travel |     82%     |       98%     |     100%       |  92% |
| Messages   |     82%     |       98%     |     100%       |  92% |
| Add Message |    82%     |       91%     |     100%       |  92% |
| Clubs      |     87%     |       98%     |     100%       |  83% |
| Edit Club  |     69%     |       82%     |      93%       |  83% |
| Add Club   |     78%     |       90%     |     100%       |  92% |
| Teams      |     83%     |       90%     |      93%       |  92% |
| Edit Team  |     78%     |       99%     |     100%       |  92% |
| Add Team   |     82%     |       98%     |     100%       |  92% |
| Add Competition |  82%   |       98%     |     100%       |  92% |
| Kit Bag    |     75%     |       95%     |     100%       |  92% |
| Checkout   |     69%     |       97%     |     100%       |  92% |
| Checkout Success |  79%  |       97%     |     100%       |  92% |
| Profile    |     77%     |       96%     |     100%       |  92% |

____

### **Security Testing** <a name="security"></a>
The following tests have been performed on the security features implemented on this site, and are documented in the table below:
#### **URL Manipulation**
These tests ensure that there are appropriate levels of access to the various pages in the web app, and that annonymous users cannot access content requiring login, or that registered users are only able to access content equal to their access rights:

| Page | URL | Registered user - Desired Result | Status | Anonymous User - Desired Result | Status |
|------|-----|----------------------------------|--------|---------------------------------|--------|
| Add Competition | `matches/comp/` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Add Club | `matches/club/` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Add Team | `matches/team/` | Error message displayed  | **PASS** | Redirected to login | **PASS** |
| Add Match | `matches/add/` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Add Travel | `matches/travel/match.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Edit Club | `matches/edit_club/club.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Edit Team | `matches/edit_team/team.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Edit Match | `matches/edit/game.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Delete Club | `matches/delete_club/club.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Delete Team | `matches/delete_team/team.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Delete Match | `matches/delete/game.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| Messages | `matches/chat/game.id` |  |  | Redirected to login | **PASS** |
| Add Message | `matches/add_chat/game.id` |  |  | Redirected to login | **PASS** |
| Kit bag | `bag/` |  |  | Redirected to login | **PASS** |
| Checkout | `checkout/` |  |  | Redirected to login | **PASS** |
| Profile | `profile/` | N/A | N/A | Redirected to login | **PASS** |
  

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Username Reuse  | No username duplication allowed | Sign-up does not allow duplicate usernames. A warning message is flashed onscreen and the user redirected to Sign-in again | **PASS** | **PASS** |
|  002   | Password Security  | Passwords are hashed and salted  | Each user passwords is converted into a unique string of characters | **PASS** | **PASS** |
|  003   | Only superusers can edit a match | Users can only view their own uploads when selecting the Manage Recipes page | The Manage Recipes view is limited to those recipes the user has uploaded |  **PASS** | **PASS** |
|  004   | Prevent unauthorised recipe edits | Prevent users from editing a Full_Recipe URL such as ("https://ci-ms3-w3recipes.herokuapp.com/full_recipe/604105c97084e9c04df5e2e7") and changing full recipe to  edit_recipe. | Users are redirected back to the Manage Recipes page. Warning message flashed to screen. | **PASS** | **PASS** |
|  005   | Prevent unauthorised recipe deletion | Prevent users from editing a Full_Recipe URL such as ("https://ci-ms3-w3recipes.herokuapp.com/full_recipe/604105c97084e9c04df5e2e7") and changing full recipe to delete_recipe.| Users are redirected back to the Manage Recipes page. Warning message flashed to screen. | **PASS** | **PASS** |
|  006   | Prevent web app URL copy and paste | Error page if a user copies a logged-in page url into a new browser, without logging in | Results in a 500 Internal server error as there is no session cookie with the required username| **PASS** | **PASS** |




______

## **Bugs, Issues and Fixes** <a name="bugs"></a>
The following table explains the bugs and issues encountered while building this website.
|  Issue #   |  Bug or Issue  |  Description  |  Solution  |
|:----------:|:--------------:|---------------|------------|
|  |  |  |  | 

**[Back to Github Repo](https//:github.com/GazzaJ/CI-MS3-W3Recipes/)**