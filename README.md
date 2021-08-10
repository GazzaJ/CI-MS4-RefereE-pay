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

**There is no difference between the developed version of RefereE-Pay and that deployed to Heroku**

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
The purpose of RefereE-Pay web app is to provide grassroots football coaches and managers with an electronic means of communicating with and paying match officials fees. The aim is to try and provide a visual dashboard of each fixture, containing all of the relevant information needed by either the home or away coach. or the ref, in a single location.
 - As the site owner and grassroots team coach I get to create a potential solution for the grassroots game
 - Users get access to all of the fixtures in the data base; are able to filter and search to narrow down to a specific team, 
 - On selecting one of their fixtures the home team coach can add the match to the kit bag and subsequently pay the match fees.
 - The home team coach can also communicate with the referee through the app so that the coms are associated with the match
 - Referees are able to update their travel expenses, if they have any.
 - The Referee can also communicate with the home team coach with respect to a particular match/fixture.
 - Admin Users can add and edit Clubs, Teams and Matches, as well as act as a proxy for the user and perform the tasks of either coach or ref.
 
> **The ultimate intention is to provide a more hollistic and cashless solution to matchday payments and communication.**

#### **Scope**
This app is intended to address **two** key needs not currently solved by existing commercial apps, namely:
- **Paying Match Officials match fees electronically.**
- **In app communication with the ref; with messages linked and viewed by individual match.** 

The scope could easily extend to try and include sophisticated league and match creation algorithms, or seek to track and display results. This app is a MVP; a concept of what could be provided to address the above needs in the time available to complete the project. The additional features could certainly be developed and added in the future, which could eventually produce a single hollistic app for all league, match, payment and communication needs.

I have grouped the key features required for this app to function as intended into their associated CRUD category for thoroughess:
 - **Create** Competitions, Clubs, Teams and Matches by specific age group. 
 - **Read**, or view all of the Clubs, Teams or Matches stored in the database.
    - Display all relevant match detail in one convenient dashboard
    - Filter those matches by age group, or Team name
    - Search for a team and display that teams games
 - **Update** Enable Admin users to edit Clubs, Teams and Matches as required, and also allow the Match Officials to input any travel expenses they have into the fixture information.
 Enable Coaches and Referees to communicate with each other through a simple in app message app.
 - **Delete** function for Site Admins, who can remove Clubs, Teams and fixtures as required

The final but most critical part of this app is the requirement for site security, which serves three purpooses:
1. Mimic existing commercial app security
It may come as a surprise but existing app provided by Regional FA's have tight security limiting access to registered club and match officials 
2. Provide security for the e-commerce platform so users feel their transactions are secure (User Story #)
3. Prevent unwanted and unauthorised editing or deletions of records, 

##### Functional Requirements
App functionality is provided through a typical intuitive, mobile responsive navbar. The navbar menu options increases once a user registers or logs into the website, increasing what they can view and achieve.
Additional interactive anchor links are provided throughout to provide users with multiple ways of navigating around the app.

##### Content Requirements
Much of the content in this app revolves around the Matches Model, which contains lists of Venues, Clubs, Teams, Match Officials and Games I have uploaded through fixture files. Additional data has subsequently been added using the app's CRUD functionality
I have deliberately included just enough content for this app to function as defined in the Scope, and no more. This has been a conscious decision to prevent unnecessary scope creep.
 
___

#### **Structure**  
The structure of RefereE-Pay is user dependent with user roles dictating what each group can achieve:
  - **Anonymous Users** can view the fixture list, Clubs and Teams only. They do not have access to the match details, nor can they access the payment system.
  - **Registered Users** have the functionality as anonymous users with the addition of viewing match details, but cannot access the kit bag or complete any transactions.
  - **Registered Coaches** are able to view the Fixtures, Clubs and Teams as well as the individual Match Details. They have the ability to add their teams HOME games to the kit bag and to complete payment. Home team coaches are also able to add messages to the fixture to communicate with the Match Official
  - **Match Officials** - have the same viewing capabilities as Coaches but obviously cannot pay the required match fees. They can add their travel expenses and send in app messages to the Home team Coach
  - **SuperUsers** - have full and unrestricted access to all functionality

The app is constructed from **19** distinct pages which are accessed through the main and mobile navbars. 

The workflow for RefereE-Pay is quite complex, but I have attempted to capture it below:
![Workflow](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/referee-pay-flow.jpg "Website workflow")

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
 - **Clubs**
 The clubs page displays all of the clubs saved in the database as a card displaying club badge and club name. Clicking the club badge redirects the user to the club website. Below the badge and name sits a **"Teams"** button which takes the user to a separate page which displays all of the teams saved in the database, for that club.
Admin / Superusers also have Edit and delete buttons to select from.
   - Edit - redirects to a form displaying club information where the superuser can change the club name, badge or website URL.
   - Delete  - does as it says once the superuser has confirmed the deletion
 - **Teams**
 The Teams page displays all of the teams for the selected CLub by age group and shows team name and the Manager/coach for that team. There is limited data in the team menu, as designed, however this could be increased in the future to include contact details for the Manager/Coach. 
Admin / Superusers have the ability to Edit and Delete the teams:
   - Edit - redirects the superuser to a form page where the team detail can be adjusted
   - Delete  - does as it says once the superuser has confirmed the deletion
 - **Kit Bag**
 This section of the app stores (for the duration of the session) any of the matches a user has selected for payment, and provides the user with a useful summary of the:
   - Match Fees
   - Match Fines
   - Match Total
   - Grand Total 
  
- **Checkout**
This page enables users to pay the match officials fees for any games they have in their kit bag.  

 - **User Profile**
Displays the users billing address, if they have elected to save it, and a summary of the matches they have paid for.
 - **Admin**
A special menu option has been provided for Admin/Superusers to create new Competitions, Clubs, Teams and Matches. Each one redirects the superuser to a form page where they can input and save the relevant information.
Match creation is currently simplistic choice based form. Future versions could use a more sophisticated 
> I had opted to keep this as a superusers task because it didn't make sense to enable any user to log in and start creating new teams.




##### **Information Design**
Information is provided to users on multiple pages; Matches, Match Detail, Clubs, Teams, Kit Bag and Profile.
Despite rendering slightly different information the structure of each page has been designed to provide a similar layout and theme.

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
The intention was to provide a relatively simple app which maintains a clean and consistent interface design, re-using elements and page styles wherever possible to benefit from the users learned behaviour. 
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
The landing page explains the purpose of the site to new and returning users. Functionality is limited from this page. Users are only able to Sign-up with a new account or Log-In to an existing account. Anonymous users are able to navigate to the Matches, Clubs and Teams pages but cannot go any further.

![Landing Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/home-page.png "Landing Page Wireframe")

##### Sign-Up Page
A simple Sign-Up page provided by All Auth package enables the user to create unique log-in credentials based on an alphanumeric Username and alphanumeric Password. Back-end logic tests for duplicate entries. Redirects the user to the Recipes Page on successfully signing up.  
![Sign-Up](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/sign-up.png "Sign-Up Page Wireframe")

##### Login Page
For returning users there is a separate All Auth Log-In page to grant access into the site.  
![Login](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/sign-in.png "Log-In Page Wireframe")

##### Matches Page
The Matches page could be considered one of the key pages on the site as it is the entry point for each of the match detail pages which subsequently allow users to add their matches to the kit bag for payment. Uses READ functionality to display basic detail for each match. and provides the ability to filter matchesd by different categories. A seaarch box will allow users to  find specific teams. This page has pagination controls which are set to display a specific number of matches to limit scrolling.
Registered Users can select any match to view the full details of that match.
![Matches](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/matches-page.png "Matches Page Wireframe")


##### Match Detail Page
Provides users with the full match details such as:
 - Home and Away Team
 - Home and Away Coaches
 - Venue and Kick-off
 - Match Officials
 - Match officials fees
 - Messages
...and will permit home team coaches to pay match fees and also communicate with the referee.
![Match Detail](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/match-detail.png "Match Detail Wireframe")

##### Refs Page
This page is intended as a dashboard for the Referee and match officials to interact with the Team coaches and add their travel expenses.
![Ref's Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/refs-page.png "Ref's Page Wireframe")
> **In hindsight I decided not to build this page, but to instead allow the Ref and Home Team Coach to interact with the Match Detail page. From this page the Match Officials can add their travel expenses and communicate with the Home team coach.**

##### Clubs
Simple page displaying each team on a card, each one having a "Teams" button which takes the user to the list of teams for that Club.
Admin / Superusers also have the functionality to Edit or Delete the club at this point.
![Clubs](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/clubs.png "Club Directory Wireframe")

##### Add Club
A very simple form page where Admin/Superusers can add a new club to the directory
![Add Clubs](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/add-club.png "Add Club Wireframe")

##### Edit Club
Almost a mirror image of the Add Club form page. The Edit Club page displays current club information and allows Admin/Superusers to edit the details as required.
![Edit Club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/edit-club.png "Edit Club Wireframe")

##### Teams
A simple page listing each of the chosen Club's teams by age group and displaying the Manager/Coach for that Team.
Admin / Superusers also have the functionality to Edit or Delete the Team at this point.
![Teams](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/teams-page.png "Teams Page Wireframe")

##### Add Team Page
A very simple form page where Admin/Superusers can add a new team to the directory.
![Add Teams](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/add-team.png "Add Teams Wireframe")

##### Edit Team
Similat to the Edit teams page this page is a replica of the Add Team form page. The Edit Team page displays current Team information and allows Admin/Superusers to edit the details as required.
![Edit Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/edit-team.png "Edit Team Wireframe")

##### Kit Bag
A simple page which stores any matches the user has selected to place in the kit bag for payment. The matches remain in the kitbag for as long as the session cookie is active. 
![Kit Bag](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/order-detail.png "Kit Bag Wireframe")

##### Payment
The is the key page wher the user enters their billing address and card details in order to process the payment of the match officials fees. 
![Payment](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/payment.png "Payment Wireframe")

##### Checkout Success
The Checkout success page is the final page in the payment process, summarising the matches paid for and confirming a successfull payment
![Profile](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/checkout-success.png "Profile Wireframe")

##### Profile Page
The profile page initially renders the basic profile information added on Sign-up. There is a button at the bottom of the profile card to enable the users to access the 'Edit Profile' page where they can customise their profile image and select whether or not to subscribe and provide an email address.  
![Profile](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/profile-page.png "Profile Wireframe")

___
#### **Surface**
The aesthetics of RefereE-Pay was just as important to me as the functionality. Despite not using a lot of imagery for the app, what I have selected needs to be impactful, yet relaxed and fun to match the overall objective.

##### **Colour Scheme**
I typically find great inspiration for colour schemes on Pinterest. For W3Recipes I sought inspiration from the following website (https://mariahalthoff.com/blog/food-themed-color-palettes). Rather than stick to a single palette I have selected some of the colours from three of the palettes which match the browns, greens, oranges and reds in the hero image.  
  
![Colour Scheme](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/profile.png "Colour Palette") 

##### **Typography**  
Selecting the correct typography for this site wasn't as important as it had been for some of the other projects I have worked on. Since this app comprises an e-commerce platform my aim was to find complimentary fonts which were relatively simple yet easily. I also wanted variety to help demarcate different sections of the site. The primary criteria which I used to select the fonts for this app' were:
 - Simplicity
 - Readability

With these criteria and ideas in mind, I started searched through the [Google Fonts](https://fonts.google.com/?preview.text=Hello%20World!&preview.text_type=custom) library, however my main font was eventually chosen when I created the website logo using the Exo font.

 - Main Website Headings, Club and Team Names (Exo)  
It was important to have a font which was clear and readable. I was also looking for bolder/thicker font for impact.  

![Exo Font](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/exo-font.jpg "Exo Font")  

 - Page headings (Galada)  
For these I was looking for a more relaxed, fun font with a slightly cursive style and a bit of weight.  

![Roboto Font](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/roboto-font.jpg "Roboto Font")  

>>**I had considered using a sport themed font for this app, but decided I want to overdo it, and certainly didn't want to detratct from the main purpose of the site.**

##### **Imagery** 
I had a very clear plan for the site images right from the very early planning stages. I wanted to find images showing amateur football in action including the referee or other match officials. I found a decent selection of good quality, licence free images on Pixabay. The full list of images and credits are in the Cedits section.

I also wanted to add some fun to the messages rendered by the app by adding footbal icons matching the level of message, such as:
 - Error = Red Card

 - Warning = Yellow Card

 - Alert = Tactics Board

 - Success = Goal

______

## **Database Schema** <a name="dbschema"></a>  
This app was developed using a SQLite3 database, but was transferred over to a Postgres DB on Deployment.
The ER diagram below illustrates the relationships between the each of the Models.
![RefereE-Pay Schema](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/referee-pay-db-schema.jpeg "Database Schema")

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



____

### **Security Features**
Despite not being explicitly required for this build I have chosen to implement certain security features to provide some protection against unauthorised access to other users data.

 1. User Login




### **Features Left to implement**
I have attempted to provide as much initial functionality in this app' as I can in the time available. Despite this there are features I would still like to incorporate in the future:
|   Feature     |     Description      |
|---------------|----------------------|
| Conditional dropdown and seach | To reduce the number of search boxes on the Recipes page. Render either countries or recipe categories in the dropdown based on what the users selects|
| Algorythm based match creation| To create a more sophisticated means of creating multiple games at once rather than manually creating each game|
|Person to Person Payment| The ability to pay the Match officials directly rather than paying the app as it currently stands|
______

## **Technologies Used** <a name="technologies"></a>  

This website has been built using the following core technologies:

##### Core Coding languages

- ![HTML 5](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/html-5-logo.png "HTML5") - HTML5
- ![CSS3](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/css3-logo.png "CSS3") - CSS3
- ![Python](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/Python.png "Python") - Python
- ![Javascript](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/javascript.png "Javascript") - Javascript


##### Integrations

- ![Django](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/django.jpg "Django") - The project uses the Django framework
- ![Bootstrap CSS](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/Bootstrap-logo.png "Bootstrap 4") - Bootstrap 4.6
- ![Font Awesome](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/fontawesome-logo.png "Font Awesome") - Font Awesome was the source of all icons.
- ![Google Fonts](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/googlefonts-logo.png "Google Fonts") - Fonts used on the website courtesy of Google Fonts
- ![JQuery](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/jquery.png "JQuery") - The project uses JQuery to simplify DOM manipulation.


#### Database
- ![SQLite3](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/sqlite.jpg "SQLit3") - SQLite3  
- ![Postgres](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/postgres.png "Postgres") - Postgres was used as the deployed DB  

##### Version Control, storage and hosting

- ![Gitpod](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/gitpod-logo.png "Gitpod logo") - All of the website's code was written in the Gitpod IDE.
- ![Git](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/git-logo.png "git logo") - used for maintaining version control of the saved files.
- ![GitHub](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/github-logo.png "Github logo") - used as the primary repository for storying the files and documentation.
- ![Heroku](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-logo.png "Heroku logo")  - Deployment site
- [AWS](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/aws.png "AWS logo") - used to store all media and static files

##### Other

- Dillinger was once again used to edit the markdown required for the README.md and TESTING.md files.
______

## **Testing** <a name="testing"></a>
All of the testing conducted on this app', as well as any bugs encountered and explanations of solutions are documented in the following file:-
# [TESTING.md](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING.md) 

______
## **Database Creation** <a name="database"></a>




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
`pip3 install dj_database_url`
`pip3 install psycopg2_binary`
- In your app's settings.py file import dj_database_url
`import dj_database_url`
- Then scroll down to the Database settings and add a call to **dj_database_url.parse**
```
DATABASE = {  
    'default': dj_database_URL.parse('DATABASE_URL')
}
```
- Retrieve your database URL from Heroku  (Heroku - Settings - Reveal Config Vars - )
   
- Connect to Database and Run Migrations by typing the following in the terminal:
`python3 manage.py migrate`

- Load any fixture data you have used, if this is how you have elected to add your data
`python3 manage.py loaddata <filename>.json`
- Create a superuser
`python3 manage.py createsuperuser`
- Create an IF - ELSE statement in the Database setrtings section of settings.py to allow access to either database whether you are in DEVELOPMENT or DEPLOYED mode
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_URL.parse('os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {'ENGINE': 'django.db.backends.sqlite3'
                    'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
Your Postgres database should now be ready for use.

- For our app to work correctly we need to install Gunicorn
`pip3 install gunicorn`

- Next we need to create a procfile in our app, and add in the following code:
`web:gunicorn <your app name>.wsgi:application`

### **Heroku Deployment**
1. To start the Heroku deployment, first log into Heroku from the terminal using:
`heroku login -i`
2. You will need to tempoarily disable the static files as we will set these up on Amazon AWS. To do this type
`heroku config:set DISABLE_COLLECTSTATIC=1 --app <app name>`
3. In `settings.py` add Heroku to the allowed hosts and localhost so the project can run locally and as a deployed site
`ALLOWED_HOSTS = ['<your Heroku app name>.heroku.com', 'localhost']`
4. 
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
|   DATABASE_URL  | 0.0.0.0 |
|  SECRET_KEY |  5000   |
| STRIPE_PUBLIC_KEY | Your Stripe Public Key|
| STRIPE_SECRET_KEY | Your Stripe Secret Key |
| STRIPE_WH_SECRET | Your Stripe Webhook secret key |

 5. Copy your connection string

### **Enabling Automatic Deployment**
 - Select the Heroku "Deploy" tab
 - In the "Automatic deploys" section select the branch you wish to use

### **Connect to Amazon AWS**
Amazon AWS has been utilised to store both STATIC and MEDIA files for our deployed web app.
Follow these steps to connect your app to AWS:
1. Create an Amazon AWS account
   - Follow all of the registration steps until you are back at the AWS Console view
2. Create a new **"Bucket"** for your data.
   - Navigate to the S3 service of AWS, and under the buckets section select **Create bucket**
 ![AWS Bucket Creation](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/aws-bucket.jpg "AWS Bucket Creation")
   - Name the bucket (advisable to give it the same name as your website)
   - Select the Region nearest you.
   - Uncheck the **Block Public Access** checkbox and acknowledge the bucket will be public
   - Scroll down and select **Create bucket**
3. Select your newly created bucket from the Buskets window and then select the **Properties** Tab
   - Scroll down towards the botton and **Enable Static web hosting**
   - For the Index and Error values enter `index.html` and `error.html` respectively
   - Save the properties
4. Now select the Bucket **Permissions Tab**
   - Scroll to the bottom and type the following into the **Cross-origin resource sharing (CORS)** box to set up the required access between our Heroku app and our S3 bucket.
   ```
   [
        {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
        }
    ]
   ```
 5. Next scroll up to the **"Bucket Policy"** section.
 6. Click on **"Generaget policy"** to create a security policy for our bucket.
 7. Select **"S3 Bucket Policy"** from the dropdown menu.
 8. Type * into the **"Principal"** field to allow all principals.
 9. Select **"GetObject"** from the actions dropdown menu.
 10. Paste in your Amazon Resource Name (ARN) into the ARN box
 Your ARN is available on the Properties Tab
11. Click **"Add Statement"**
12. Then click **"Generate policy"**
13. Copy the code from the Policy JSON Document window and paste into the Bucket policy editor
14. To allow access to all resources in the bucket add a "/*" to the end of the Resource key
` "Resource": "<your ARN>/*",`
15. Click **"Save"**
16. Scroll down to the **"Access control list"** and select the **"List"** checkbox for **"Everyone"**
 ![Access Control](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/access-control.jpg "AWS Access Control")

#### **Creating an AWS User Group**
- Return to the AWS Console and under the services dropdown menu locate the **"IAM"** (Identity and Access Management) service.
- Select **"User Groups"** from the Menu
- Click **"Create group"**
 ![IAM](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/iam-usergroup.jpg "IAM User Group")
- Add a name which is linked to your project e.g. **manage-<your project name>**
- Click **"Next"** through to the end and then **"Create group"**
- Once done select **"Policies"** and click the **"Create policy button"**
![IAM-Policy](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/iam-createpolicy.jpg "Create IAM policy")
- Select the **"JSON"** Tab and click the **"Import managed policy link"**
![IAM-Policy](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/iam-json.jpg "IAM import policy")
- Search for **"S3"** in the "import managed policy" modal, and select the **"AmazonS3FullAccess"** policy.
- Click **"Import"**

Realistically we only want to allow full access to our Bucket and everything in it.

- Retrieve your ARN from your Bucket - Policy tab in S3
- Paste the ARN into the JSON
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "<your ARN>",
                "<your ARN>/*"
            ]
        }
    ]
}
```
- Click **"Review policy"**
- Name it something appropriate to your project e.g. **<Your Project name> policy**
- Add a description
- Click **"Create policy"**

You should be returned to the Policies page with a notification that your policy has been created.

- Return to the User Groups menu item
- Select the user group you created earlier
- Select the **"Permissions"** Tab, click **"Add permissions"** and select **"Add policy"** from the options
![Add Policy](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/iam-json.jpg "Add Policy")
- Locate the policy you just created and attach it.

#### **Creating a User**
Follow these steps to create a user in the User Group
1. Back on the main IAM page select **"Users"** from the menu items
![IAM User](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/create-user.jpg "Create a User")
2. Select **"Add users"** and create a username relevant to your project e.g. **<your project name>-staticfiles-user**
3. Allow programmatic access by selecting the appropriate checkbox
4. Select **"Next: Permissions"**
5. Select the User Group you created earlier to add the new User to the group
6. Click **"Next"** all the way to the end and click **"Create user"**
7. At the Final step, you are notified of successfull creation, below which there is a button to **"Download .csv"**.
8. Click **"Download .csv"**

**Ensure you download and save this file to a safe location as it contains the Users Access Key and Secret Key.
You will need these to authenticate them from Django and you cannot download them again once you proceed beyond this page**.
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
| 002   |[Landing Page](https://pixabay.com/photos/football-goals-grass-lawn-4789850/)| Pixabay | olebertelsen |
| 003   | [Matches Background](https://pixabay.com/photos/football-ball-sport-goal-kick-1678992/) | Pixabay | SeppH |
| 004   | [Club Badges](https://www.cheltenhamyouthleague.co.uk/clubdirlist/1021)| Cheltenham Youth Football League website |  |
| 005   | [Checkout](https://pixabay.com/photos/referee-linesman-sport-football-4733190/) | Pixabay | Planet_fox |
| 006   | [Goal](https://thenounproject.com/term/goal/56918/) | thenounproject  | Amos Kofi Commey |
| 007   | [Yellow Card](https://thenounproject.com/term/yellow-card/2022056/) | thenounproject adapted by the developer | inDhika coloured by the developer |
| 008   | [Red Card](https://thenounproject.com/term/yellow-card/2022056/) | thenounproject adapted by the developer | inDhika coloured by the developer |
| 009   | [Tactics Board](https://thenounproject.com/term/football-tactics/2278781/) | thenounproject | ProSymbols, US |
| 010   | [Burrows](https://thenounproject.com/term/football-tactics/2278781/) | Cheltenham Borough Concil | Cheltenham Borough Concil |
| 011   | [Beeches](https://thenounproject.com/term/football-tactics/2278781/) | Cheltenham Borough Concil | Cheltenham Borough Concil |
| 012   | [King George V](https://thenounproject.com/term/football-tactics/2278781/) | Cheltenham Borough Concil | Cheltenham Borough Concil |
| 013   | [Naunton Park](https://thenounproject.com/term/football-tactics/2278781/) | Cheltenham Borough Concil | Cheltenham Borough Concil |
| 014   | [Priors Fam](https://thenounproject.com/term/football-tactics/2278781/) | Cheltenham Borough Concil | Cheltenham Borough Concil |
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