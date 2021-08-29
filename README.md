![RefereE-Pay](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/readme-title.jpg "RefereE-Pay")

# [**RefereE-Pay**](https://ci-ms4-referee-pay.herokuapp.com/)

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

![Am I responsive images](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/am-i-responsive.jpg "Am I Responsive")

**There is no difference between the developed version of RefereE-Pay and that deployed to Heroku**

## Table of contents

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
|  2  | Site User  | Easily login or logout | Access the match details and my personal account information |
|  3  | Site User  | Easily recover or reset my password in case I forget it | Recover access to my account |
|  4  | Site User  | Receive an email confirmation after registering | Verify that my account registration was successful |
|  5  | Site User  | Have a personalised user profile | View my personal payment history and payment confirmations, and save my payment information |

#### **Searching and Filtering**
| User Story |  As a  | I need to | In order to |
|:----------:|-------|-----------|-------------|
|  6  |  Team Manager  | Easily find and view the database of matches | understand who I am playing and when |
|  7  |  Team Manager  | Sort all fixtures by age | Easily identify all fixtures by age group |
|  8  |  Team Manager  | Sort fixtures by team | Easily find different fixtures by team name |
|  9  |  Team Manager  | Be able to quickly navigate through the list of fixtures, | find different fixtures. |
| 10  |  Team Manager  | Search for fixtures by team name | Find a specific fixture I'd like to pay the match official fees for |

#### **Communication**
| User Story |  As a  | I need to | In order to |
|:----------:|-------|-----------|-------------|
| 11  |  Team Manager  | Communicate with the referee | Confirm match status and alert them of any issues with the condition of the pitch. |
| 12  |  Team Manager  | Post/send pictures to the Referee | Illustrate pitch conditions ahead of any game |
| 13  |  Referee  | Communicate with the Home team manager | Reply to any concerns or issues raised ahead of the game |

#### **Selection and Checkout**

| User Story |  As a  | I need to | In order to |
|:----------:|-------|-----------|-------------|
| 14  |  Team Manager  | Easily select the fixture | Discover the full details of that match |
| 15  |  Team Manager  | Have a simple cashless method to pay the referee | Pay the assigned match officials their match fees |
| 16  |  Team Manager  | View any pending payments in my kit bag | Identify the total cost of match fees for each game and the grand total |
| 17  |  Team Manager  | Easily enter my payment infoirmation | Complate my payment quickly and efficiently |
| 18  |  Team Manager  | Feel my personal and payment information is secure and safe | Feel confident in providing required information to complete a payment |
| 19  |  Team Manager  | View a payment confirmation after checkoutt | Verify that I have successfully paid my match fees |
| 20  |  Team Manager  | Receive an email confirmation after checkout | Have recorded confirmation of each payment |

#### **Admin and Management**
| User Story |  As a  | I need to | In order to |
|:----------:|-------|-----------|-------------|
| 21  |  Site Admin  | Add, edit and delete Matches | Keep pace with league fixtures and provide a long term solution  |
| 22  |  Site Admin  | Add, edit and delete Clubs | Keep track of league clubs and those using the site |
| 23  |  Site Admin  | Add, edit and delete Teams | Keep track of all clubs teams |
| 24  |  Referee  | Add my travel expenses | ensure I get paid the full amount for my services |

___

### **The 5 Planes of UX** <a name="planes"></a>
I refer to the five planes of UX to provide a framework for discussing the finer points of this app's design and development.

#### **Strategy**  
The purpose of RefereE-Pay web app is to provide grassroots football coaches and managers with an electronic means of communicating with and paying match officials fees. The aim is to try and provide a visual dashboard of each fixture, containing all of the relevant information needed by either the home or away coach. or the ref, in a single location.
 - As the site owner and grassroots team coach myself I get to create a potential solution for the grassroots game.
 - Users get access to all of the fixtures in the data base; are able to filter and search to narrow down to a specific team, 
 - On selecting one of their fixtures the home team coach can add the match to the kit bag and subsequently pay the match fees.
 - The home team coach can also communicate with the referee through the app so that the messages are associated with the match
 - Referees are able to update their travel expenses, if they have any.
 - The Referee can also communicate with the home team coach with respect to a particular match/fixture.
 - Admin Users can add, edit and delete Clubs, Teams and Matches, as well as act as a proxy for the user and perform the tasks of either coach or ref.
 
> **The ultimate intention is to provide a more hollistic and cashless solution for matchday payments and communication.**

#### **Scope**
This app is intended to address **two** key needs not currently solved by existing commercial apps, namely:
- **Paying Match Officials match fees electronically.**
- **In app communication with the ref; with messages linked and viewed by individual match.** 

The scope could easily extend to try and include sophisticated league and match creation algorithms, or seek to track and display results. This app is intended as a MVP; a concept of what could be provided to address the above needs in the time available to complete the project. The additional features could certainly be developed and added in the future, which could eventually produce a single hollistic app for all league, match, payment and communication needs.

I have grouped the key features required for this app to function as intended into their associated CRUD category for thoroughess:
 - **Create** Competitions, Clubs, Teams and Matches by specific age group and allow match officials to add travel expenses into the fixture information. Enable Coaches and Referees to communicate with each other by adding in app messages.
Let coaches pay for their match fees and add an order to the database.
 - **Read**, or view all of the Clubs, Teams or Matches stored in the database.
    - Display all relevant match detail in one convenient dashboard.
    - Filter those matches by age group, or Team name.
    - Search for a team and display that teams games.
 - **Update** Enable Admin users to edit and update Clubs, Teams and Matches as required, and also allow the Match Officials to update their travel expenses.
 - **Delete** function for Site Admins, who can remove Clubs, Teams and fixtures as required.

The final but most critical part of this app is the requirement for site security, which serves three purpooses:
1. Mimic existing commercial app security
It may come as a surprise but existing app's provided by Regional FA's have tight security, limiting access to key features to registered club and match officials.
> This app is intentionally not designed for the anonymous user.
2. Provide security for the e-commerce platform so users feel their transactions are secure (User Story #18)
3. Prevent unwanted and unauthorised editing or deletions of records, 

##### Functional Requirements
App functionality is provided through a typical intuitive, mobile responsive navbar. The navbar menu options increases once a user registers or logs into the website, increasing what they can view and achieve.
Each match on the Fixtures page is a link to that matches dashboard.
Additional interactive anchor links are provided throughout to provide users with multiple ways of navigating around the app to achieve tasks or navigate back to where they had come from.

##### Content Requirements
Much of the content in this app revolves around the Matches Model, which contains lists of Venues, Clubs, Teams, Match Officials and Games I have uploaded through fixture files. Additional data has subsequently been added using the app's CRUD functionality. Club and Team information has come from the [Cheltenham Youth Football League](https://www.cheltenhamyouthleague.co.uk/) website. The images used have been taken from Pixabay, while other graphics were copied from the nounproject website.

I have attempted to maintain a consistant design and theme for each of the apps pages and have deliberately included just enough content for this app to function as defined in the Scope, and no more. This has been a conscious decision to prevent unnecessary scope creep.
 
___

#### **Structure**  
The structure of RefereE-Pay is consistent irrespective of user, however functionality is compartmentalised with user roles dictating what each group can achieve:
  - **Anonymous Users** can view the Fixture list, Clubs and Teams only. They do not have access to the match details, nor can they access the payment system.
  - **Registered Users** have the same functionality as anonymous users with the addition of being able to view match details, but they cannot communicate with match officials access the kit bag or complete any transactions.
  - **Registered Coaches** are able to view the Fixtures, Clubs and Teams as well as the individual Match Details. They have the ability to add their team's HOME games to the kit bag and to complete payments. Home team coaches are also able to add messages to the fixture to communicate with the Match Official.
  - **Match Officials** - have the same viewing capabilities as Coaches but obviously cannot pay any match fees. They can add their travel expenses and send in-app messages to the Home team Coach.
  - **SuperUsers** - have full and unrestricted access to all functionality, and can if required act as a proxy for a Coach or Match Official. Superusers also have tha ability to Create, edit and Delete Clubs, Matches and Teams. Crucially they are the ones who assign the **full name**, the **role** and where applicable the **team** to registered users to allow them to act as Coach or Referee.

The workflow for RefereE-Pay is quite complex, but I have attempted to capture it below:
![Workflow](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/referee-pay-flow.jpg "Website workflow")

##### **Interaction Design**
User interaction with the RefereE-Pay website falls into a number categories:

 - **Navigation**
Navigating between the 19 distinct pages is achieved through a conventional mobile responsive navbar placed at the very top of each page. 

![Main Navbar](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/navbar.jpg) 

Additionally, and where appropriate in page links have been provided to assist users navigate back to previous pages or to redirect them to another page where they are able further interact with the site.

![In page navigation](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/inpage-nav.png)

 - **Manipulation**
Pages rendering large amount of data have been paginated for convenience and navigation through this data is achieved through the standard Bootstrap Pagination controls.

    ![Pagination](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/pagination.jpg)

    Data can also be manipulated via the Filter and search function provided.

    ![Data Filters](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/filters.jpg)

 - **Data Input**
Date is input into the app's Postgres database via a series of Model Forms each linked to it's respective DB model. Form layout is similar across the platorm, and forms are relatively simple and straightforward to use. The structure of the data was designed to enable users to, wherever possible, make choices rather than have to input data manually.
   - New Data can be added by Superusers and Registered users (limited to their Profile)
   
   ![Add Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/add-team.jpg)

   - The existing data can be editted by superusers and registered users (limited to their Profile)
   
   ![Edit Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/teams-super.jpg)


##### **Information Design**
Information is provided to users on a number of key pages; Matches, Match Detail, Match Messages, Clubs, Teams, Kit Bag and Profile. Despite rendering slightly different information the structure of each page has been designed to provide a similar layout and theme. The game summary elements are the key pieces which tie the different pages together.

![Information Design](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/information-design.png)

___

#### **Skeleton** 
RefereE-Pay has been deliberately designed to optimise the placement of elements such as images, buttons  and data. Key elements on each page are located in the same place so users are confident in how they interact with the app

##### **Interface Design**
The intention was to provide an app which maintains a clean, intuitive and consistent interface design, re-using elements and page styles wherever possible to benefit from the users learned behaviour.

###### **Navigation**
Consistenty located at the top of the page, and providing a consistent set of choices, depending on the users role/access rights.

![Navbar](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/navbar.jpg)

- Grand Total
Links users to their Kit Bag while providing a running total of matches in the kitbag (for the duration of the session).

- Search box
Located in the very top right of the navbar and ever present. Allows users to search for a team's matches irrespective of which page they are currently on.

###### **Filters**
Data select dropdowns used to filter the page information are always located towards the top of the page below the Page header.

![](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/skel-filter.jpg)

###### **Pagination**
Pagination controls are located below the filters and also at the bottom of the page below the data, and can be used to navigate the filtered data.

![](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/skel-pag.jpg)

###### **Information**
As is to be expected , information provided by this site takes up the bulk of the center of the pages.

##### **Forms**
Forms are located on the lefthand side of pages on laptop or large monitors. Any additional information provided with that form is located on the right hand side.

![Forms](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/add-travel.png)

###### **In App Navigation**
Navigating back to the Fixtures page or back to a previous page is achieved through buttons consistently located at the base of each page. Button titles should be self explanatory.

![Forms](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/bot-nav.jpg)
 
###### **Messages**
All messages are displayed at the top right of the page just below the search box and are designed to heklp convey the class of message, whether Error, Warning, Info or Success.

![Message Location](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/message-loc.jpg)

###### **Error Pages**
Each error page extends the base template to provide the users with a design consistent with the remainder of the site, and a navbar theu are already familiar with. Thus should a user encounter an unexpected error they are able to easily navigate back to the site without having to use the back button.

![Error Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/404error-page.jpg)

> There should be no requirement for the user to ever have to resort to the Browser BACK button.

##### **Information Design**
The basic concept for the information design for RefereE-Pay is laid out in the following wireframes.

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
I typically find great inspiration for colour schemes on Pinterest. For this project I am looking for very simple bold colurs which enable good contrast. I have used:
 - A green respresenting the grass of playing fields
 - Red for the Red cards wielded by Referees
 - Yellow representing the Yellow cards wielded by Referees
 - A dark blue whicg provides good contract for buttons and text
 - A Lighter blue (Bootstrap info blue) for a few button and my footer text. 
  
![Navbar](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/colour-scheme.jpg) 

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

>**I had considered using a sport themed font for this app, but decided I want to overdo it, and certainly didn't want to detratct from the main purpose of the site.**

##### **Imagery** 
I had a very clear plan for the site images right from the very early planning stages. I wanted to find images showing amateur football in action including the referee or other match officials. I found a decent selection of good quality, licence free images on Pixabay. The full list of images and credits are in the Cedits section.

I also wanted to add some fun to the messages rendered by the app by adding footbal icons matching the level of message, such as:
 - Error = Red Card
 
![Red Card](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/message-error.jpg) )

 - Warning = Yellow Card
 
![Yellow Card](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/message-warning.jpg) )

 - Alert = Tactics Board

![Tactics](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/message-alert.jpg) )

 - Success = Goal

![GOAL!](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/message-success.jpg) )
______

## **Database Schema** <a name="dbschema"></a>  
This app was developed using a SQLite3 database, but was transferred over to a Postgres DB on Deployment.
The database schema below illustrates the relationships between the each of the Models.
![RefereE-Pay Schema](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/referee-pay-db-schema.jpeg "Database Schema")

The schema contains twelve database tables which can be divided into Three categories:
1. User related data used to store individuals data like usernames, passwords, roles etc.
2. Those required to build up the Game details and associated logic like match fees.
3. Those required to process and store the match charges payment transactions.

 - **User**
 Stores user data collected through the AllAuth registration process:
    - Username
    - email
    - password
Additional paramaters like First Name, Last Name and the users Admin/superuser status can be set in the Admin console.

 - **Fee**
    This table stores the Match Officials match fees by age group and role:
    - Age e.g. U10 (Under 10)
    - Referee (referees match fee £)
    - Asst_referee (assistant referees match fee £)
    - Milage rate (agreed value  per mile travelled in excess of 10 miles)
    >I have included the milage rate for travel expenses in the event I change the logic, in future versions, to calculate the travel expenses by distance travellled rather than allowing match officials to input their expenses.

 - **Venue**
    The Venuw table stores the pitch location details, can be rendered to provide pitch location information to website users, who are Team Coaches, Match Officials or potentially supporters :
    - Name (Playing field name)
    - Short name (Convenient short name if required)
    - Street Address
    - Town or City
    - County
    - Postcode
    - Country
    - Map (Map showing park layout with actual pitch locations)
    - Map_url (Link to Google maps)

 - **Official**
    This is a simple table storing the name of each match officials

 - **Competition**
    Another simple table to store the name of each competition. Enables games to be grouped into distinct competitions by ability for instance.

 - **Club**
    Stores a limited set of Club information, sufficient for proof of concept:
    - Club Name
    - Club Badge url
    - Club Badge (Image file upload)
    - Website url (Club website url)
    > Arguably this could be expanded in the future to include details such as address, contact numbers and email address.

 - **Team**
    The Team table stores the basic critical information for each Team:
    - Team Name
    - Short Name (Convenient short name if required for smaller displays)
    - Club Name contains a Foreign Key back to the "Clubs" table, associates each team to a Parent Club.
    - Age contains a Foreign Key back to the Fees table and categorises each team into a particular age group. Ensures teams of similar age can be selected to play each other.
    - Manager/Coach lists the Teams Manager or Coach contains a loose logical link back to the Users Table

 - **Game**
    This table is where much of the previous tables data is joined:
    - Age - contains a Foreign Key back to the Fees table, enables each game to be categorised by age.
    - Competition - contains a Foreign Key to the Competitions Table and allows each game to be grouped by it's competition.
    - Home Team - Foreign Key to the Teams Table and sets the Home team for a game.
    - Away Team - Foreign Key to the Teams Table and sets the Away team for a game.
    - Date_Time - A datetime field which is associated with each Games kick off date and time.
    Also important for calculating match fines (nonpayment fines), and limits when Match Officials can upload travel expenses, and when Coaches or Refs can communicate with each other.
    - Venue - has a Foreign Key back to the Venue table so each game can be assigned a playing field/pitch
    - Referee field - a Foreign Key back to the Match Officials table, enabling the assignment of a match referee
    - Asst_Referee1 - a Foreign Key back to the Match Officials table, enabling the assignment of a match assistant referee. All Match officials are essentially qualified referees so there is no additional complexity of assigning specific roles to each match official.
    - Asst_Referee2 - a Foreign Key back to the Match Officials table, enabling the assignment of a match assistant referee. All Match officials are essentially qualified referees so there is no additional complexity of assigning specific roles to each match official.
    - Ref_trav - added to store the input from Match Officials as and when they update any travel expenses
    - Asst1_trav - added to store the input from Match Officials as and when they update any travel expenses
    - Asst2_trav - added to store the input from Match Officials as and when they update any travel expenses
    - Ref_total - display the total fee for the referee combining match fee with any travel expenses
    - Asst1_total - display the total fee for the assistant referee (if assigned) combining match fee with any travel expenses
    - Asst2_total - display the total fee for the assistant referee (if assigned) combining match fee with any travel expenses

 - **Chat**
 Stores messages associated with an associated game, so the messages can be rendered by game and by authors role. This table is critical to allow in app communication between coach and ref.
    - Match - is a Foreign Key back to the game_id, and allows storage of messages by game
    - Author - a Foreign Key back to the User Table identifies the author of the message
    - Body - The content of the message
    - Image - Coaches and Refs are thus able to upload and save match related images, like the condition of the pitch, goals etc.
    - date - a date time field with auto_now_add set to True, and provides a means to order the messages by, so they are displayed chronologically
    - 
 - **User Profile**
    Primarily used to store Billing address information and a their role if applicable. Used to prefill the payment details for any subsequent orders.
    - User - a one to one relationship back to the All Auth Users table.
    - Role - Stores a users role e.g. Coach, Match Official or Admin. Is used to set permissions for certain functions by role. For example any superusers and match officials can add Travel expenses, and only Coaches and Superusers can add a match to the kit bag for payment.
    - Profile_phone_number - stores the users phone number to the Billing information if they choose the save info option on the form field
    - Profile_street_address1 - stores the first line of the users street address to the Billing information if they choose the save info option on the form field
    - Profile_street_address2 - stores the second line of the users street address to the Billing information if they choose the save info option on the form field
    - Profile_town_or_city - stores the users town or city of residence to the Billing information if they choose the save info option on the form field
    - Profile_county - stores the users county/state to the Billing information if they choose the save info option on the form field
    - Profile_postcode - stores the users postal code (if applicable) to the Billing information if they choose the save info option on the form field
    - Profile_country - stores the users country of residence to the Billing information if they choose the save info option on the form field

 - **Order**
    Stores all of the information critical to processing a payment.
    - Order_number - Stores the unique alphanumeric number generates for each transaction
    - User_profile - a Foreign Key back to the Users UserProfile table
    - Full_name - Records the users full name
    - Email -  Records the users email address
    - Phone_number -  Records the users phone number
    - Street_address1 -  Records the first line of the users street address
    - Street_address2 -  Records the second line of the users street address
    - Town_or_city -  Records the users town or city of residence
    - County_or_state -  Records the users county or state
    - Postcode -  Records the users potal code
    - Country -  Records the users country of residence
    - Date - Stores the date of the transaction if successfully processed by Stripe
    - Grand_total - Records and saves the Grand total of all matches in the kit bag
    - Original_bag - Stores the id of games that have been successfully paid for. This is used to identify matches that have already been poaid for and to marck them as paid and remove the "Add to Bag" functionality.
    - Stripe_pid - Records and saves the stripe pid for the transaction
 
 - **Order Lineitem**
    - Order - is a Foreign key back to the Order_id in the Order Table.
    - Match - a Foreign Key back to the Game_id of the Game table, associates the lineitems with a specific game
    - Payment_due_date - a datetime filed used to calculate whether a nonpayment/match fine is applicable. This is set to 24hrs after kick-off date and time. Gives the Coach 24hrs to pay the necessary fees or incur an automatic fine.
    - Match Fines - Stores the nonpayment fine as an item. This is important to render in the kit bag so Coaches have a full breakdown of the charges they are paying for in each Match.
    - Lineitem_total - Represents the total for each match and is a sumation of, officials fees, travel expenses and fines.

___
## **Features** <a name="features"></a>
The following table lists the primary features provided by the W3Recipes app.

### **Existing Features**

 1. A **[Landing Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/home-page.jpg)** to convey the purpose of the website to new and returning users.
 
 2. A **[Footer](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/footer.jpg)** is visible on each page and contains some basic information for UK & Ireland FA's and the developers contact info.
   a. Each **FA Icon** for each of the UK and Irish Football Associations contains a link to their respective websites.
   b. A link to the developers **GitHub Repo**
   c. A link to the developers **LinkedIn Profile**
   d. An **Email link** to quickly contact the deleoper

 3. A Mobile Responsive **[Navbar](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/navbar.jpg)** tops each page and provides conditional menues based on a users role.
   a. The **[Referees Navbar](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/ref-nav.jpg)** doesn't require the Grand Total or access to Kitbag and Checkout so has limited options suitable for Referee users.
   b. The **[Coaches Navbar](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/my-account.jpg)** provides much of the functionality they need in one place. The my account select menu provides access to the bit bag and checkout. The Grand Total also contains a link to the Kit Bag.
   c. The superusers **[Admin Navbar](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/admin.jpg)** is very similar to that for Coaches other than they have the additional Admin select menu.

 4. A Paginated **[Fixtures](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/matches.jpg)** page where all matches are displayed.
   a.**[Age & Team filter ](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/filters.jpg)** functions, filters matches by age or team, or both.
   b.**[Match Text Search](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/navbar.jpg)** function located in the main navbar enables users to narrow down the results to a single team.
   c. **[Pagination Controls](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/pagination.jpg)** at the top and bottom of the page to aid navigation.
   d. **[Back to Top](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/btt-button.jpg)** button to return users to the top of the page without having to scroll all the way back.

 5. The**[Match Detail Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/match-detail-1.jpg)** page provides a dashboard of all match details with interactive elements.
   a. The **[Edit Match](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/edit-match-btn.jpg)** button which is exclusive to superusers takes them to the Edit Match page.
   b. The **[Edit Match page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/edit-match.jpg)** provides the functionality to edit and update all of the match detail in one place.
   c. The **[Home and Away Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/cond-select.jp)** choices function as conditional dropdown mewnus linked to the age selection field
   d. The **[Delete Match](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/edit-match-btn.jpg)** button initiates the Match deletion process by opening a delete confirmation modal.
   e. The **[Delete Confirmation](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/match-conf.jpg)** modal warns the superuser they are about to delete a particular Match and checks that is the intention.
   f. Interactive **[Match Venue](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/match-detail-2.jpg)** accordion renders a map of the venue, or provides a link to Google Maps if no map exists.
   g. Interactive **[Match Fees](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/match-detail-3.jpg)** accordion, opens up to display Match Officials and their fees and any travel expenses
   h. **[Add to Bag](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/add-bag.jpg)** button is exclusive to coaches and superusers and enables Home team coaches to add their matches to the kit bag for payment.
   i. **[Add to Bag - Success](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/bag-cuccess.jpg)** A notification is displayed when the user clicks the "Add to Bag" button on the match detail page. This notification will display a summary of all matches in the kitbag for the duration of the users session but gets cleared if the user logs out.
   j. **[Add Travel](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/add-travel.png)** button is exclusive to referees and superusers, to enable them to add their match day travel expenses.
   k. **[PAID Stamp](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/paid.jpg)** is rendered once a match has been paid for and replaces the "Add to Bag" and "Add Travel" buttons.
   l. **[Messages](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/messages-btn.jpg)** button which takes users to the Match Messages Page. Displays the current number of messages if greater than 0.

 6. **[Match Messages](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/match-messages.jpg)** page displays a summary of the game and also any messages posted by either Home team Coach of Match Referee.
   a. Each of the **[Messages](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/messages.jpg)** is coloured according to user role (ref or coach) and tagged with that users name. Images uploaded also display below the message.

 7. **[Add Message](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/add-msg-btn.jpg)** button takes authorised users to the Add Message page.
 
 8. **[Add Message](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/add-message.jpg)** page displays and allows authorised usres to post a new message for a particular match. Images can also be uploaded using the same form.
 
 9. **[Club Directory](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/club-directory.jpg)** page displays a paginated list of the Clubs stored in tha database. Superusers can edit and delete Clubs from this view.
   a. **Club Badge** acts as a link to the Club's website.
   b. ** [View Teams](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/club-teams.jpg)** takes users to the Teams directory for that particular Club.
   c. **[Edit Club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/club-super.jpg)** button is available only to Superusers, and takes them to the "Edit Club page"
   d. The **[Edit Club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/edit-club.jpg)** page enables Admin users to edit the club name, club badge and the clubs website url. 
   e. **[Delete Club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/club-super.jpg)** button initiates the Club deletion process by opening a delete confirmation modal.
   f. **[Delete Confirmation](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/del-conf.jpg)** modal warns the superuser they are about to delete a particular Club and checks that is the intention.

 10. **[Teams Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/teams.jpg)** displays basic information for all teams associated with a particular Club. Superusers can edit and delete Teams from this view.
   a. **[Team - Age Filter](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/team-filter.jpg)** allows users to filter the clubs teams by age group. Handy if the Club has a long list of teams.   
   b. **[Edit Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/teams-super.jpg)** function takes Superusers to the Edit Teams page.
   c. Team details can be changed through the functionality of the **[Edit Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/edit_team.jpg)** page. This page initially populates with the existing information and is where Admin users can change the Team name, age club and manager.
   d. **[Delete Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/teams-super.jpg)** button initiates the Club deletion process by opening a delete confirmation modal.
   e. **[Delete Confirmation](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/del-team.jpg)** modal warns the superuser they are about to delete a particular Team and checks that is the intention.

 11. The **[Kit Bag](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/kit-bag.jpg)** page displays a summary of all of the active user's matches they have added to the kit bag and summarises the fees.
   a. The kitbag displays a **[Fees Summary](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/fee-summary.jpg)** section for each game so the active user can see the breakdown of fees, and understand what they are paying for.
   b. A **[Remove from Bag](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/bag-remove.jpg)** icon sits on the middle right of the maych name, and enables the user to remove that match from their kit bag.
   c. The **[Secure Checkout]()** button takes the active user to the "Checkout" page where they have the ability to pay for their match fees.

 12. The **[Checkout Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/checkout.jpg)** proceses the payments of any matches in the kitbag.
   a. The Checkout page has a **[Fees Summary](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/checkout-summary.jpg)** section on the top right with a basic breakdown of fees.
   b. The bulk of the page is taken up by the **[Billing Details](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/billing.jpg)** form, where users enter their billing address.
   c. Users can select to have their information saved automatically by selecting the **[Save info](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/billing.jpg)** checkbox below the billing information form.
   d. The **[Card Details](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/card-secure.jpg)** window is a Stripe element connected to the Stipe payments API and allows users to enter their card details.
   e. The **[Secure Checkout](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/card-secure.jpg)** button completes the payment process, sends the information to Stripe and generates an order.
 
 13. A **[Checkout Success](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/checkout-success.jpg)** page to confirm successful processing of the match fees transactionappears on successful payment.
   a. A **Success message** appears as the Checkout Success page loads
   b. Users receive an **[Email Notification](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/success-email.jpg)** of the success of their payment. The email confirm order # payment date and Grand Total

 14. Each registered user has a personalised **[Profile Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/profile.jpg)** displaying the users role and team if appropriate as well as billing information, if saved, and a summary of any payments processed for that user. Profile information can also be updated from this page.
   a. Each order in the **[Order Summary]()** contains a link to the confirmation page summary for that order.

 15. Superusers are provided with a unique navbar **[Admin Menu](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/features/admin.jpg)** which enables them to Access the Admin functions of the app.
   a. **[Add Competition](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/add-comp.jpg)** form allows Admin/Superusers to add new competitions to the list.
   b. The **[Add Club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/add-club.jpg)** view allows Admin/Superusers to add new Clubs to the directory, populating club badge and club website.
   c. **[Add Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/add-team.jpg)** allows Admin/Superusers to add new teams to the selected Club and assign the Manager/Coach.
   d. The **[Add Match](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/add-match.jpg)** page allows Admin/Superusers to add new matches to the app, populating all of the information required to renderf the details.

 16.  A football inspired **[Success Notification]()** messages appears through out the site whenever a positive outcome is achieved.
 17.  The is also a football themed **[Warning Notificatio]()** message used when appropriate.
 18.  All of the site's **[Error Notification]()** messages are suitably football inspired and appear whenever something doesn't function or if the user attempts something they don't have permission for.
 19.  To complete the set, each information **[Alert Notification]()** is also football themed.
 20.  | A football themed **[Loading screen]()** is used while the match payments are being processed by Stripe.
 
_____

### **Security Features**
Despite not being explicitly required for this build I have chosen to implement certain security features to provide some protection against unauthorised access to other users data.

 1. User Login
 2. 2. An AllAuth powered **[Sign-up Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/sign-up.jpg)** for new users to sign-up.
 3. An AllAuth powered **[Log-in Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/sign-in.jpg)** for returning registered users.
|  033  | **Logout Screen** |  | []() |



### **Features Left to implement**
I have attempted to provide as much initial functionality in this app' as I can in the time available. Despite this there are features I would still like to incorporate in the future:
|   Feature     |     Description      |
|---------------|----------------------|
| Conditional dropdown on fixtures | To reduce the number options in the teams filter box by conditionally filtering the options by age. |
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

- ![Django](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/django.png "Django") - The project uses the Django framework
- ![Bootstrap CSS](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/Bootstrap-logo.png "Bootstrap 4") - Bootstrap 4.6
- ![Font Awesome](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/fontawesome-logo.png "Font Awesome") - Font Awesome was the source of all icons.
- ![Google Fonts](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/googlefonts-logo.png "Google Fonts") - Fonts used on the website courtesy of Google Fonts
- ![JQuery](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/jquery.png "JQuery") - The project uses JQuery to simplify DOM manipulation.


#### Database
- ![SQLite3](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/sqlite.png "SQLit3") - SQLite3  
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
# [TESTING.md](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/TESTING.md) 

______

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

- Migrate the Apps database models to set up the database.
- Dry run the migrations to see if there are any issues. In the Terminal type:
`python3 manage.py makemigrations --dry-run`
- Run the migrations
`python3 manage.py makemigrations`
- You can check the list of queued migrations using:
`python3 manage.py showmigrations`
- Verify the planned migrations using:
`python3 manage.py migrate --plan`
- If all is well migrate
`python3 manage.py migrate`
- A superuser account is required to access the Admin Page of the database, and can be created as follows:
`python3 manage.py createsuperuser`
- Follow the prompts in the Terminal
- Once complete the app can be run using:
`python3 manage.py runserver`

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

#### **Enabling Automatic Deployment**
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
These steps were followed to create a user in the User Group
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

### **Connecting AWS to Django**
The following steps are used to connect Amazon AWS to our Django project.
- Two packages need to be installed to achieve this
  - boto3
  - django-storages
`pip3 install boto3`
`pip3 install django-storages`
-  Add these two packages to our requirements.txt file
`pip3 freeze > requirements.txt`
-  Add storages to the INSTALLED_APPS section of the settings.py file

- To connect S3 to Django some additional we have to tell it which bucket it should be communicating with. This is ONLY required for Heroku so create a new environment variable **"USE_AWS"** in an if statement as follows:

```
if 'USE_AWS' in os.environ:
    
    # AWS Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'ci-ms4-referee-pay'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and Media file storage settings
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URL's in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
- Next, open **Heroku** and navigate to the **CONFIG VARIABLES** (Settings - Reveal Config VARS)
- Add the AWS Keys to the Heroku Config Vars
`AWS_ACCESS_KEY_ID:` `insert your access key`
`AWS_SECRET_ACCESS_KEY:` `insert your secret key` 
- Add the USE_AWS key and set it to True so that the settings file knows to use AWS when deployed to Heroku
`USE_AWS` `True`
- Remove the DISABLE_COLLECTSTATIC key we set up at the beginning of the deployment process
Django should now collect the static files and upload them to our S3 Bucket
- Create a **"custom_storages.py"** file
This will tell Django to use S3 to store our static files in Production whenever someone runs collectstatic.
- Open custom_storages.py file and type the following:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
There is an optional setting which if included in settings.py can help to improve performance. It tells the browser to cach static files foir a long time; this is OK since they don't change very often.
- In settings.py above the AWS Bucket Config settings add:
```
# Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000'
    }
```
- **Commit these changes and Push them to GitHub**
This will trigger an automatic deployment to Heroku
- Check the Heroku Build log to verify that STATIC files were transferred
- Open S3 and verify that a /static folder has been created in your Bucket

#### **Adding MEDIA files to AWS**
1. Open S3 and navigate to the Bucket created earlier
2. Click **"Create folder"**
![Media Folder](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/s3-newfolder.jpg "Create a Media Folder")
3. Name it **"media"** and **"Save"**
4. Select this new folder
5. Click the **"Upload"** button
6. Select **"Add Files"** and select all of the images used for your project
7. Click **"Next"** and allow **"Read Access"** under Public permissions
8. Click **"Upload"**
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
- [Pixabay](https://www.pixabay.com/) – Licence free image repository
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
The basic shell of this site follows what was taught during the Full Stack Frameworks - Boutique Ado walkthrough project provided by Code Institute. However the premise and design of the remained of the RefereE-Pay app is entirely original.

 | Code Snippet | Description | Source |
 |:-------:|-------------|:------:|
 |Football Loader| Bouncing football loader | https://codepen.io/glafontaine/pen/geMYaJ |
 | Chained Selects | Chained / dependent dropdown lists/select elements | https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html |
 | Stripe integration | Code Institute Boutique Ado walkthrough project | - |


### **Acknowledgements** <a name="acknowledgements"></a>

 - Thanks as always to everyone at the Code Institute for the excellent video tutorials and fantastic introduction to Django and Automated testing in Python and some of the different databases structures. Chris Zielinski's Walkthrough projects were extremely helpful and enjoyable.
 - Grateful thanks to Tutor support who were on hand when most needed to provide assistance.
 - My mentor Precious Ijege for his support and advice throughout this final project. Thank you also for providing such a thorough review of the finished project helping ensure it was fit for submission.
 - My appreciation to all the users who took time to test the web app:
______
### **Technical Support** <a name="technical"></a>
If you encounter any issues with this website, or require any support please email the developer [johnge71@gmail.com](mailto:johnge71@gmail.com)