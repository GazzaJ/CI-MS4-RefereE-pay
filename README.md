![RefereE-Pay](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/readme-title.jpg "RefereE-Pay")

# [**RefereE-Pay**](https://ci-ms4-referee-pay.herokuapp.com/matches/clubs)

## **Project Justification**
The idea for this web app came about as a direct result of the ongoing COVID-19 pandemic. This crisis affected many aspects of our lives, not least of which were the consequences for grass-roots football. When the initial lockdowns eased and sports were once agaion allowed; the environment in which we participated was dramatically different, with a higher emphasis placed on reducing person to person contact.
In Grassroots football this meants no exchanging of team sheets and player registration cards, however, we were still required to pay our referees and assistant referees fees in cash, but to hand over the cash in an envelope or bag.
With many clubs and businesses using this crisis as an opportunity to pivot towards electroniuc payments I was surprised that the English FA hadn't addressed this need, and Team managers and coaches continue to have to pay match officials in cash.

As a grassroots team coach/manager myself, I found this almost insignificant change to be a headache. People just weren't using cash as much, and always ensuring you had an appropriate receptacle to place the money in was an added complication.
With everything else happening on a match day, (set up, warm up, team talk, game, substitutions, post game chat, packing away kit) it is easy to forget about the ref's payment, particularly if they want to receive the payment after the game.
Since the use of cahless transactions has certainly accelerated in many areas of society and I thought it would be great to have a cashless means of paying the match officials fees, and thus RefereE-Pay formed as an idea for a project.

In addition to ensuring the match officials get paid, home team managers are also required to contact the referee, a couple of days prior to the game and let them know any changes to the fixture or any issues with the pitch. This is currently done via text message.
Thus while forming the idea for RefereE-Pay I figured it would also be useful to have a single match day app which is capable of handling both communication with and payments for the match officials.

The English FA already provides some excellent grassroots technology like [FA FullTime](https://fulltime.thefa.com/en) (Fixture Listings and League tables), The Whole Game system (Club, Team and player Management) and Matchday (for game day team management and player subs payments), but doesn't (to my knowledge) currently have a solution for communicating with and paying the Referees electronically.

RefereE-Pay is a concept for how such an app might function.
Ideally this app would integrate with existing FA software, and would simply exist as a payment and communication app. However for the purposes of this project, I have also included a basic manual fixture creation feature to complete the CRUD functionality, although in reality this would likely be satisfied by existing technology used by county FA's.

The target audience for this app would be registered football coaches/managers. There is no requirements for annonymous/non-registered users to make payments or view content.

My aim is to achieved the above with a visually appealing, interactive yet intuitive UX, which provides simple consistent navigation and interaction irrespective of the device. Ultimately, I would like this site to be fun, and enabling users to:
 - Find Fixtures relevant to a particular team or age group
 - Select a fixture and view the details such as:
   - Teams
   - Venue
   - KO Time and Date
   - Match Officials
   - Match Officials Fees
 - Communicate information and share pictures with the ref relevant to the fixture
 - Be able to select a fixture and pay for the officials match fees
 - enable useres to view their payment history, so thay can claim back monies owed to them
 - Provide Admin with a means to create Edit and Delete fixtures as required.

[The live website can be viewed here!](https://ci-ms4-referee-pay.herokuapp.com/matches/clubs)

![Am I responsive images]( "Am I Responsive")

## Table of contents
An automatically generated Table of Contents can be accessed by clicking the README.md menu icon at the start of the README section.  
![TOC](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/toc-alt.png)  

1. [User Experience](#user-experience)
   - [User Stories](#stories)
   - [The 5 Planes](#planes)
   - [Wireframes](#wireframes)
2. [Database Schema](#dbschema)
3. [Features](#features)
4. [Technologies Used](#technologies)
5. [Testing](#testing)
6. [Database Creation](#database)
7. [Deployment](#deployment)
8. [Resources](#resources)
9. [Credits](#credits)
    - [Media](#media)
    - [Code Snippets](#code)
    - [Acknowledgements](#acknowledgements)
10. [Technical Support](#technical)
______

## **User Experience (UX)** <a name="user-experience"></a>
I have attempted to produce a simple clean and intuitive site which is easy to navigate and simple to use. Despite being spread over many pages, each page has a single purpose related to an element of C.R.U.D functionality. Navigation is achieved with a typical navbar with mobile responsive behaviour. The imagery used is also key to creating a positive user experience.

### **User Stories** <a name="stories"></a>
The following user stories were developed during the planning stages for this site.
#### **Registration and User Accounts**
| User Story |  As a  | I need to | In order to |
|:----------:|-------|-----------|-------------|
|  1  | Site User  | Easily register for an account | Have a personal account and be able to view my profile |
|  2  | Site User  | Easily login or logout | Access my personal account information |
|  3  | Site User  | Easily recover my password in case I forget it | Recover access to my account |
|  4  | Site User  | Receive an email confirmation after registering | Verify that my account registration was successful |
|  5  | Site User  | Have a personalised user profile | View my personal payment history and payment confirmations, and save my payment information |

#### **Searching and Filtering**
| User Story |  As a  | I need to | In order to |
|:----------:|-------|-----------|-------------|
|  6  |  Team Manager  | Easily identify all of my teams matches | understand who I am playing and when |
|  7  |  Team Manager  | Sort all fixtures | Easily identify my teams fixtures |
|  8  |  Team Manager  | Sort a specific category of matches |  |
|  9  |  Team Manager  | Sort multiple categories of products simultaneously |  |
| 10  |  Team Manager  | Search for fixtures by team name | Find a specific fixture I'd like to pay the match official fees for |

#### **Communication**
| User Story |  As a  | I need to | In order to |
|:----------:|-------|-----------|-------------|
| 11  |  Team Manager  | Communicate with the ref | Confirm status and alert on any pitch team issues |
| 12  |  Team Manager  | Post Pictures | Illustrate pitch conditions ahead of any game |
| 13  |  Referee  | Communicate with the teams | Reply to any concerns or issues raised |

#### **Selection and Checkout**

| User Story |  As a  | I need to | In order to |
|:----------:|-------|-----------|-------------|
| 14  |  Team Manager  | Easily select the fixture | Ensure ability to exit fixture if incorrect one selected |
| 15  |  Team Manager  | A simple cashless method to pay the referee | Pay the assigned referee |
| 16  |  Team Manager  | View payments in my cart | Identify the total cost of payments and what I'm paying for |
| 17  |  Team Manager  | Easily enter my payment infoirmation | Check out quickly without complications |
| 18  |  Team Manager  | Feel my personal and payment information is secure and safe | Confidently provide the needed information to make a purchase |
| 19  |  Team Manager  | View on order confirmation after checkout | Verify that I haven't made any mistakes |
| 20  |  Team Manager  | Receive an email confirmation after checkout | Keep the confirmation of what paid for my records and claiming from Club |

#### **Admin and Management**
| User Story |  As a  | I need to | In order to |
|:----------:|-------|-----------|-------------|
| 21  |  Site Admin  | Create a new Fixture | Add new team fixtures  |
| 22  |  Site Admin  | Edit / Update an existing Fixture | Change fixture dates, venues, images, times and Referee |
| 23  |  Site Admin  | Delete a Fixture | Remove a fixture if necessary |

___

### **The 5 Planes of UX** <a name="planes"></a>
I refer to the five planes of UX to provide a framework for discussing the finer points of this app's design and development.

#### **Strategy**  
The purpose of RefereE-Pay web app is to provide grassroots football coaches and managers with an electronic means of communicating with and paying match officials fees. The aim is to try and provide a visual dashboard of each fixture, containing all of the information needed by either the home or away coach. or the ref, in a single location.
 - As the site owner and grassroots team coach I get to create a potential solution for a 
 - Users get access to all of the fixtures in the data base; are able to filter, and access individual fixtures which they can subsequently pay the match fees for.

#### **Scope**  
The key features required for this app to function as designed are centred around CRUD interactions with a MongoDB Atlas cloud database management system.:
 - **Create** fixtures for a group of teams in an age group. 
 - **Read**, or view all of the fixtures stored in the database.
    - Filter those fixtures by age group, or Team name
    - Search functionality enables the user to search the database for a particular team and display their games
 - **Update** Enable Admin users to edit Clubs, Teams and Fixtures as required, and also allow the Match Officials to input any travelk expenses they have into the fixture information
 - **Delete** function for Site Admins, who can remove Clubs, Teams and fixtures as required

In order to prevent unwanted editing or deletions of records, I have used the @login_required decorator in functions and also built in logic which requires the user to be a superuser in oprder perform deletions. Thus, to access the full functionality users are required to Sign-up to the App as a superuser.

##### Functional Requirements
App functionality is provided through a typical intuitive, mobile responsive navbar. The navbar menu options increases once a user registers or logs into the website, increasing what they can view and achieve.
Additional interactive anchor links are provided throughout to provide users with multiple ways of navigating around the app.

##### Content Requirements
Much of the content in this app revolves around the Matches Model, which is a list of Venues, Clubs, Teams, Match Officials and Games I have uploaded through fixture files. Additional data has subsequently been added using the app's CRUD functionality
Outside of this I have maintained football themed images and icons to maintain a consistent look.

The typography selected for this site was not as important, but nonetheless needed to be clear and functional. 
I had considered using a sporty font but didn't want to detratct from the purpose of the site
I deliberately stuck with a clean and simple, structured layout to make it easy to view and edit the content.

It was obviously important that the imagery used in this app was related to football, and more importantly, amateur football, which is the intended audience for this app.

Design elements and imagery are able to be re-used through through the wonders of Django template inheritance.
Each match has been deliberately structured to group critical pieces of information into distinct sections.
___

#### **Structure**  
The structure of RefereE-Pay is user dependent with user roles dictating what each group can achieve:
  - **Anonymous Users** can view the fixture list, Clubs and Teams only. They do not have access to the match details.
  - **Registered Users** can view the match details, but cannot complete any transactions
  - **Registered Coaches** are able to view the Fixtures, Clubs and Teams as well as the individual Match Details. They have the ability to add their teams HOME games to the kit bag and to complete payment. Home team coaches are also able to add messages to the fixture to communicate with the Match Official
  - **Match Officials** - have the same viewing capabilities as Coaches but obviously cannot pay the required match fees. They can add their travel expenses and send in app messages to the Home team Coach
  - **SuperUsers** - have full and unrestricted access to all functionality

constructed from **XX** distinct pages which are accessed through the main and mobile navbars. Prior to log-in there are only **XX** options: 

The workflow for RefereE-Pay is quite complex, but I have attempted to capture it below:
![Workflow](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/workflow.png "Website workflow")

##### **Interaction Design**
Interaction with each page is achieved through the main navbar, or through the use of stratcgically placed anchor links where appropriate.
Aside from this each page is self contained:
 - **Matches**
 Initially displays a paginated list of ALL matches. This list can be filtered based on user selections, to focus on a specific age group, and team of choice. The search box also enables the user to narrow down to a particular team 
 - **Match Detail**
 Selecting any of the displayed matches enables the user to drill down into the match detail and discover:
    - Home and Away Teams
    - Home and Away team Coaches
    - The venue and Kick Off time
    - Interactive dropdown showing the Venue Map (where provided)
    - Match Officials
    - Interactive dropdown of Match officials Fees
    - Message the 
    
   From this page, Coaches can add a particular match to their kit bag for checkout at their convenience. To avoid confusion, any match they have already paid for is marked with a "PAID" label and the the "Add to Bag" button is removed. 
 - **Kit Bag**
 This section of the app stores (for the duration of the session) any of the matches a user has selected for payment, and provides the user with a useful summary of the:
   - Match Fees
   - Match Fines
   - Match Total
   - Grand Total 
  
- **Checkout**
This page enables users to pay the match officials fees for any games they have in their kit bag.  

 - **User Profile**

 - **Data Input**
The primary User inputs are achieved using a series of forms through which, users are able to add and change their data (Recipes or User Profile). 
> A key consideration in the early planning stages was the method for inputting the recipe ingredients and preparation steps. I had initially thought about getting the user to input the number of ingredients and then looping through this number to enter each ingredient, one at a time. However, this would be problematic, if the user inputs an incorrect number. In this case they might have to restart the process, which would be undesirable. **Thus, the goal; has been to make it as easy as possible for the user to input this data.**


##### **Information Design**
Information is provided to users on multiple pages; Matches, Match Detail, Profile and Dashboard.
Despite rendering slightly different information the structure of the Recipe and Manage Recipe Pages are deliberately similar.

___

#### **Skeleton** 
The RefereE-Pay website initially comprises three main pages:
 - Landing Page
 - Registration Page for first time visitors to gain access to the content
 - Log-in Page for returning visitors

Assuming the user choses to register they are provided access to the remaining pages
 - Recipe's page displays 6 recipe cards per page
   - Filter and search options provided to reduce the number of recipes displayed
 - Individual Recipe pages provide the full recipe detail
 - An "Add Recipe" page enables users to upload their own recipe information
 - A page for the users to manage (Update or Delete) their recipes
   - Echoes the functionality provided by the Recipes and Add Recipe pages
 - A Profile page, leads onto an Edit Profile page where users can add a profile picture and subscribe by providing their email address.
 - A dashboard to track where recipes are uploaded for

Navigation between these pages is provided by a standard intuitive navbar, additional anchor links are provided on strategic pages to assist navigation. 

##### **Interface Design**
The intention was to provide a relatively simple app which maintains a clean and consistent interface design, re-using elements and page styles wherever possible to benefit from the users learned behaviour. Button colours provide visual cues to their role.
 - The Recipes page and Manage Recipes page are virtually identical aside from the search and filter elements being removed for managing recipes.  

![Interface Design](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/interface-1.jpg) 

 - Recipe cards have a consistent layout between the Recipes and Manage recipes pages. Each has a Floating Action Button which when clicked takes the user to the next level.

![Interface Design](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/interface-2.jpg)

 - The Add Recipes and Edit recipes pages are also identical in their appearance and structure.

![Interface Design](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/interface-3.jpg)

Flashed messages are displayed at the top of the screen below the navbar

Buttons colours are chosen to reflect their purpose, and anchor links have some interactive response when hovered.

##### **Interaction Design**
User interactions on the W3Recipes app can be subdivided into three categories:
 - **Navigation**  
 I have reverted to a conventional, mobile responsive navbar for this project, and this is one of the key elements which anchors each distinct page together.  
  ![Navbar](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/navbar.jpg)  

Navigating through the Recipes is achieved through familiar pagination controls.  
![Pagination](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/pagination.jpg)

I have provided links on several pages to also assist user navigation; these are quick links to :
 - Sign-in
 - Add a Recipe
 - Manage Recipes

These anchor links provide user feedback by either changing or reversing colours when hovered.
![Strategic anchor links](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/anchors.jpg)

 - **Manipulation**  
 Button colours have been chosen to match the site colours while also providing visual cues to their purpose:
   - Green ![Green Button](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/green-button.jpg)  
 Highlights functions to proceed with changes such as submitting a recipe or confirming changes  

   - Orange ![Orange and Red Buttons](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/orange-button.png)  
 Used as a warning, or to indicate an action which will eventually result in data being changed.

   - Red ![Red Button](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/red-button.jpg)  
 Highlights a Stop or Cancel function for changes, but more importantly highlight actions which could result in data being permanently removed or changed.

##### **Navigation Design**
I have used a standard Bootstrap, mobile responsive navbar for RefereE-Pay.
The menu items change depending on the user's status (logged-in or not).
 - New users only see: Home, Sign-up and Log-in
 - Once signed-up users are able to see the full menu list which enables them to interact with the whole app.

Additional anchor links have been provided in strategic locations to assist user navigation and provide easy access to certain pages. These are consistently located at the bottom of the content above the footer.
 - Landing Page
 Contains two anchor links prompting the user to sign-up. One located within text of a call-to-action section in the middle of the page. The second is located at the bottom of the page above the footer

 - Recipes page and Manage Recipes page
 Both have a link to the Add Recipes page, where the user is able to upload a new recipe

 - Profile Page
 Contains a link to the Manage Recipes page where they are able to Edit and Delete the recipes they have previously uploaded.

There should be no requirement for the user to ever have to resort to the Browser BACK button.
 - Error Pages
Each error page uses the template inheritance to provide the users the navbar seen throughout the site. should a user  encounter an unexpected error they are able to easily navigate back to the site without having to use the back button.

##### **Information Design**
The basic concept for the information design for W3Recipes is laid out in the following wireframes.

#### Wireframes <a name="wireframes"></a>
Wireframes for the original design concepts were created using Balsamiq.
##### Home Page
The landing page explains the purpose of the site to new and returning users. Functionality is limited from this page. Users are only able to Sign-up with a new account or Log-In to an existing account.
A Mini version of the Dashboard is shown to hopefully encourage users to find an empty country and to sign-up in order to provide a recipe for it.
![Landing Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/home-page.png "Landing Page Wireframe")

##### Sign-Up Page
Simple Sign-Up page enables the user to create unique log-in credentials based on an alphanumeric Username and alphanumeric Password. Back-end logic tests for duplicate entries. Redirects the user to the Recipes Page on successfully signing up.  
![Sign-Up](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/Sign-up.png "Sign-Up Page Wireframe")

##### Login Page
For returning users there is a separate Log-In page to enable access to the full functionality of the site.  
![Login](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/login-page.png "Log-In Page Wireframe")

##### Main Recipe Page
The Recipe page could be considered one of the key pages on the site. Uses READ functionality to display Recipes and provides the ability to filter Recipes by country or search by keywords. This page has pagination controls which are set to display a specific number of recipes to limit scrolling.
Users can select any recipe to view the full details of that recipe in order to make it.
![Recipes Display](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/recipes-page.png "Recipes Page Wireframe")


##### Individual Recipe Page
Provides users with the full recipe detail so they can check the ingredients and follow the steps to make it.
![Full Recipe](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/full-recipe.png "Full Recipe Wireframe")

##### Add Recipe Page
If the logged in user chooses to upload a recipe they can select "ADD RECIPE" from the navbar, which redirects the user to a page with various input fields where they can populate:
 - Recipe Name
 - An image representative of the recipe
 - Recipe Country
 - Recipe Category
 - Recipe Description
 - Servings
 - Vegetarian and Vegan selectors
 - Preparation and Cooking Time
 - Ingredients
 - Method

Once complete the recipe is uploaded to the MongoDB Atlas Recipes collection.  
![Add Recipe](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-recipe.png "Add Recipe Wireframe") 

###### Manage Recipes Page
This page is a copy of the Recipes Page, however rather than providing search functionality it displays only the recipes the user has uploaded, and enables the user to **UPDATE** or **DELETE** those recipes.
Edit redirects the user to a page similar to the Full Recipe page but with editing functionality.
Selecting Delete will render a check modal to double check the deletion request before removing the recipe.  
![Manage](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-recipe.png "Manage Recipes Wireframe")  

##### Edit Recipe Page
If the user selects EDIT on the Manage Recipes page, they are redirected to a page displaying the full recipe with their previous inputs pre-filling the various input fields. The user can change as few or as many field s as necessary or if they change their mind there is an option to Cancel the edit.  
![Recipe Edit](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-recipe.png "Edit Recipe Wireframe")


##### Profile Page
The profile page initially renders the basic profile information added on Sign-up. There is a button at the bottom of the profile card to enable the users to access the 'Edit Profile' page where they can customise their profile image and select whether or not to subscribe and provide an email address.  
![Profile Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/profile-page.png)  


##### Edit Profile Page
Enables the user to add a photo or avatar to their profile, provide their location and subscribe to the website.
I chose not to place the subscribe option on the landing page because until you log in you wouldn't necessarily know whether you wanted to subscribe to the website.
Thus it made sense to me to add this to a profile page  

![Edit Profile](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-profile.png)  

##### Dashboard Page  
The dashboard page enables the users to track how many countries the site has recipes for and also see how they compare to other users in terms of total recipes uploaded.
![Dashboard Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/recipe-dashboard.png)  

___
#### **Surface**
The aesthetics of RefereE-Pay was just as important to me as the functionality. Despite not using a lot of imagery for the app, what I have selected needs to be impactful, yet relaxed and fun to match the overall objective.

##### **Colour Scheme**
I typically find great inspiration for colour schemes on Pinterest. For W3Recipes I sought inspiration from the following website (https://mariahalthoff.com/blog/food-themed-color-palettes). Rather than stick to a single palette I have selected some of the colours from three of the palettes which match the browns, greens, oranges and reds in the hero image.  
  
![Colour Scheme](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/colour_palette_1.jpg "Colour Palette") ![Colour Scheme](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/colour-palette_2.jpg "Colour Palette") ![Colour Scheme](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/colour_palette_3.jpg "Colour Palette")

##### **Typography**  
Selecting the correct typography for this site is just as important as the other design aspects. My aim was to find fonts to reflect a more relaxed style, welcoming the user into the site. I also wanted variety to help demarcate different sections of the site. The primary criteria which I used to select the fonts for this app' were:
 - Readability
 - Relaxed Style
 - Weight

With these criteria and ideas in mind, I started loading various fonts into my CSS file and experimented with different combinations to find the ones which complemented each other and provided an aesthetically pleasing look to the site.
I have used Google fonts for each of my builds to date as it has an extensive library of fonts and is simple and reliable to use.  
![Google Fonts]https://fonts.google.com/?preview.text=Hello%20World!&preview.text_type=custom "Google Fonts"
 After some experimentation I settled on the following font styles:
 - Main Website Title and occasional text (Shrikhand)  
It was important to have a font which was clear and readable. I was also looking for bolder/thicker font for impact.  

![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/shrikhand.jpg)  

 - Page headings (Galada)  
For these I was looking for a more relaxed, fun font with a slightly cursive style and a bit of weight.  

![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/galada.jpg)  

 - Recipe Titles (Molle)  
I just had to use this font style! Something about it elicited a positive reaction with me and just seemed to work for the Recipe cards.  

![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/molle.jpg)  

 - Recipe Detail (Happy Monkey)  
Given the recipe notebook style I was trying to achieve I wanted a font which looked more natural and 'written' than the typical online typography.  

![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/happy-monkey.jpg) 

##### **Imagery** 
I was originally planning on using world map as the primary landing page image but decided against as this would have been confusing. I opted to go with a food montage which was an image I purchased from iStock
>**_I chose this image for the range of food types and the vibrant colour combining some of the greens browns and oranges I was looking to incorporate into the app.

The second image was sourced on the internet while searching for images for a Kebab recipe. It's just a great image which I liked and was keen to incorporate into the app.

Last but certainly not the least was my desire to have a subtle food related background behind the interactive elements. I found a really cool version designed and distributed by Freepik. The original version would have been too distracting so I opted to adjust the contrast and colours to fade the image. I also added my logo into the circular gap in the centre.
>**_I selected this particular image because it had a range of food types; each one is a decent size and they are not too densely packed._**
______

## **Database Schema** <a name="dbschema"></a>  
W3Recipes uses Mongo DB Atlas, a non-relational database to store and retrieve all of the user input data.
The schema for W3 Recipes is relatively simple and is illustrated below:
![DB Schema](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/db-schema.jpg "DB Schema")

The schema contains four collections, with each collection containing multiple documents. 
 - **Users**
 Stores user data. Initially populated with username and password and a default profile image when users register on the app. Once logged in users can upload their own image URL, specify their town or city. If the user elects to subscribe to the site, they are then able to provide their email address.
> **_I chose to do it this way so users are only required to provide some basic information and can register very easily. Once registered they can decide how much more they want to input at any subsequent point. I believe this simplifies the registration process_**

 - **Countries**
 This collection was populated from JSON file of 254 countries using the MongoDB Compass app, which simplified the transfer of the data into individual documents within the collection. The JSON data was copied from (https://flagpedia.net/download/api) and uses the CDN link provided on the website to display the flags on the recipe cards and pages. The individual UK countries were subsequently added into the collection by myself, as they did not appear in the original JSON file.
 Each document contains two id fields; the Atlas provided id and that provided in the JSON data. It also contains the country name, an alpha2 field which is the ISO two letter country code and an alpha3 field which is the ISO three letter country code.  
 The alpha2 code is used to render the appropriate country flag.  

 - **Recipe Category**
 The recipe_category collection contains short documents each defining the type of meal category each recipe might be identified by; such as Breakfast, Brunch, Lunch, Dinner, Desserts, Snacks, Appetisers and Sides. The recipe type documents were populated by myself and can be queried when a recipe is created or edited.
> **_There are many different ways to categorise recipes, but the one selected seems the most appropriate for my application_**
 
 - **Recipes**
 The recipes collection is the largest in the database as it combines user text input with data retrieved from the other collections; all of the user supplied input with fields from the other collections. I have selected what I view as essential fields for a basic recipe app, though clearly many more could be added.
Recipe Ingredients and preparation step data is formatted into an Array by splitting the data using each new line. When queried the data is formatted into a list for display.

___
## **Features** <a name="features"></a>
The following table lists the primary features provided by the W3Recipes app.

### **Existing Features**
|Feature|Description| Image URL |
|:-----:|-----|:----:|
| 001   | Landing page to convey the purpose of the website to new and returning users | [Landing](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/landing.jpg) |
| 002   | Simple registration Process with dedicated sign-up page | [Sign-up Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/register.jpg) |
| 003   | Dedicated Log-in screen for returning registered users | [Log-in Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/log-in.jpg) |
| 004   | Paginated "Recipes Page" where all recipes are displayed | [Recipes Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/recipes.jpg) |
| 005   | Recipe Filter function, filters recipes by country of origin. The image provided shows a search by the country "Wales". | [Recipe Filter ](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/filter.jpg) |
| 006   | Recipes text search function enables text based search on Title, recipe type, country, description and ingredients. The image provided illustrates a text search for all recipe Type "Sides" | [Recipe Text Search](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/search.jpg) |
| 007   | A Full Recipe Page provides complete recipe details | [Full Recipe Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/full.jpg) |
| 008   | A form which enables users to upload their own recipes | [Add Recipe Form Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/add.jpg) |
| 009   | Manage Recipes Page, from where users have the ability to Edit or Delete their own recipes | [Manage Recipes Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/manage-recipes.jpg) |
| 010   | Edit Recipe Form, enables users to modify all of the fields for any of the recipes they themseleves have uploaded. Original image is uploaded from the database, and the new image will be displayed below if the user decides to change the image file. |  [Edit Recipe](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit.jpg) |
| 011   | A Profile page contains user details and subscription preference | [Profile Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/profile.jpg) |
| 012   | An Edit Profile page to allow users the ability to Edit profile details and change subscription status | [Edit Profile Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-prof.jpg) |
| 013   | Delete function allows logged in users to delete any of their own recipes | [Delete Funtion](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/delete.jpg) | 
| 014   | Dashboard page displaying number of recipes by country, by user, meal type | [Dashboard Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/dash.jpg) |
| 015 | Footer | The footer for this web app contains links to the developers GitHub site and LinkedIn Account. The footer also contains a link to contact the developer via email. |  |

> **_I chose not to add a recipe category filter in this release as I thought it would make the top of the recipes page too clutters and would be an inelegant solution. Ideally I would like to incorporate an conditional dropdown menu where users can select between recipe category or countries._**

> **_The UK map is provided because the standard Atlas Charts world map only recognises the UK as a country and not the individual countries. Showing the individual countries is only possible by selecting the UK Countries map._**

> **_I have chosen not to provide a contact form for this web app. I believe that being able to contact the developer by email is sufficient for this initial release._**

____

### **Security Features**
Despite not being explicitly required for this build I have chosen to implement certain security features to provide some protection against unauthorised access to other users data.

 1. User Login

 User registers on the site with a simple username and password. Password gets hashed and salted using Password Hash from the Werkzeug Library.

![Sign-up Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/register.jpg)

 2. Session Cookie

 Once a user signs up or logs-in a unique session cookie is generated for the duration of their session. Recipe uploads are saved in the database against the session cookie username.  

 3.  Restricted Access

 The app logic checks the session cookie and only enables users to Manage (edit/delete) their own uploaded recipes. I have also attempted to prevent backdoor access to the delete function through retyping another url and inserting delete_recipe/Object_id.
 > **Thanks to Kotaro (Toto) Tanaka for highlighting this one while reviewing the app.**

![Restricted Access](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/restricted-1.jpg)

 4.  Restricted Access

 I have also attempted to prevent backdoor access to editing recipes from the Recipes or Full Recipe pages.  

![Unauthorised Access](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/restrict-2.jpg)

 5.  Deletion Check

 When a user selects the Delete Recipe button, the app renders a modal with a message to confirm the user wishes to delete that particular recipe.  

![Deletion Check](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/delete.jpg)

 6. Profanity Filter  

  Basic profanity filter, analyses user input and replaces any matching profanities with "****"

![Profanity Filter](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/profane.jpg)

7. Flask-SSLify

Configures the app to redirect all incoming requests to https//


### **Features Left to implement**
I have attempted to provide as much initial functionality in this app' as I can in the time available. Despite this there are features I would still like to incorporate in the future:
|   Feature     |     Description      |
|---------------|----------------------|
| Image File Upload  | Ability to upload images from users personal image library as opposed to only using URL's. This would be useful as it's a social media norm rather than using URL's |
| Image Validation | Validate image properties (size, aspect ratio etc) prior to uploading                 |
|Inappropriate image filter| Filter inappropriate images from being uploaded or worse, displayed |
| Conditional dropdown and seach | To reduce the number of search boxes on the Recipes page. Render either countries or recipe categories in the dropdown based on what the users selects|
______

## **Technologies Used** <a name="technologies"></a>  

This website has been built using the following core technologies:

##### Core Coding languages

- ![HTML 5](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/html-5-logo.png "HTML5") - HTML5
- ![CSS3](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/css3-logo.png "CSS3") - CSS3
- ![Python](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/Python.png "Python") - Python
- ![Javascript](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/javascript.png "Javascript") - Javascript


##### Integrations

- ![Flask](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/flask.png "Flask") - The project uses the Flask micro-framework and links with jinja to create the webpages
- ![Jinja](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/jinja.png "Jinja") - The project uses the Jinja templating engine
- ![Materialize CSS](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/materialize-css.png "Bootstrap 4") - Materialize CSS
- ![Font Awesome](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/fontawesome-logo.png "Font Awesome") - Font Awesome was the source of all icons.
- ![Google Fonts](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/googlefonts-logo.png "Google Fonts") - Fonts used on the website courtesy of Google Fonts
- ![JQuery](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/jquery.png "JQuery") - The project uses JQuery to simplify DOM manipulation.


#### Database Management System
- ![MongoDB Atlas](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongodb.png "MongoDB Atlas") - MongoDB Atlas  
- ![MongoDB Compass](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongodb.png "MongoDB Compass") - MondgoDB Compass was used to upload the JSON data to the W3Recipes Cluster  
- ![MongoDB Charts](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongodb.png "MongoDB Charts") - MongoDB Charts was used to create the website's dashboard

##### Version Control, storage and hosting

- ![Gitpod](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/gitpod-logo.png "Gitpod logo") - All of the website's code was written in the Gitpod IDE.
- ![Git](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/git-logo.png "git logo") - used for maintaining version control of the saved files.
- ![GitHub](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/github-logo.png "Github logo") - used as the primary repository for storying the files and documentation.
- ![Heroku](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-logo.png "Heroku logo")  - Deployment site
- [AWS](https://aws.amazon.com/?nc2=h_lg) - used to store all media and static files

##### Other

- Dillinger was once again used to edit the markdown required for the README.md and TESTING.md files.
______

## **Testing** <a name="testing"></a>
All of the testing conducted on this app', as well as any bugs encountered and explanations of solutions are documented in the following file:-
# [TESTING.md](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING.md) 

______
## **Database Creation** <a name="database"></a>
This app was developed using a SQLite3 database, but was transferred over to a Postgres DB on Deployment.
The ER diagram below illustrates the relationships between the each of the Models.
![RefereE-Pay Schema](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/RefereE-Pay%20Database%20Schema.jpeg)


## **Deployment** <a name="deployment"></a>
All of the files necessary to run this website have been stored in the GitHub repository. If you would like to work on your own version of this site or use it as a template for your own work, you have the option to either fork, or make a clone of the original repo.

### **Forking the GitHub Repository**
By forking the GitHub Repository you can make a copy of the original repository on your GitHub account, which enables you to view and/or make your own changes without affecting the original repository. This can be achieved using the following steps...

- Log in to GitHub and locate the GitHub Repository
- At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
- You should now have a copy of the original repository in your GitHub account.
### **Making a Local Clone**
- Log in to GitHub and locate the GitHub Repository
- Under the repository name, click the green "Clone or download" button; then the Download Zip button, extracting the files into your desired directory.
- Alternatively one can clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location where you want the cloned directory to be made.
- Enter the following command into the terminal
`git clone https://github.com/gazzaj/ci-ms4-referee-pay`
- For the app to function correctly you MUST install all of the files in the requirements.txt file. To do this, type the following command into the terminal.
`pip3 install -r requirements.txt`
- Set up the following environment variables to use the full functionality of the site.

   - DANGO_SECRET_KEY = your secret key.
   Unique Django secret keys can be obtained here [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)

   - STRIPE_PUBLIC_KEY = your stripe public key.

   - STRIPE_SECRET_KEY = your stripe secret key.

   - STRIPE_WEBHOOK_SECRET = your stripe webhook secret.

    **The web app will not function correctly without these variables.**

Your stripe variables can be found on your [Stripe dashboard](https://www.stripe.com)

Then migrate:

### **Heroku app creation**
As this is a full-stack website it has been deployed to Heroku.com using the following procedure:
- Log in to Heroku.com
- From the Dashboard, select the "New" button on the Top-Right of the screen
  - Select "Create new app"  

![Heroku]https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-app.jpg  

- Insert your app name
  - Heroku will let you know whether your chosen name is available
- Select the most appropriate region for your location
- Click the "Create app" button
- Select the Resources tab
  - Type postgres into the Ad-ons search bos 
  - Select Heroku Postgres
  - Choose an appropriate plan for your project (Hobby Dev-Free plan selected for initial deployment)

> To use Postgres you will need to go back to gitpod and install: **dj_database_url** and **psycopg2-binary**. 
   - pip3 install dj_database_url
   - pip3 install psycopg2-binary 
   In your app's settings.py file import dj_database_url
   Then scroll down to the Database settings and add a call to **dj_database_url.parse**
   Provide your database URL (Heroku - Settings - Reveal Config Vars - )
   
Connect to Database and Run Migrations
Load all of your fixture data if this is how you are working

### **Heroku Deployment**
The above steps will automatically bring you to the "Deploy" tab of your new app.  
![Deployment](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-github.jpg)

 1. In the "Deployment Method" section select Github  
 Once selected a Connect to GitHub section will display below

![Deployment](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-app-menu.jpg)  

 2. Ensure your profile is displayed
    - If not type in your GitHub username

![Heroku + Github Repo](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-repo.jpg)  

 3. Search for, and select the Repo corresponding to the Heroku app
 4. Click "Connect"

This app uses configuration settings and secret keys for MongoDB and Session cookies respectively, which Heroku requires in order for the website to function as desired. To do this you need to set the Config Vars within Heroku:
 - Under the "Settings" tab, in the Config Vars section select the "Reveal Config Vars" button.  

![Config Vars](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-config-vars.jpg)  

This will reveal a form for inputting the key and value pairs necessary to connect to the app.

|  KEY  |  VALUE  |
|:-----:|:-------:|
|   IP  | 0.0.0.0 |
|  PORT |  5000   |
| SECRET KEY | Randomly Generated Fort Knox Key|
| MONGO_URI | Your unique MongoDB URI |
| MONGO_DBNAME | Your unique Mongo DB name |

The above Mongo_URI variable can be found in the appropriate Mongo DB Project under Cluster by selecting "Connect"
 1. Select "Clusters"
 2. Select "Connect"
 3. Select "Connect your application"
 4. Choose your Driver and Version
   - **Remember to substitute in your own DBNAME and Password**
 5. Copy your connection string

### **Enabling Automatic Deployment**
 - Select the Heroku "Deploy" tab
 - In the "Automatic deploys" section select the branch you wish to use
 
**There is no difference between the developed version of W3Recipes and that deployed on Heroku**
______

## **Resources** <a name="resources"></a>

I have attempted to work independently as much as possible while building this website, choosing to solve my own issues, using web resources wherever possible. Thus, my main resource throughout this project was again the trusty Google search.
 Aside from Google I have made use of the following resources: -

- [Balsamiq](https://balsamiq.com/wireframes/) – Wireframing Tool
- Code Institute course material and Walkthrough projects
- Google DevTools - for trouble shooting and first pass testing
- Google Lighthouse - Website performance testing
- [StackOverFlow](https://stackoverflow.com/) – Web based coding tips
- [W3Schools](https://www.w3schools.com/) – General coding resource
- [Pexels](https://www.pexels.com/) – Licence free image repository
- [BeFunky](https://www.befunky.com/create/resize-image/) – Online image resizer
- [W3C Validator](https://validator.w3.org/) - HTML and CSS Validation tool
- [JSHint](https://jshint.com/) - JavaScript code analysis tool
- [JSLint](https://jslint.com/) - JavaScript code quality analysis tool
- [Python Beautifier](https://www.tutorialspoint.com/online_python_formatter.htm) - Python code beautifier
- [PEP8 Error Check](http://pep8online.com/) - Python PEP8 validation
- [SEO Site Checkup](https://seositecheckup.com/tools/custom-404-error-page-test) - Checks to see if you have a custom 404 page
- [Online JavaScript Beautifier](https://codebeautify.org/jsviewer) - Useful tool for indenting JS code
- [Am I responsive?](http://ami.responsivedesign.is/) - Provides a simple view of a websites responsiveness.
- [Responsinator](https://www.responsinator.com/) - Fairly comprehensive responsiveness testing
- [Regex Generator](https://regex-generator.olafneumann.org/) - Helps compile Regular expressions
- [Regex 101](https://regex101.com/) - Useful Regex tester

______

## **Credits** <a name="credits"></a>

### **Content**
The content of this website was created by Gareth John. Snippets of code have been copied from official documentation and other sources credited below and in the respective code files. All pre-loaded recipes were written by the developer.

### **Media** <a name="media"></a>

The photos used in this site, or in pre-populated recipes by the developer were obtained from the following sources:
| Photo | Description | Source | Attribution |
|-------|-------------|--------|-------------|
| 001   | [App Logo](https://www.freelogodesign.org/manager) | Free Logo Design | Designed by the developer |
| 002   |[Landing Page](https://pixabay.com/photos/football-goals-grass-lawn-4789850/)| Pixabay | No Attribution Required |
| 003   | [Shish Kebab](https://www.pexels.com/photo/food-plate-restaurant-dinner-5175623/) | Pexels | Shameel Mukkath |
| 004   | [Club Badges](https://www.cheltenhamyouthleague.co.uk/clubdirlist/1021)| Cheltenham Youth Football League website |  |
| 005   | [Kofta Kebab](https://cdn.pixabay.com/photo/2015/08/20/15/15/grill-897553_960_720.jpg) | Pixabay | No Attribution Required |
| 006   | [Welsh Cakes](https://cdn.pixabay.com/photo/2018/10/05/14/55/cake-3726058_960_720.jpg) | Pixabay | No Attribution Required |
| 007   | [Lamingtons](https://upload.wikimedia.org/wikipedia/commons/c/c5/Mocha_Flake_amingtons.jpg) | Wikimedia Commons | Andy Cavell |
| 008   | [Goal](https://thenounproject.com/term/goal/56918/) | thenounproject.com  | Amos Kofi Commey |
| 009   | [Yellow Card](https://pixabay.com/photos/avocados-guacamole-drink-food-386795/) | thenounproject.com adapted by the developer | inDhika coloured by the developer |
| 010   | [Red Card](https://pixabay.com/photos/food-refreshment-yorkshire-puddings-3264773/) | thenounproject.com adapted by the developer | inDhika coloured by the developer |

____

### **Code Snippets** <a name="code"></a>
Much of the structure of this site follows what was taught during the Backend Development - Task Manager walkthrough project provided by Code Institute, but has been heavily modified to suit a recipe database site with additional functionality not provided in the walkthrough.

 | Code Snippet | Description | Source |
 |:-------:|-------------|:------:|
 |Animated Arrows| Animated arrows in the Landing Page call to action | https://freefrontend.com/css-arrows/#animated-arrows|
 |Remove blank lines and spaces from text inputs | Ensure that if users entered blank lines into the ingredients and methods they could be removed to maintain a neat list | https://www.kite.com/python/answers/how-to-remove-empty-lines-from-a-string-in-python |
 | Country Flag CDN | Code snippet required to programmatically embed flags into the website | https://flagpedia.net/download/api |
 | Image URL display | Display the image when the URL is provided in a textbox | https://stackoverflow.com/questions/31398473/load-image-in-div-from-url-obtained-from-a-text-box/31398762|
 |Pagination| Splits the recipes collection and displays a maximum of 6 recipes/page|https://www.hacksparrow.com/databases/mongodb/pagination.html|
 | Materialize Select on iOS | Solves issues with select elements not displaying correctly on iOS devices | https://stackoverflow.com/questions/52850091/materialize-select-and-dropdown-touch-event-selecting-wrong-item/52851046#52851046 |
 | Form Validation | Add Recipe Form validation adapted from HTML form guide | https://html.form.guide/snippets/javascript-form-validation-using-regular-expression/ |

### **Acknowledgements** <a name="acknowledgements"></a>

 - Thanks as always to everyone at the Code Institute for the excellent video tutorials and fantastic introduction to Django and Automated testing in Python and some of the different databases structures. Chris Zielinski's Walkthrough projects were extremely helpful and enjoyable.
 - Grateful thanks to Tutor support who were on hand when most needed to provide assistance.
 - My mentor Precious Ijege for his support and advice throughout this final project. Thank you also for providing such a thorough review of the finished project helping ensure it was fit for submission.
 - My appreciation to all the users who took time to test the web app:
______
### **Technical Support** <a name="technical"></a>
If you encounter any issues with this website, or require any support please email the developer [johnge71@gmail.com](mailto:johnge71@gmail.com)