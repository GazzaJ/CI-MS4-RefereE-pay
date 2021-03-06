![RefereE-Pay](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/readme-title.jpg "RefereE-Pay")
# [**Testing & Bug Descriptions**](https://ci-ms4-referee-pay.herokuapp.com/)
This document records all of the automated and manual testing conducted on the RefereE-Pay app, and also lists the bugs and fixes recorded during the development of the app'.
The philosophy I have used throughout this build is to code, review and test each part of the website as I progressed, relying heavily on Google Dev tools throughout, for first pass testing.
______
## Table of contents
1. [Login Credentials](#login)
2. [User Story Testing](#user-story-testing)
3. [Functionality Testing](#functionality)
   - [Navigation Testing](#first-navigation)
   - [Registration / Log-in](#registration)
   - [Matches & Match Detail](#matches)
   - [Kit Bag](#kitbag)
   - [Checkout & Checkout Success](#checkout)
   - [Adding New Data](#add-data)
   - [Editing Existing Data](#edit-data)
   - [Deleting Existing Data](#delete-data)
   - [Delete a Recipe](#delete-recipe)
   - [User Profile](#user-profile)
4. [Automated Testing](#automated-testing)
5. [Appearance Testing](#appearance)
5. [Code Quality & Validation](#code-validation)
6. [Usability Testing](#usability)
7. [Responsiveness Testing](#responsiveness)
8. [Performance Testing](#performance)
9. [Security Testing](#security)
10. [Bugs & Issues](#bugs)  

______
## **Login Credentials** <a name="login"></a>

I have pre-loaded a number of user profiles for a selection of Coaches and Referees to facilitate testing of this web-apps features. Some of the web-apps' functionality is dependent on which Role is selected.
| Profile |      Username     |   Password   |    Role   |    Team    |
|:-------:|:-----------------:|:------------:|:---------:|:----------:|
|   001   |      CI_Admin     |   C!_4dm1n   | Superuser |      -     |
|   002   |  Richard_Spencer  |  G)_d3v1l5   |   Coach   | LRFC U12 Devils |
|   003   |    Mark_Hawkins   | WH$dd0n_utd  | Coach | Whaddon United U12 |
|   004   |     Alex_Hunt     |  FC14k3s1d3  | Coach | FC Lakeside U11 Reds |
|   005   | Pierluigi_Collina |  "Y??LC=1r3dc | Referee | - |
|   006   |   Damir_Skomina   | D4m1r5k0m1n4 | Referee | - |
|   007   |   Bjorn_Kuipers   | BJ0rnku1p3r5 | Referee | - |
|   008   |    Felix_Blych    | F??l1x8lych | Referee | - |
> It may be necessary to change a Coaches email address during testing in order to receive a payment confirmation email.
______

### **User Story Testing** <a name="user-story-testing"></a>
The following testing has been carried out to validate how the website addresses each of the user stories:

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 01 |_As a_ **site user**, _I need to_ **easily register for an account**, _in order to_ **have a personal account and be able to view my profile**| There is the clear and obvious link on the home page, which redirects the user to the registration page. This link correctly opens the registration page to begin the registration process | **PASS** | 

![Home Sign-up](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-1.png)


|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 02 |_As a_ **site user**, _I need_ **easily log-in and log-out of the site**, _in order to_ **access the match details and my personal information**| There are two ways to log into RefereE-Pay. The first is the clear and obvious link on the home page. There is also an additional link in the Navbar under the "My Account" tab. | **PASS** |

![Home Page Log-in](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-2.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 03 |_As a_ **site user**, _I need to_ **easily recover or rested my password in case I forget it** _in order to_ **recover access to my account**| A "Forgot Password" link exists on the log-in page which redirects the user to the Reset password page | **PASS** |

![Password Reset](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-3.png)



|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 04 |_As a _ **site user**, _I need to_ **receive an email confirming registration**, _in order to_ **verify that my account creation was successful**|During the registration process users are sent an email from the app to confirm their email address. On confirmation they are taken back to the site and a success messages is displayed | **PASS** |

![Registration confirmation](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-4.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 05 |_As a _ **site user**, _I need to_ **have a personalised user profile**, _in order to_ **View my personal payment history and payment confirmations, and save my payment information**.| A profile page exists under the "My Account" tab. This page displays the users billing details **if saved** and also displays a list of any payments the user has made.| **PASS** |    

![User Profile](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-5.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 06 | _As a _ **Team Manager**, _I need to_ **easily find and view the database of matches**, _in order to_ **understand who I am playing and when**. | Anonymous and Registered users can find all of the games in the database on the fixtures page | **PASS** | 

![Matches Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-6.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 07 | _As a _ **Team Manager**, _I need to_ **sort all fixtures by age**, _in order to_ **easily identify all fixtures in an age group**. | Anonymous users and Registered users can use the Age dropdown menu to select an age group to filter the match list by | **PASS** | 

![Sort by Age](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-7.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 08 | _As a _ **Team Manager**, _I need to_ **sort fixtures by team**, _in order to_ **View my personal payment history and payment confirmations, and save my payment information**. | Anonymous users and Registered users can use the Team dropdown menu to select a Team name to filter the match list by | **PASS** | 

![Sort by Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-8.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 09 | _As a _ **Team Manager**, _I need to_ **be able to quickly navigate through the list of fixtures**, _in order to_ **find different fixtures**. | The matches list is displayed over several pages navigated via the pagination controls. There is also a back to top button to take the user from the bottom of a page back to the top | **PASS** | 

![Paginated Matches Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-9.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 10 | _As a _ **Team Manager**, _I need to_ **search for fixtures by team name**, _in order to_ **find a specific fixture I'd like to pay the match official fees for**. | The search box located in the navbar facilitates easy searching of teams by name. | **PASS** | 

![Search by Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-10.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 11 | _As a _ **Team Manager**, _I need to_ **communicate with the Referee**, _in order to_ **confirm match status and alert them of any issues with the condition of the pitch**. | The matches - messages page provides a simple method for the Home team manager and coach to communicate with each other. Messages are stored and displayed per match and a simple add message form facilitates message creation | **PASS** |

![Messages App](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-11.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 12 | _As a _ **Team Manager**, _I need to_ **post/send pictures to the Referee**, _in order to_ **illustrate the condition of the pitch ahead of any match**. | Images can be uploaded and stored with the message for each match. A simple Add message form facilitates image upload | **PASS** | 
 
![Add Image](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-12.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 13 | _As a _ **Referee**, _I need to_ **communicate with the Home team manager**, _in order to_ **reply to any issues or concerns raised ahead of the game**. | The matches - messages page provides a simple method for the Home team manager and coach to communicate with each other. Messages are stored and displayed per match and a simple add message form facilitates message creation | **PASS** |

![Messages App](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-13.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 14 | _As a _ **Team Manager**, _I need to_ **easily select a fixture**, _in order to_ **discover the full details of that match**. | Clicking on any one of the fixtures opens up the full fixture detail. From here the user can discover the venue , date and time of KO, match officials and their fees. Several other links are provided to return users to the fixtures page  | **PASS** |

![Select and View Fixture](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-14.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 15 | _As a _ **Team Manager**, _I need to_ **have a simple and quick payment method**, _in order to_ **pay the assigned match officials their match fees**. | The checkout process is completed in 3 easy steps. Matches can be added to the kit bag from the Match detail page. A confirmation pop-up appears showing the match has been added. users can click the bag icon or the "Secure Checkout" link on the popup to view the bag contents. Clicking "Secure Checkout" from the bag redirects the user to the Checkout page where they complete their details (if not saved) and add their card details. | **PASS** |

![Payment Process](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-15.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 16 | _As a _ **Team Manager**, _I need to_ **view any pending payments in my kit bag**, _in order to_ **identify the total cost of match fees for each game and the grand total**. | The shopping bag or "Kit bag" displays all matches that the user has selected for payment. These matches will be stored in the session memory for as long as the user is logged in. | **PASS** |

![Kit Bag](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-16.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 17 | _As a _ **Team Manager**, _I need to_ **easily enter my payment information**, _in order to_ **complete my payment quickly and efficiently**. | There is a very simple and intuitive payment form which takes literally seconds to complete. | **PASS** |

![Payments](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-17.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 18 | _As a _ **Team Manager**, _I need to_ **feel my personal and payment information is secure and safe**, _in order to_ **feel confident in providing required information to complete a payment**. | Payment process is provided and managed through the Stripe Payments API. Stripe is the favoured e-commerce payment platform for many household names. | **PASS** |

![Stripe](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/stripe.jpg)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 19 | _As a _ **Team Manager**, _I need to_ **view a payment confirmation after checkout**, _in order to_ **verify that I have successfully paid my match fees**. | Following successful payment processing the user is redirected to a Payment Success page which displays their order #, billing details and a summary of their payments | **Pass** |

![Payment Confirmation](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-19.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 20 | _As a _ **Team Manager**, _I need to_ **receive an email confirmation after checkout**, _in order to_ **have recorded confirmation of each payment**. |  | **FAIL** |

![Payment confirmation email](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-20.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 21 | _As a _ **Site Admin**, _I need to_ **add, edit and delete Matches**, _in order to_ **keep pace with league fixtures and provide a long term solution**. | Separate views exist to create a new match, edit and existing match and delete an existing match from the database. A Delete confirmation modal has been provided to ensure a level of security before the match is irreversibly deleted | **PASS** |

![Matches CRUD](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-21.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 22 | _As a _ **Site Admin**, _I need to_ **add, edit and delete Clubs**, _in order to_ **keep track of league clubs and those using the site**. | Separate views exist to create a new Club, edit and existing Club and delete an existing Club from the database. A Delete confirmation modal has been provided to ensure a level of security before the Club is irreversibly deleted | **PASS** |

![Clubs CRUD](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-22.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 23 | _As a _ **Site Admin**, _I need to_ **add, edit and delete Teams**, _in order to_ **keep track of all clubs teams**. | Separate views exist to create a new Team, edit and existing Team and delete an existing Team from the database. A Delete confirmation modal has been provided to ensure a level of security before the Team is irreversibly deleted | **PASS** |

![Teams CRUD](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-23.png)

|User Story|Description|Testing| Result |
|:--------:|-----------|-------|--------|
| 24 | _As a _ **Referee**, _I need to_ **add my travel expenses**, _in order to_ **ensure I get paid the full amount for my services**. | Match Officials are able to add their travel expenses to any future, and unpaid match. A link exists on the Match Detail page for them to do this, and is only visibly to match officials and superusers. This takes them to a form where they can update their travel expenses. | **PASS** |

![Match Officials travel fees](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/user-stories/user-story-24.png)

______

### **Functionality Testing** <a name="functionality"></a>
The following tables capture the functional testing performed on the web-app to ensure it works as desired. I have tested on the listed browsers only, using Windows version 1909 (OS Build 18363.1556), and have not conducted any backward compatibility testing in older browser versions.  

#### **First Time Navigation Testing** <a name="first-navigation"></a>
Tests the initial navbar selections _( Home | Fixtures | Clubs | My Account )_ for anonymous users, and various anchor links provided to assist users navigating between pages.

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Sign-up Link** on Homepage |Take users to the registration page | Opens Sign up/registration page | **PASS** | **PASS** |
|   002  | **Sign-in Link** on Homepage |Take users to the to Log-in page| Redirects users to the login page as expected | **PASS**  | **PASS** |
|   003  | **Navbar - My account** login link | Correctly redirects users to the login page | Log-in Link under "My Account in the Navbar" opens log-in page as expected | **PASS** | **PASS** |
|   004  | **Fixtures** navbar link | Opens up the fixture list | Correctly navigates to the fixtures page | **PASS** | **PASS** |
|   005  | **Age Dropdown**  | Should filter the list of matches by the teams age group when filter is clicked | The age dropdown correctly filters the matches by age group; provided games of that age group exist | **PASS** | **PASS** |
|   006  | **Team Dropdown** | This should filter the list of matches by the team selected when the filter button is clicked | Correctly filters the list of games by the selected team | **PASS** | **PASS** |
|  007   | **Reset Button** | Reset the list of matches to display all fixtures | Correctly resets the list | **PASS** | **PASS** |
|   008  | **Clubs** navbar link | Redirects users to the club directory Page | Selecting the link takes users to Club directory page | **PASS** | **PASS** |
|   009  | **Search Box** on homepage |Redirects users to the Fixtures page with a list of games filtered by the team. Else displays warning message. | Correctly filters the fixture list if the team exists in the DB else displays toast message  | **PASS**  | **PASS** |

![No Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/no-team.jpg)

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   010  | **App logo** |Redirects users to the homepage | Correctly takes users to the homepage as desired | **PASS** | **PASS** |
|   011  | **Selecting a fixture** from the fixture list | Redirect un-authorised and un-logged in users to the login page | Redirects as expected | **PASS** | **PASS** |
|   012  | Selecting the **"View the Teams"** link in the Club Directory | Redirects users to the Team directory for the Club the selected | Correctly takes users to the team directory for the club they selected | **PASS** | **PASS** |
|   013  | **Back to Clubs** link | Redirects users back to the Club directory from team they had selected | Users are taken back to the Club Directory page as expected | **PASS** | **PASS** |

___

#### **Registration/Log-in Testing** <a name="registration"></a>
This section covers some basic testing of the Registration Log-in functionality. Account authorisation is provided by the AllAuth package and will have been independently validated. My intention is to simply ensure that I have not introduced any unwanted issues while customising the templates. 

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Sign-up Link** | Should direct users to the Registration form  | The Sign-up link works as desired | **PASS** | **PASS** |
|   002  | **Email Reuse** | Should prevent the re-use of an email by more than one user | Form does not submit and error message displayed as desired | **PASS** | **PASS** |
|   003  | **Username reuse** | Should prevent the re-use of an username by more than one user | Form does not submit and error message displayed as desired | **PASS** | **PASS** |
|   004    | **Email Validation Email** | App should send email to users email address with instructions to validate email address | The email validation message is sent | **PASS** | **PASS** |
|   005    |  **Custom Validation email** | The content of the email is specific to RefereE-Pay and the user | The email refers to RefereE-Pay and mentions the Users Username | **PASS** | **PASS** | 
|   006    | **Registration Success** | Successful registration is confirmed with a message on the website | On successful signup users are directed to the Log-in page and a success message is displayed | **PASS** | **PASS** |
|   007    | **Use of Correct Templates and Styles**  | The pages should use the RefereE-Pay background images and styles | The webpage styles are correct for the application | **PASS** | **PASS** |
|   008    | **Navbar Functionality**  | Maintain navbar functionality throughout the process | The navbar remains functional throughout this process | **PASS** | **PASS** |

![Account Sign-up](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/account-signup.png)

____

#### **Matches & Match Detail (Searching and Viewing)** <a name="matches"></a>
This section documents the testing performed to validate the ability of the user to search for and view the match list, filtering it by age and team, as well as viewing individual games. This testing is aimed at the functionality for logged in Coaches and Referees

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|  001   | **Navigate to matches**| Clicking the fixtures tab redirects users to the match list | Users are redirected correctly | **PASS** | **PASS**|
|  002   |  **Matches listed in date order**  | Matches should be listed in Chronological order | The matches are listed in the correct order | **PASS** | **PASS** |
|  003   |  **Age Filter**  | Reduces the match list to games for a specific age group | Match list is correctly filtered and remain in chronological order | **PASS** | **PASS** |
|  004   | **Team Filter**  | Reduces the match list to display only the games where the selected team features, as either the home or the away team | The match list is correctly filtered by Team name and remains in chronological order | **PASS** | **PASS** |
|  005   | **Search Box filter** | Functions like the Team filter, reducing the match list to those games featuring the searched team else a warning message displayed | The match list is correctly filtered by Team name and remains in chronological order | **PASS** | **PASS** |
|  006   | **Match Select** | Selecting one of the games opens the full match detail for that fixture | Match detail appears as desired | **PASS** | **PASS** |
|  007   | **Match Detail** | Provides sufficient information without further interaction (Teams, Venue, Times, Match Officials) | All of the critical basic information is displayed as desired | **PASS** | **PASS** |
|  008  | **Match Venue** | Display Date/time and venue address, and the pitch location map (if available) once the "Map for the Venue" button is clicked, else opens up a Google maps window displaying pitch location | Match location and time details display correctly, Accordion feature works as desired. Link to Google maps works as desired | **PASS** | **PASS** |
|  009   | **Match Officials** | displays match officials names, and expands to render match fees when "Review Match Fees" selected | Match officials are displayed correctly and the accordion feature expands to show fees by each official | **PASS** | **PASS** |
|  010   | **Match PAID** | Indicates when a match has been paid for by the Coach | A "PAID" indicator displays once a game has been processed trough the system and exists in the orders database | **PASS** | **PASS** |
|  011   | **Add to Bag** | Available to Coaches and superusers. Adds that match to the kit bag for subsequent payment. | Correctly adds the selected match to the kit bag. Appends it to existing matches if others exist in the kit bag. | **PASS** | **PASS** |
|  012   | **Add to Bag notification** | Toast success displayed confirming match has been added to the kit bag | The Success Toast appears correctly and displays a summary of the match and fees | **PASS** | **PASS** |
|  013   | **Add Travel** | Only available for referees and superusers. Redirects them to the Add travel form | Where applicable the Add travel button takes Referees or superusers to the Add Travel page and form to add travel expenses | **PASS** | **PASS** |
|  014   | **Add Travel** | The Add Travel button should not display after the game date and kick-off time | The button only displays for future matches and doesn't display for historical matches | **PASS** | **PASS** |
|  015   | **Messages Button** | Redirects users to the Match Messages Page | The "Messages" button functions as desired, taking users to the Match Messages page | **PASS** | **PASS** |

____

#### **Kit Bag** <a name="kitbag"></a>
|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Access Kitbag** | Gain access to the kitbag from the Success Toast message by clicking "Secure Checkout" | Users are redirected to the current kitbag when they click the Secure Checkout button on the Success message. | **PASS** | **PASS** |
|   002  | **Access the Kitbag** | Gain access to the kitbag by clicking on the shopping bag icon and grand total in the navbar | Users are redirected to the kitbag when the icon/grand total is selected | **PASS** | **PASS** |
|   003  | **Number of items in Bag** | Display the number of matches currently in the kit bag | The number of matches currently in the kitbag is displayed directly above the list of matches | **PASS** | **PASS** |
|   004  | **Summary of Charges** | The kit bag displays the match and a summary of fees by match Official | The fees for each match are correctly displayed based on the Fees Model in the DB | **PASS** | **PASS** |

![Summary of Charges](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/pages/kit-bag.jpg)
	
|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   005  | **Travel Expenses** | Any travel expenses added to a Match officials fee are rolled into the total for that official |Match officials Total is correctly displayed as Match fees + Travel Expenses | **PASS** | **PASS** |
|   006  | **Match Fines** | A Match fine is added to the match charges if the payment date  = Kick off date/time + 24 hrs | The non-payment fine is calculated and rendered correctly | **PASS** | **PASS** |
|   007  | **Remove Match** | Matches can be easily removed from the kitbag by the user | Each match header has a red and white "X" marked with a Tooltip which indicates "Remove from Bag". Matches are removed from the kitbag when clicked.| **PASS** | **PASS** |

![Remove from Bag](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/remove-from-bag.jpg) 
	
|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   008  | **Update total** | Update the Grant total when games are added or deleted from teh bag | The Grand Total updates as matches are added or removed to the kitbag | **PASS** | **PASS** |
|   009  | **Back to Fixtures** | Redirects users to the Fixtures page | The link takes users back to the Fixtures page as desired | **PASS** | **PASS** |
|   010  | **Secure Checkout** | Directs users to the Checkout page | The link takes the user to the Checkout page | **PASS** | **PASS** |
____
 
#### **Checkout & Checkout Success** <a name="checkout"></a>
|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Summary of Charges** | Checkout page renders a summary of the charges for each game | Checkout Page displays match officials total, Fines and grand total | **PASS** | **PASS** |
|   002  | **Billing Information** | Checkout page has a form where users can populate their billing information |  |
|   003  | **Required Fields** | Indicate to the user which of the Billing Info fields are required | Fields are indicates and a message lets users know to fill in each required field | **PASS** | **PASS** |

![Required Fields](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/checkout-required.jpg)

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   004  | **Save information** | The Checkout page has the option for users to save their billing information | A "save info" checkbox has been provided so users can save their billing information to save them filling it in future | **PASS** | **PASS** |
|   005  | **Card Details** | A secure card details field is provided for the user | An empty, secure Card details field has been provided for users to enter their card details | **PASS** | **PASS** |
|   006  | **No Card Details** | Warn user that card detail have not been entered | The payment will not proceed without card details. If tried a warning message is displayed | **PASS** | **PASS** |

![Save Info](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/card-required.jpg)

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   007  | **Card Charge confirmation** | Indicate to the user how much their card is going to be charged for the match/matches in their kit bag | The Grand Total in the Navbar and a message at the bottom of the page indicates how much the users card will be charged | **PASS** | **PASS** |
|   008  | **Checkout Button** | A button to confirm payment and to proceed with the payment process | A "Complete Payment" button has been provided for users to confirm the payment | **PASS** | **PASS** |
|   009  | **Buffering Loading screen** | Display a buffering/Loading screen while the card payment processes | A Football themed loading screen has been provided | **PASS** | **PASS** |
|   010  | **Checkout Success** | Display the Checkout Success page on successful completion of the payment | The checkout success page is displayed on successful processing of payment | **PASS** | **PASS** |
|   011  | **Success Message** | Display a success message telling the user their payment went through successfully | A message gets displayed when redirected to the Checkout Success page | **PASS** | **PASS** |
|   012  | **Confirmation Email** | The paying user should receive a confirmation email on completion of successful payment | A confirmation email is sent to the email address of the logged in user on successful completion of the payment | **PASS** | **PASS** |
|   013  | **Zero Total** | Ensure the Kitbag contents are cleared and the grand total cleared once the payment process has completed successfully | The total is correctly zeroed on completion of the payment | **PASS** | **PASS** |

____

#### **Adding New Data** <a name="add-data"></a> 
Tests to determine how the Add Competition, Club, Team, Match, Travel and Message pages function.

##### Add Competition 
The Add Competition page enables superusers to add a new Competition to the database. This section validates the functionality of this page.

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Add Competition** | Function only accessible by superusers | Access to the Add Competition Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to add a Competition. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Add Competition link** | Add Competition form displayed | The very simple form displays as desired | **PASS** | **PASS** |
|   004  |**Required Fields** | Required fields are clearly indicated | Required fields are highlighted with an asterix | **PASS** | **PASS** |
|   005  | **Incomplete fields indicated** | Any incomplete, required fields are clearly indicated with a tooltip | Incomplete required fields are indicated | **PASS** | **PASS** |
|   006  | **Add Competition** | Ensure DB updates and users are redirected to the Fixtures page | The Competition gets created and users are redirected as desired | **PASS** | **PASS** |
|   007  | **Success Message** | Display a message when a new Competition has been created | Message displays as desired | **PASS** | **PASS** |
|   008  | **DB Update**s | Ensure the Competition is written to the DB correctly | The Competition name is added to the database as intended | **PASS** | **PASS** |
|   009  | **Cancel Button** | Redirect users to the Fixtures page | Users are taken to the Fixtures page as planned | **PASS** | **PASS** |

![Add Competition](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/add-comp.png)

##### Add Club  
The Add Club page enables superusers to add a new Club to the database. This section validates the functionality of this page.
|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Add Club** | Function only accessible by superusers | Access to the Add Club Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to add a Club. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Add Club link** | Add Club form displayed | The  form displays as desired | **PASS** | **PASS** |
|   004  | **Required Fields** | Required fields are clearly indicated | Required fields are highlighted with an asterix | **PASS** | **PASS** |
|   005  | **Incomplete fields** indicated | Any incomplete, required fields are clearly indicated with a tooltip | Incomplete required fields are indicated | **PASS** | **PASS** |
|   006  | **Image selection** | Ensure the image selection input functions and uploads image file | Upload image functions correctly and the image file is saved to the DB | **PASS** | **PASS** |
|   007  | **Add Club** | Ensure DB updates and users are redirected to the Clubs page | The new Club gets created and users are redirected as desired | **PASS** | **PASS** |
|   008  | **Success Message** | Display a message when a new Club has been created | Message displays as desired | **PASS** | **PASS** |
|   009  | **DB Updates** | Ensure the new Club is written to the DB correctly | The Club name and details name are added to the database as intended | **PASS** | **PASS** |
|   010  | **Cancel Button** | Redirect users to the Clubs page | Users are redirected to the Clubs page as desired | **PASS** | **PASS** |

![Add Club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/add-club.png)

##### Add Team  
The Add Team page enables superusers to add a new Team to the database. This section validates the functionality of this page.

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Add Team** | Function only accessible by superusers | Access to the Add Team Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to add a Team. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Add Team link** | Add Team form displayed | The form displays as desired | **PASS** | **PASS** |
|   004  | **Required Fields** | Required fields are clearly indicated | Required fields are highlighted with an asterix | **PASS** | **PASS** |
|   005  | **Incomplete fields** indicated | Any incomplete, required fields are clearly indicated with a tooltip | Incomplete required fields are indicated | **PASS** | **PASS** |
|   006  | **Club Select** | Ensure the dropdown is populated with the correct clubs | The dropdown functions as desired | **PASS** | **PASS** |
|   007  | **Age Group Select** | Ensure the select element is populated with the various age groups and ages can be selected | The dropdown functions as desired and age groups can be selected | **PASS** | **PASS** |
|   008  | **Add Team** | Ensure DB updates and users are redirected to the Clubs page | The new Team gets created and users are redirected as desired | **PASS** | **PASS** |
|   009  | **Success Message** | Display a message when a new Team has been created | Message displays as desired | **PASS** | **PASS** |
|   010  | **DB Updates** | Ensure the new Team is written to the DB correctly | The Team name and details are added to the database as intended | **PASS** | **PASS** |
|   011  | **Cancel Button** | Redirect users to the Fixtures page | Users are redirected to the Fixtures page as desired | **PASS** | **PASS** |

![Add Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/add-team.png)

##### Add Match  
The Add Match page enables superusers to add a new match to the database. This section validates the functionality of this page.

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Add Match** | Function only accessible by superusers | Access to the Add Match Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to add a Match. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Add Match link** | Add Match form displays and is empty | The form displays as desired | **PASS** | **PASS** |
|   004  | **Required Fields** | Required fields are clearly indicated | Required fields are highlighted with an asterix | **PASS** | **PASS** |
|   005  | **Incomplete fields** indicated | Any incomplete, required fields are clearly indicated with a tooltip | Incomplete required fields are indicated | **PASS** | **PASS** |
|   006  | **Age Select** | Ensure the dropdown is populated with the age groups | The dropdown functions as desired | **PASS** | **PASS** |
|   007  | **Competition Select** | Ensure the select element is populated with the competitions and saves as desired | The competition select element functions as desired | **PASS** | **PASS** | 
|   008  | **Home Team Select** | The team select element has a list of teams conditionally filtered by age, saves as required | The select element and conditional select works as designed | **PASS** | **PASS** |
|   009  | **Away Team Select** | The team select element has a list of teams conditionally filtered by age, saves as required | The select element and conditional select works as designed | **PASS** | **PASS** |
|   010  | **Venue Select** | Display a list of the venues and save when selected | The Venue select element functions as desired | **PASS** | **PASS** |
|   011  | **KO Date & Time** | Ensure users can select the date and time of kick-off | The date time select works in Chrome but not in Firefox | **PASS** | **FAIL** |
> After reading the documentation I discovered I am using the correct version of the DateTime Input element. However, to date not all browsers have been modified to accept this element.

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   012  | **Referee Select** | Ensure the select element is populated with the various referee names can be selected | The dropdown functions as desired and match officials can be selected | **PASS** | **PASS** |
|   013  | **Asst1 Referee Select**  | Ensure the select element is populated with the various referee names can be selected | The dropdown functions as desired and match officials can be selected | **PASS** | **PASS** |
|   014  | **Asst2 Referee Select**  | Ensure the select element is populated with the various referee names can be selected | The dropdown functions as desired and match officials can be selected | **PASS** | **PASS** |
|   015  | **Add Team** | Ensure DB updates and users are redirected to the Match Detail page | The new Match gets created and users are redirected as desired | **PASS** | **PASS** |
|   016  | **Success Message** | Display a message when a new Match has been created | Message displays as desired | **PASS** | **PASS** |
|   017  | **DB Updates** | Ensure the new Match is written to the DB correctly | The Match details are added to the database as intended | **PASS** | **PASS** |
|   018  | **Cancel Button** | Redirect users to the Fixtures page | Users are redirected to the Fixtures page as desired | **PASS** | **PASS** |

![Add Match](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/add-match.png)

##### Add Travel
The Add Travel page enables Match Officials and Superusers to add Match officials travel expenses so that they get added to the match fees. This section validates the functionality of this page.

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Add Travel** | Function only accessible by superusers | Access to the Add Travel Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to add travel Expenses. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Add Travel link** | Redirects Match Officials and Superusers to the Add Travel Form | The Add Travel form displays as desired | **PASS** | **PASS** |
|   004  | **Match Summary** | Display a brief match summary so users know which match they are adding expenses for | A Match summary is rendered as desired | **PASS** | **PASS** |
|   005  | **Error Validation** | Ensure a warning is provided if the wrong input is given | A tooltip indicates to the user that the form required the number format | **PASS** | **PASS** |
|   006  | **Error Validation** | Ensure the travel expenses are input in the correct number format | The application displays a tooltip indicating the correct format | **PASS** | **PASS** |
|   007  | **Add Team** | Ensure DB updates and users are redirected to the Match Detail page | The new Match gets created and users are redirected as desired | **PASS** | **PASS** |
|   008  | **Success Message** | Display a message when a new Match has been created | Message displays as desired | **PASS** | **PASS** |
|   009  | **DB Updates** | Ensure the new Match is written to the DB correctly | The Match details are added to the database as intended | **PASS** | **PASS** |
|   010  | **Cancel Button** | Redirect users to the Fixtures page | Users are redirected to the Fixtures page as desired | **PASS** | **PASS** |

![Add Travel](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/add-travel.png)

##### Add Message
The Add Message page enables Match Officials and Superusers to add a message to that match. This section validates the functionality of this page.

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Add a Message** | Function only accessible by superusers | Access to the Add Chat function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to add a message to a match. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Add Message link** | Redirects Coaches, Match Officials and Superusers to the Add Message Form | The Add Message form displays as desired | **PASS** | **PASS** |
|   004  | **Pre-populated Data** | Make sure the form come prepopulated with the match and Author/users username | The form is rendered with the data for the match and author populated | **PASS** | **PASS** |
|   005  | **Required Fields** | Required fields are clearly indicated | Required fields are highlighted with an asterix and a tooltip appears if the user attempts to submit with an empty required field. | **PASS** | **PASS** |
|   006  | **Image Upload** | Make sure the image upload feature functions correctly | Images are uploaded correctly | **PASS** | **PASS** |
|   007  | **Add Message** | Ensure DB updates and users are redirected to the Match Messages page | The new Message gets created and users are redirected as desired | **PASS** | **PASS** |
|   008  | **Success Message** | Display a message when a new Message has been created | Message displays as desired | **PASS** | **PASS** |
|   009  | **DB Updates** | Ensure the new Message is written to the DB correctly | The Message is added to the database as intended | **PASS** | **PASS** |
|   010  | **Cancel Button** | Redirect users to the match detail page | Users are redirected back to the match detail page as desired | **PASS** | **PASS** |

![Add Chat](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/add-chat.png)

_____

#### **Edit Existing Data** <a name="edit-data"></a>
This sections defines the testing performed on the Superuser function which enable them to edit existing database records for Clubs, Teams and Matches. This allows superusers to change any field as required.

##### Edit Club
The Edit Club page enables superusers to retrieve a previously uploaded club from the database and edit any of the data previously supplied. This section validates the functionality of this page.
|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Edit Club** | Function only accessible by superusers | Access to the Edit Club Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to edit a Club. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Edit Club link** | Redirects superusers to the Edit Club Form | The Edit Club form displays as desired | **PASS** | **PASS** |
|   004  | **Load Data** | Populate the Edit Club form with data from the database | The correct data is rendered from the database | **PASS** | **PASS** |
|   005  | **Required Fields** | Required fields are clearly indicated if left unpopulated | Required fields are highlighted with an asterix, and tooltip appears if left unpopulated | **PASS** | **PASS** |
|   006  | **Update Club** | Ensure DB updates and users are redirected to the Club Directory page | The users are redirected as desired and the new Club details are rendered correctly  | **PASS** | **PASS** |
|   007  | **Success Message** | Display a message when the Club has been edited | Message displays as desired | **PASS** | **PASS** |
|   008  | **DB Updates** | Ensure the new Club Details are written to the DB correctly | The Club details are added to the database as intended | **PASS** | **PASS** |
|   009  | **Cancel Button** | Redirect users to the Club directory page | Users are redirected to the Fixtures page as desired | **PASS** | **PASS** |

![Edit Club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/edit-club.png)
_____

##### Edit Team
The Edit Team page enables superusers to retrieve a previously uploaded team from the database and edit any of the data previously supplied. This section validates the functionality of this page.  

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Edit Team** | Function only accessible by superusers | Access to the Edit Team Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to edit a Team. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Edit Team link** | Redirects superusers to the Edit Team Form | The Edit Team form displays as desired | **PASS** | **PASS** |
|   004  | **Load Data** | Populate the Edit Team form with data from the database | The correct data is rendered from the database | **PASS** | **PASS** |
|   005  | **Required Fields** | Required fields are clearly indicated if left unpopulated | Required fields are highlighted with an asterix, and tooltip appears if left unpopulated | **PASS** | **PASS** |
|   006  | **Update Team** | Ensure DB updates and users are redirected to the Team Directory page | The users are redirected as desired and the new Team details are rendered correctly  | **PASS** | **PASS** |
|   007  | **Success Message** | Display a message when the Team has been edited | Message displays as desired | **PASS** | **PASS** |
|   008  | **DB Updates** | Ensure the new Team Details are written to the DB correctly | The Team details are added to the database as intended | **PASS** | **PASS** |
|   009  | **Cancel Button** | Redirect users to the Team directory page | Users are redirected to the Fixtures page as desired | **PASS** | **PASS** |

![Edit Teams](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/edit-team.png)

##### Edit Match
The Edit Match page enables superusers to retrieve a previously uploaded match from the database and edit any of the data previously supplied. This section validates the functionality of this page. 

|   Test | Function        | Desired Result | Actual Result | Chrome v 92.0.4515.159 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:----------------------:|:-----------------------:|
|   001  | **Edit Match** | Function only accessible by superusers | Access to the Edit Match Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to Edit a Match. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Edit Match link** | Redirects superusers to the Edit Match Form | The Edit Match form displays as desired | **PASS** | **PASS** |
|   004  | **Load Data** | Edit Match form is populated with data from the database | The correct data is rendered from the database | **PASS** | **PASS** |
|   005  | **Select Elements** | Ensure all select elements and conditional lists function as desired | The select elements are rendered pre-populated and function as desired. The age/team conditional lists function as desired | **PASS** | **PASS** |
|   006  | **Required Fields** | Required fields are clearly indicated if left unpopulated | Required fields are highlighted with an asterix, and tooltip appears if left unpopulated | **PASS** | **PASS** |
|   007  | **Update Match** | Ensure DB updates and users are redirected to the Match Directory page | The users are redirected as desired and the new Match details are rendered correctly  | **PASS** | **PASS** |
|   008  | **Success Message** | Display a message when the Match has been edited | Message displays as desired | **PASS** | **PASS** |
|   009  | **DB Updates** | Ensure the new Match Details are written to the DB correctly | The Match details are added to the database as intended | **PASS** | **PASS** |
|   010  | **Cancel Button** | Redirect users to the Match directory page | Users are redirected to the Fixtures page as desired | **PASS** | **PASS** |

![Edit Match](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/edit-match.png)
> The DateTime input field will not render correctly in some browsers as they have not yet been updated to accept this input element.

_____
#### **Delete Existing Data** <a name="delete-data"></a>
This sections defines the testing performed on the Superuser function which enable them to delete existing database records for Clubs, Teams and Matches. This allows superusers to change any field as required.

##### Delete Club
The Delete Club function enables superusers to permanently remove a previously uploaded Club from the database. This section validates the functionality of this page.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|   001  | **Delete Club** | Function only accessible by superusers | Access to the Delete Club Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | Display Error | Display an Error if non-authorised user attempts to Delete a Club. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Delete Club link** | Should generate a Delete confirmation modal. The Club should not be deleted yet!! | The Delete Club button directs users to the delete confirmation modal. The `delete_club` function isn't called yet  | **PASS** | **PASS** |
|   004  | **Club Name** | The modal should clearly indicate which Club has been selected for deletion | The Club name is clearly displayed in the confirmation message | **PASS** | **PASS** |
|   005  | **Cancel Delete** | There should be an option to cancel the deletion before any data is lost | The cancel takes the user right back to the Clubs page without deleting the record | **PASS** | **PASS** |
|   006  | **Delete Club** | Ensure the Delete Club function is only called once the Delete Club button on the delete confirmation modal is clicked | Selecting the Delete Club button correctly deletes the selected club | **PASS** | **PASS** |
|   007  | DB Update | Ensure the record has been removed are no other records are affected aside from those linked through Foreign Keys |  | **PASS** | **PASS** |
> Deleting a Club obviously has a downstream effect on any matches and Teams associated with that club. Thus the clubs teams and matches featuring the deleted Club/Teams are also removed from the database. This is as intended.
No Errors occurred during testing.

![Delete Club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/delete-club.png)

##### Delete Team
The Delete Team function enables superusers to permanently remove a previously uploaded Team from the database. This section validates the functionality of this page.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|   001  | **Delete Team** | Function only accessible by superusers | Access to the Delete Team Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | Display Error | Display a Error if non-authorised user attempts to Delete a Team. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Delete Team link** | Should generate a Delete confirmation modal. The Team should not be deleted yet!! | The Delete Team button directs users to the delete confirmation modal. The `delete_team-` function isn't called yet  | **PASS** | **PASS** |
|   004  | **Team Name** | The modal should clearly indicate which Team has been selected for deletion | The Team name is clearly displayed in the confirmation message | **PASS** | **PASS** |
|   005  | **Cancel Delete** | There should be an option to cancel the deletion before any data is lost | The cancel takes the user right back to the Clubs page without deleting the record | **PASS** | **PASS** |
|   006  | **Delete Team** | Ensure the Delete Team function is only called once the Delete Team button on the delete confirmation modal is clicked | Selecting the Delete Team button correctly deletes the selected club | **PASS** | **PASS** |
|   007  | **DB Update** | Ensure the record has been removed are no other records are affected aside from those linked through Foreign Keys |  | **PASS** | **PASS** |
> Deleting a Team obviously has a downstream effect on any matches featuring that team. Thus matches featuring the deleted team are also removed from the database. This is as intended.
No Errors occurred during testing.

![Delete Team](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/delete-team.png)

##### Delete Match
The Delete Match function enables superusers to permanently remove a previously uploaded Match from the database. This section validates the functionality of this page.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|   001  | **Delete Match** | Function only accessible by superusers | Access to the Delete Match Function is only accessible by a superuser | **PASS** | **PASS** |
|   002  | **Display Error** | Display a Error if non-authorised user attempts to Delete a Match. Redirect back to Home | A Error message displays and user redirected to home page | **PASS** | **PASS** |
|   003  | **Delete Match link** | Should generate a Delete confirmation modal. The Match should not be deleted yet!! | The Delete Match button directs users to the delete confirmation modal. The `delete_match` function isn't called yet  | **PASS** | **PASS** |
|   004  | **Match Name** | The modal should clearly indicate which Match has been selected for deletion | The Match name is clearly displayed in the confirmation message | **PASS** | **PASS** |
|   005  | **Cancel Delete** | There should be an option to cancel the deletion before any data is lost | The cancel takes the user right back to the Clubs page without deleting the record | **PASS** | **PASS** |
|   006  | **Delete Match** | Ensure the Delete Match function is only called once the Delete Match button on the delete confirmation modal is clicked | Selecting the Delete Match button correctly deletes the selected club | **PASS** | **PASS** |
|   007  | **DB Update** | Ensure the record has been removed are no other records are affected aside from those linked through Foreign Keys | DB records are updated as design in the DB Schema | **PASS** | **PASS** |

![Delete Match](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/delete-match.png)
_____

#### **User Profile** <a name="user-profile"></a>

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|   001  |  **User Profile Link** | My Account - Profile link should direct users to their Profile page |  | **PASS** | **PASS** |
|   002  | **Username** | The users username should render at the top of the page | Username renders as desired | **PASS** | **PASS** |
|   003  | **Team Displayed** | If the user is a registered coach, their team badge and team name should be displayed below their username | The Club badge and team name are displayed for appropriate users | **PASS** | **PASS** |
|   004  | **Role Displayed** | If the user is a registered Coach, Referee or Superuser their role should be displayed along with the other information | The role is displayed for logged in Superusers, Coaches and Ref's | **PASS** | **PASS** |
|   005  | **Personal Details Displayed** | The users personal details will be rendered if they have completed and purchaces and selected the save info field, of have updated their profile from this page | Personal details are pre-populated where appropriate | **PASS** | **PASS** |
|   006  | **Previous Orders Displayed** | Any previous payments made by the user should be displayed on this screen | Previous payments are correctly displayed | **PASS** | **PASS** |
|   007  | **Order Link** | The order number should take the user to a checkout success page showing payment details | The order link functions correctly | **PASS** | **PASS** |
|   008  | **Back to Profile Link** | The back to profile link on the Payment Summary should redirect users back to the Profile page | The link works as it should | **PASS** | **PASS** |
|   009  | **Update Profile** | Profile data in the DB is updated if the user changes any of the form fields and selects update | The profile data is written to the database correctly if the user adds a new profile or changes an existing profile | **PASS** | **PASS** |

> I have intentionally not included a Delete Profile function for this section of the app. Due to the nature of the app and the way it functions I didn't want users to have this ability and inadvertently affect downstream processes.

![User Profile](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/profile.png)

______

### **Automated Testing** <a name="automated-testing"></a>
Automated testing was carried out on the app's of RefereE-Pay which contain Models, Forms and . The results of the testing have been captured in a coverage report, which is illustrated in the image below.

![Automated Testing Report](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/functionality-testing/coverage-report.png)
>I would have liked to have conducted more automated testing, but struggled with creating tests for individual matches, clubs, teams etc. With more time and more background reading I am confident I can increase the amount of code tested in this way.

______
### **Appearance Testing** <a name="appearance"></a>
This web app was primarily developed on a Google Chrome browser, on a Windows Laptop. The app has been regularly tested on Firefox to check functionality. This section tests for any changes in appearance between the different browsers.  

|       Page      |  Desired Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:---------------:|-----------------|-----------------------|-------------------------|
|  **Landing Page**   | Minimal visible difference | No visible difference | No visible difference |
|  **Matches**        | Minimal visible difference | No visible difference | Dropdown appearance slightly different |
|  **Match Detail**   | Minimal visible difference | No visible difference | Match officials totals show up and down arrows |
|  **Edit Match**     | Minimal visible difference | No visible difference | Dropdown appearance slightly different. Date/Time picker does not function as desired |
|  **Add Match**      | Minimal visible difference | No visible difference | Dropdown appearance slightly different. Date/Time picker does not function as desired |
|  **Add Travel**     | Minimal visible difference | No visible difference | Match officials travel show up and down arrows |
|  **Messages**       | Minimal visible difference | No visible difference | Dropdown appearance slightly different |
|  **Add Message**    | Minimal visible difference | No visible difference | Dropdown appearance slightly different |
|  **Clubs**          | Minimal visible difference | No visible difference | No visible difference  |
|  **Edit Club**      | Minimal visible difference | No visible difference | Dropdown appearance slightly different |
|  **Add Club**       | Minimal visible difference | No visible difference | No visible difference  |
|  **Teams**          | Minimal visible difference | No visible difference | No visible difference  |
|  **Edit Team**      | Minimal visible difference | No visible difference | Dropdown appearance slightly different |
|  **Add Team**       | Minimal visible difference | No visible difference | Dropdown appearance slightly different | 
| **Add Competition** | Minimal visible difference | No visible difference | No visible difference  |
|  **Kit Bag**        | Minimal visible difference | No visible difference | No visible difference  |
|  **Checkout**       | Minimal visible difference | No visible difference | No visible difference  |
| **Checkout Success**| Minimal visible difference | No visible difference | No visible difference  |
| **Profil**e         | Minimal visible difference | No visible difference | No visible difference  |
| **Sign-up**         | Minimal visible difference | No visible difference | No visible difference  |
| **Sign-in**         | Minimal visible difference | No visible difference | No visible difference  |
| **Log-out**         | Minimal visible difference | No visible difference | No visible difference  |

______

### **Code Quality and Validation** <a name="code-validation"></a> 
Online tools have been used to validate the HTML, CSS, Python and JavaScript files to ensure they are free from errors, and comply with the latest standards. The results of these tests are documented below. 

#### **HTML Validation**
This section contains the results and any warnings or errors reported during HTML validation using the WC3 validator. 

|      Page       | Error / Warning | Comment  |
|-----------------|:---------------:|:--------:|
|  **Landing Page**   |       None      | **PASS** |
|  **Matches**        |       None      | **PASS** |
|  **Match Detail**   |       None      | **PASS** |
|  **Edit Match**     |       None      | **PASS** |
|  **Add Match**      |       None      | **PASS** |
|  **Add Travel**     |       None      | **PASS** |
|  **Messages**       |       None      | **PASS** |
|  **Add Message**    |       None      | **PASS** |
|  **Clubs**          |       None      | **PASS** |
|  **Edit Club**      |       None      | **PASS** |
|  **Add Club**       |       None     | **PASS** |
|  **Teams**          |       None      | **PASS** |
|  **Edit Team**      |       None      | **PASS** |
|  **Add Team**       |       None      | **PASS** | 
| **Add Competitio**n |       None      | **PASS** |
|  **Kit Ba**g        |       None      | **PASS** |
|  **Checkou**t       |       None      | **PASS** |
| **Checkout Success**|       None      | **PASS** |
| **Profile**         |       None      | **PASS** |
| **Sign-up**         |       None      | **PASS** |
| **Sign-in**         |       None      | **PASS** |
| **Log-out**         |       None      | **PASS** |

#### **CSS Validation**
The following section contains the results and any warnings or errors reported during CSS validation using the WC3 validator.

|    CSS File     | Error / Warning |  Comment |
|:---------------:|:---------------:|----------|
|     **base.css**    |       None      | **PASS** |
|     **home.css**    |       None      | **PASS** |
|   **matches.css**   |       None      | **PASS** |
|  **checkout.css**   |       None      | **PASS** |
|  **profile.css**    |       None      | **PASS** |


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
I requested Club Officials and the Referees Coach for the Cheltenham Youth Football League to test the website to gather their feedback on the User Experience and Interactivity. What follows are the comments I received in return:
|   User   | Feedback |
|:---------:|----------|
|  Dave Pitts - Club Secretary LRFC | Very professional looking website and a great idea. Simple enough to navigate and pay match officials Fees |

____

### **Responsiveness Testing** <a name="responsiveness"></a>
I have conducted continuous responsiveness testing, right up to the final submission, to ensure the website functions on different devices and in both portrait and landscape orientation, using Google Devtools and Responsinator.com.
This project has been deployed using Heroku and the website has been continuously reviewed on several real devices:
  - Samsung Galaxy S9 (360 x 740) and (740 x 360)
  - Samsung Tab A (768 x 1024) and (1024 x 768)
  - HP Laptop with attached monitor

This helped me make changes and apply appropriate media queries to maintain responsiveness.

The table below contains lists the results of the Responsiveness testing and links to images compiled from Google Devtools using the following Devices:
- iPhone 5/SE (320 x 568) and (568 x 320)
- iPhone 6/7/8 (375 x 667) and (667 x 375)
- iPad (768 x 1024) and (1024 x 768)
 

|  Test  | Page | Responsiveness Image Link | Result |
|:------:|------|--------------------|--------|
|   001  |**Landing Page**|![Home / Landing Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/landing-page.png)| **PASS** |
|   002  | **Matches**    | ![Fixtures Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/matches.png) | **PASS** |
|   003  | **Match Detail** | ![Match Detail Page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/match-detail.png) | **PASS** |
|   004  | **Edit Matc**h | ![Edit a Match page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/edit-match.png) | **PASS** |
|   005  |** Add Match**  | ![Add a Match page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/add-match.png) | **PASS** |
|   006  | **Add Travel** | ![Add Match Officials travel expenses](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/add-travel.png) | **PASS** |
|   007  | **Messages**   | ![Match Messages page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/match-messages.png) | **PASS** |
|   008  | **Add Message** | ![https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/add-message.png](image.jpg) | **PASS** |
|   009  | **Clubs**      | ![Clubs Directory](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/clubs.png) | **PASS** |
|   010  | **Edit Club**  | ![Edit a Clubs details](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/edit-club.png) | **PASS** |
|   011  | **Add Club**   | ![Add a club to the DB](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/add-club.png) | **PASS** |
|   012  | **Teams**      | ![Teams Directory by Club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/teams.png) | **PASS** |
|   013  | **Edit Team**  | ![Edit one of a Clubs teams](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/edit-team.png) | **PASS** |
|   014  | **Add Team**   | ![Add a new team to a club](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/add-team.png) | **PASS** | 
|   015  | **Add Competition** | ![Add a new Competition](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/add-competition.png) | **PASS** |
|   016  | **Kit Bag**    | ![Kit Bag view / Pending match payments](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/kit-bag.png) | **PASS** |
|   017  | **Checkout**   | ![Checkout page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/checkout.png) | **PASS** |
|   018  | **Checkout Success** | ![Successful Checkout confirmation](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/checkout-success.png) | **PASS** |
|   019  | **Profile**    | ![User profile information page](https://github.com/GazzaJ/CI-MS4-RefereE-pay/blob/master/ReadMe_Images/responsiveness/profile.png) | **PASS** |

____

### **Performance Testing** <a name="performance"></a>
The website has been performance testing using the following tools:
 - Google Lighthouse (Desktop)
> Testing was performed in incognito mode as Google extensions can affect the results of the lighthouse testing.


|    Page    | Performance | Accessibility | Best Practices | SEO  |
|:----------:|:-----------:|:-------------:|:--------------:|:----:|
|**Landing Page**|     97%     |       97%     |     100%       |  90% |
| **Matches**    |     95%     |       96%     |     100%       | 100% |
| **Match Detail** |   93%     |       95%     |      93%       |  90% |
| **Edit Match** |     96%     |       91%     |     100%       |  90% |
| **Add Match**  |     98%     |       93%     |     100%       |  90% |
| **Add Travel** |     98%     |       97%     |     100%       |  90% |
| **Messages**   |     95%     |       97%     |     100%       |  90% |
| **Add Message** |    96%     |       92%     |     100%       |  90% |
| **Clubs**      |     94%     |       97%     |     100%       |  80% |
| **Edit Club**  |     98%     |       85%     |     100%       |  80% |
| **Add Club**   |     98%     |       93%     |     100%       |  90% |
| **Teams**      |     98%     |       92%     |     100%       |  90% |
| **Edit Team**  |     98%     |       99%     |     100%       |  90% |
| **Add Team**   |     94%     |       97%     |      93%       |  90% |
| **Add Competition** |  98%   |       97%     |     100%       |  90% |
| **Kit Bag**    |     97%     |       97%     |     100%       |  90% |
| **Checkout**   |     87%     |       97%     |     100%       |  90% |
| **Checkout Success** |  96%  |       97%     |     100%       |  90% |
| **Profile**    |     97%     |       97%     |     100%       |  90% |

 - Google Lighthouse (Mobile)  

|    Page    | Performance | Accessibility | Best Practices | SEO  |
|:----------:|:-----------:|:-------------:|:--------------:|:----:|
|**Landing Page**|     85%     |       98%     |     100%       |  92% |
| **Matches**    |     79%     |       97%     |     100%       |  83% |
| **Match Detail** |   82%     |       97%     |     100%       |  92% |
| **Edit Match** |     78%     |       92%     |     100%       |  92% |
| **Add Match**  |     81%     |       90%     |     100%       |  92% |
|**Add Travel** |     82%     |       98%     |     100%       |  92% |
| **Messages**   |     82%     |       98%     |     100%       |  92% |
| **Add Message** |    82%     |       91%     |     100%       |  92% |
| **Clubs**      |     87%     |       98%     |     100%       |  83% |
| **Edit Club**  |     69%     |       82%     |      93%       |  83% |
| **Add Club**   |     78%     |       90%     |     100%       |  92% |
| **Teams**      |     83%     |       90%     |      93%       |  92% |
| **Edit Team**  |     78%     |       99%     |     100%       |  92% |
| **Add Team**   |     82%     |       98%     |     100%       |  92% |
| **Add Competition** |  82%   |       98%     |     100%       |  92% |
|**Kit Bag**    |     75%     |       95%     |     100%       |  92% |
| **Checkout**   |     69%     |       97%     |     100%       |  92% |
| **Checkout Succes**s |  79%  |       97%     |     100%       |  92% |
| **Profile**    |     77%     |       96%     |     100%       |  92% |

____

### **Security Testing** <a name="security"></a>
The following tests have been performed on the security features implemented on this site, and are documented in the table below:
#### **URL Manipulation**
These tests ensure that there are appropriate levels of access to the various pages in the web app, and that anonymous users cannot access content requiring login, or that registered users are only able to access content equal to their access rights:

| Page | URL | Registered user - Desired Result | Status | Anonymous User - Desired Result | Status |
|------|-----|----------------------------------|--------|---------------------------------|--------|
| **Add Competition** | `matches/comp/` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Add Club** | `matches/club/` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Add Team** | `matches/team/` | Error message displayed  | **PASS** | Redirected to login | **PASS** |
| **Add Match** | `matches/add/` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Add Travel** | `matches/travel/match.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Edit Club** | `matches/edit_club/club.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Edit Team** | `matches/edit_team/team.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Edit Match** | `matches/edit/game.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Delete Club** | `matches/delete_club/club.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Delete Team** | `matches/delete_team/team.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Delete Match** | `matches/delete/game.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Add Message** | `matches/add_chat/game.id` | Error message displayed | **PASS** | Redirected to login | **PASS** |
| **Kit bag** | `bag/` | N/A | N/A | Redirected to login | **PASS** |
| **Checkout** | `checkout/` | N/A | N/A | Redirected to login | **PASS** |
| **Profile** | `profile/` | N/A | N/A | Redirected to login | **PASS** |
  
#### **Secure Usage**
The functionality of RefereE-Pay is deliberately compartmentalised by a users role and the permissions granted to those roles restrict what each role can achieve. This section describes the testing which has been performed to validate this compartmentalisation.

##### **General users**
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | **Regular Users** | Registered users limited to viewing the Match Details their Profile page | Registered users access is limited by design. The app is intended for a specific audience |  **PASS** | **PASS** |
|  002   | **Regular Users** | Are NOT authorised to proceed beyond basic functionality of viewing Fixtures, Clubs, Teams and Profile | The regular user without an assigned role has no access beyond viewing fixtures, clubs, and their profile |  **PASS** | **PASS** |

##### Coaches
Aside from Superusers, coaches have one of the more prominent roles and are the primary audience for this app.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | **Assigned Role** | Users need to be assigned the role of Coach and be assigned their team by a Superuser | Users are not able to edit or update this part of their user profile |  **PASS** | **PASS** |
|  002   | **Match Details** | All authorised coaches can view Match Details | Functions as designed |  **PASS** | **PASS** |
|  003   | **Add to Bag** | Home Team coaches can add matches to the kit bag | Coaches are able to add a match to their kit bag |  **PASS** | **PASS** |
|  004   | **Add To Bag** | The should be no way to add another teams match to your bag | Access to Add to bag function is role and user specific |  **PASS** | **PASS** |
|  005   | **PAID** | Matches that have been paid for are indicated and "Add to bag button is removed" | A "Paid" stamp appears in the Review Match Fees section and Add to bag button is removed |  **PASS** | **PASS** |
|  006   | **View Messages** | A registered coach can access the Match Messages page and view any messages posted there | Access to the Match messages is as desired and is not time limited. | **PASS** | **PASS** |
|  007   | **Add Messages** | Able to add messages to the Match | Coaches can add messages to the match  | **PASS** | **PASS** |
|  008   | **Time Limit** | Add Message button should no longer render after kick-off date/time | The Add message does not render for matches whose kick off date has passed | **PASS** | **PASS** |
|  009   | **Message tags** | Messages are tagged by Author | The messages are coloured by Coach or Referee, and the username is added in the message field |  **PASS** | **PASS** |
|  010   | **Kit Bag** | Coaches can access the kit bag from their Account in the Navbar or the grand total icon on the navbar | This is an important function which enables the coach user to check pending payments. This access works as desired |  **PASS** | **PASS** |
|  011   | **Checkout** | Once in the Kit bag Coaches can proceed to Checkout as long as there are items in their bag | This functions correctly. If no items exist in the bag a message is displayed and there is no option to proceed to checkout. |  **PASS** | **PASS** |
|  012   | **Payment** | Authorised to make payments  | Registered Coaches can proceed through the payment process and pay their match fees |  **PASS** | **PASS** |

![Coaches]()

##### **Referees**
Referees have similar access rights to Coaches with the exception that they have no requirement to make payments into the system, and thus don't need access to the kit bag or checkout apps.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | **Assigned Role** | Users need to be assigned the role of Referee by a Superuser | Users are not able to edit or update this part of their user profile |  **PASS** | **PASS** |
|  002   | **Match Details** | All authorised referees can view Match Details | Functions as designed and data renders as desired | **PASS** | **PASS** |
|  003   | **Add Travel** | Have the ability to modify travel expenses up to Kick-off day and time | Match officials can add and update any travel expenses using the add travel function as desired | **PASS** | **PASS** |
|  004   | **Add travel** | Access to add travel button is removed after kick-off | The Add Travel button no longer displays after kick-off date and time | **PASS** | **PASS** |
|  005   | **Add Travel** | Access to Add travel is reserved to refs and superusers. Cannot manipulate URLS to add travel | Access works correctly. An error message is displayed if an unauthorised user attempts to manipulate a URL to add travel | **PASS** | **PASS** |
|  006   | **View Messages** | A registered referee can access the Match Messages page and view any messages posted there | Access to the Match messages is as desired and is not time limited. | **PASS** | **PASS** |
|  007   | **Add Messages** | Able to add messages to the Match | Referees can also add messages to the match in reply to coaches | **PASS** | **PASS** |
|  008   | **Time Limit** | Add Message button should no longer render after kick-off date/time | The Add message does not render for matches whose kick off date has passed | **PASS** | **PASS** |

##### **Superusers**
Superusers of the RefereE-Pay web-app have the access rights of Coaches and Referees, and are able to act on their behalf, with the additional access to Club, Team and Match Admin.

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | **Admin Menu**  | Should be able to access the Game admin menu on the navbar | Access to the Admin menu works as desired for super users |
|  002   | **Add Competition** | Have the ability to add a new competition name | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |
|  003   | **Add Club** | Have the ability to add a new Club to the database | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |
|  004   | **Add Team** | Have the ability to add a new Team to a Club | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |
|  005   | **Add Match** | Have the ability to create a new match and assigns teams, venues and match officials | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |
|  006   | **Edit Club** | Have the ability to edit or update an existing Club | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |
|  007   | **Edit Team** | Have the ability to edit an existing Club's team data | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |
|  008   | **Edit Match** | Have the ability to edit and update the details of any future match. Cannot edit past matches | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |
|  009   | **Delete Club** | Should be able to permanently delete a Club from the database. Confirmation Modal should appear | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |
|  010   | **Delete Team** | Should be able to permanently delete a Team from the associated Club and the database. Confirmation Modal should appear | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |
|  011   | **Delete Match** | Should be able to permanently delete a Match from the database. Confirmation Modal should appear | Functions as desired. Cannot be achieved through URL manipulation | **PASS** | **PASS** |

______

## **Bugs, Issues and Fixes** <a name="bugs"></a>
The following table explains the bugs and issues encountered while building this website.
|  Issue #   |  Bug or Issue  |  Description  |  Solution  |
|:----------:|----------------|---------------|------------|
| 001 | **AllAuth Error** | Redirect to pages not functioning as desired, returning 404 | My definition of the login redirect url was incorrect |
| 002 | **Add to bag** |  After restyling my kit bag summary table I was unable to add older matches prior to datetime_now to the bag | While editing the HTML I had inadvertently removed the { request.path } required for the redirect_url variable |
| 003 | **Chained Select** | Error for Edit Match view using the code at https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html. Unable to process the filter statement. | After much trial and error, I referred to the django Queryset API reference regarding the filter() method and field lookups and combined the `self.instance.age` with a __contains lookup. `team_name__contains=self.instance.age` |
| 004 | **DateTime Input** | Despite using the correct and current DateTime input element, some browsers have not yet been updated to this version and thus the handy date time input feature doesn't display. Users then have to enter the date and time in a particular text format. This has limited impact in this application as it would only affect Admin/Superusers creating or editing Matches. | A potential solution would be to change my Models, Forms and Templates to use separate Date input and Time input fields. |
| 005 | **Duplicate Order Creation** | The payment process for this web app functions as desired other than it appears to create save duplicate orders into the database.  I believe I have adapted the Boutique Ado code to the best of may ability and can't seem to find any obvious errors. | This does not appear to occur in the development version of the app; and after searching through Slack it appears that this could be a function of "race condition" wherein the app and webhook are vying with each other to execute the code. As undesirable as this is, I have checked the Stripe dashboard and confirmed that only a single payment is being processed.

**[Back to Github Repo](https://github.com/GazzaJ/CI-MS4-RefereE-pay/)**