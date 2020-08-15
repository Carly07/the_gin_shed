# The Gin Shed

[![Build Status](https://travis-ci.org/Carly07/the_gin_shed.svg?branch=master)](https://travis-ci.org/Carly07/the_gin_shed)

The Gin Shed is a web application, designed, built and deployed by me, Carly Clark, to satisfy the requirements of the final project for the Code Institute Full Stack Web Development diploma.

The website's is intended to be a custom built base for The Gin Shed company, allowing the owners to list and manage products for sale whilst also creating an attractive, smooth and effortless online shopping experience for customers who enjoy fine quality gins. The site also offers interactive features such as product reviews, receipes and blogs to encourage user activity and maximise user experience. 


## Demo
A live demo can be found [here](https://the-gin-shed.herokuapp.com/).


## UX

### User Stories

| ID  | As a …                | I want to be able to…                                                              | So that I can…                                                                                        |
| ----| --------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Registration and User Accounts                                                                                                                                                                                           |
| 1   | public user           | easily register for an account                                                     | have a personal acount and view my profile                                                            |
| 2   | registered user       | receive an email confirmation after registering                                    | verify my account registration was successful                                                         |
| 3   | registered user       | easily log in and out                                                              | access my personal acount information                                                                 |
| 4   | registered user       | easily recover my password if I forget it                                          | regain access to my acount                                                                            |
| 5   | registered user       | have a personalised user profile                                                   | View my order history, order confirmation and payment information                                     |
| 6   | registered user       | rate and review a product                                                          | provide feedback to store owner and other shoppers                                                    |
| 7   | registered user       | delete any product reviews that I have left                                        | remove a review if I have changed my mind                                                             |
| 8   | registered user       | add a cocktail recipe                                                              | share my recipe with other users                                                                      |
| 9   | registered user       | edit or delete any recipes that I have added                                       | amend / update the recipe or remove it if I no longer wish to share it                                |
| 10  | registered user       | leave a comment on a blog post                                                     | share my thoughts on the blog post with other users                                                   |
| 11  | registered user       | delete any comments I leave on a blog post                                         | remove them if I change my mind or its no longer relevant                                             |
| Viewing and Navigation                                                                                                                                                                                                                              |
| 12  | site user (all users) | view a list of all products                                                        | select some to purchase                                                                               |
| 13  | site user (all users) | view specific category of products                                                 | quickly browse the type of products that I am interested in                                           |
| 14  | site user (all users) | view individual product details                                                    | identify the product description, price, image, rating and corresponding product reviews              |
| 15  | site user (all users) | easily view total of shopping basket                                                 | avoid spending too much                                                                               |
| 16  | site user (all users) | view a list of cocktail recipes                                                    | find a new and exciting recipe to make with the gin I purchase                                        |
| 17  | site user (all users) | view an individual cocktail recipe                                                 | read the list of ingredients, method and all other recipe information                                 |
| 18  | site user (all users) | view a list of blog posts                                                          | select interesting articles to read about all things gin                                              |
| 19  | site user (all users) | view an individual blog post                                                       | read the full post and any corresponding comments left by other users                                 |
| 20  | site user (all users) | view the Contact Us page                                                           | contact the store owner to ask a question or provide feedback                                         |
| 22  | site user (all users) | view the privacy policy                                                            | see how my personal date is managed and understand my rights                                          |
| 23  | site user (all users) | view the websites terms of use                                                     | understand what I am agreeing to comply with by using the site.                                       |
| Sorting and Searching                                                                                                                                                                                                                               |
| 24  | site user (all users) | search for a product by name or description                                        | find a particular product that I would like to purchase                                               |
| 25  | site user (all users) | easily see the products matching my search criteria and number of results returned | quickly see whether the product I want is available                                                   |
| 26  | site user (all users) | sort the list of available products                                                | view products by category, price or rating                                                            |
| 27  | site user (all users) | sort a specific category of products                                               | view the best priced or best rated products in a specific category or view them in alphabetical order |
| Purchasing and Checkout                                                                                                                                                                                                                             |
| 28  | site user (all users) | easily select the quantity of a product to add to my shopping cart                 | purchase the amount of products I want                                                                |
| 29  | site user (all users) | view items in my cart                                                              | review the items I intend to purchase and identify the total cost                                     |
| 30  | site user (all users) | remove items or change the quantity of individual items in my cart                 | amend my order before checkout                                                                        |
| 31  | site user (all users) | easily enter my personal and payment information                                   | check out quickly with no problems                                                                    |
| 32  | site user (all users) | feel confident that my personal data is safe and secure                            | provide the information required to complete my purchase                                              |
| 33  | site user (all users) | view order confirmation                                                            | verify that I haven't made any mistakes                                                               |
| 34  | site user (all users) | receive an email confirmation after checkout                                       | Keep a record of what I have purchased                                                                |
| Admin and Store Management                                                                                                                                                                                                                          |
| 35  | Store Owner           | add products                                                                       | list items for sale                                                                                   |
| 36  | Store Owner           | edit / update a product                                                            | adjust product details where necessary                                                                |
| 37  | Store Owner           | delete a product                                                                   | remove items that are no longer available                                                             |
| 38  | Store Owner           | add new cocktail recipe                                                            | share gin cocktails with users and encourage them to purchase products on offer                       |
| 39  | Store Owner           | edit / update any cocktail recipes shared on the website                           | manage content added by other users, i.e amend errors or typos                                        |
| 40  | Store Owner           | delete any cocktail recipe shared on the website                                   | manage content added by other users i.e. remove recipes that are not appropriate                      |
| 41  | Store Owner           | add blog posts                                                                     | share interesting articles about gin                                                                  |
| 42  | Store Owner           | edit / update a blog post                                                          | amend errors or typos                                                                                 |
| 43  | Store Owner           | delete a blog post                                                                 | remove blogs that are no longer wanted                                                                |


### Design 
Inspired by the drink itself, The Gin Shed website has an overall clean, crisp, neutral feel interspersed with botanical greens and an emphasis on high quality gin products. The following design choices were made with this in mind:

#### Fonts
The primary font 'Open Sans Condensed' was chosen for the main text of the site because of it clear readability and clean, crisp style providing a neutral, yet friendly appearance. This font also looks good in uppercase to add emphasis to the buttons.

By contrast, the secondary font 'Amatic SC' was chosen for the brand name, navbar headings and page headings because of it simple but effective hand drawn, natural and slightly rugged feel, which I felt in keeping with the botanical garden shed theme of the brand. 

#### Icons
To keep the site uncluttered, clean and minimalist, a small number of icons were carefully selected and implemented across the site. 

The search, user account and shopping basket icons were used in the navigation bar as they are conventionally used in this setting and would be what the user expects to see.

Star icons are utilised for users to rate products in the review section and add visual emphasis when displaying the average rating of a product as per convention.

A small tag icon is used to highlight the product category as well as cocktail and blog tags. Similarly, a small eye icon is used to signify the number of views on a blog post. 

Social media logo icons are included as links to the associated social media page. Though, as The Gin Shed is not a real company and does not therefore have a social medica presence, the icons simply link direct to the main log in page at this time.

#### Colours

![colours](colours.png)

* White `#fff`
* Black `#000`
* Light Green `#788E5C`
* Dark Green `#414e2f`
* Light Grey `#6c757d`

The white, black and green color scheme was chosen to create a clean, crisp, botanical theme. 

#### Images
Images of gin were carefully selected to appeal to users senses whilst not detracting from the overall theme.

#### Styling
Square corners were implemented on all form, image and button elements to create the desired sharp, crisp appearance. 

Colour effects and or a curser pointer were added to content when hovered over to notify the user that they can click on the link/button to navigate to another area of the site. 


### Wireframes
The basic wireframes for this site can be found below
    
* [Home Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/home.jpg)
* [About Us Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/about-us.jpg)
* [Contact Us Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/contact-us.jpg)
* [Add/Edit Product Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/add-edit-product.jpg)
* [Product Results Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/product-results.jpg)
* [Product Detail Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/product-detail.jpg)
* [Shopping Basket Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/shopping-basket.jpg)
* [Secure Checkout Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/secure-checkout.jpg)
* [Profile Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/user-profile.jpg)
* [Add / Edit Cocktail Recipe Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/add-edit-cocktail.jpg)
* [Recipe Results Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/cocktail-results.jpg)
* [Cocktail Recipe Detail Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/cocktail-detail.jpg)
* [Add / Edit Blog Post Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/add-edit-blog.jpg)
* [Blog Results Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/blog-results.jpg)
* [Blog Post Detail Page](https://github.com/Carly07/the_gin_shed/tree/master/static/wireframes/blog-detail.jpg)


## Features

### Existing Features

#### Navbar
The Navbar features on every page across the site so to ensure users are able to easily navigate from wherever they are.  

On desktop view there is a fixed top nav featuring the brand name to the far left and three large icons to the right providing options to search for products, access account and view their shopping basket. 

Beneath the top nav lies the main navbar featuring three dropdown menus in the centre; gin shop, gin cocktails and gin blog. 

The Gin Shop menu offers users the ability to view a list of 'all products' or to view products by one of the following three categories, 'gin', 'mixers' and 'accessories'. 

The Gin Cocktail menu provides all users with the option to view a full list of cocktails whilst logged in users will note an additional option to 'add recipe'. 

Similarly, the Gin Blog menu offers all users a link to view 'Blog Posts' whilst store owners will have an additional option to 'Add Blog'. 

On smaller devices including mobiles and tablets, the brand name is omitted and the main navbar has been collapsed behind a bootstrap toggler button (burger icon) in its place. The search, user account and shopping basket icons remain to the right of the navbar but are smaller than on desktop view. It was felt that this would enhance user experience by ensuring quick and easy navigation whilst still promoting a minimalist design. 

#### Home Page
The landing page features a jumbotron displaying a mouth watering glass of gin to appeal to users senses. On desktop view, the jumbotron contains the phrase "Let the fun be gin" and a button to 'shop now' directing users straight to the product results. On mobile view the phrase and button are omitted but the brand name appears at the top of the jumbotron as it is missing fromt he navbar on small screens. Users can scroll down the page to information about free delivery, cocktail recipes and the blog. 

#### Search bar
Users can search for a particular product or for a product containing a specific word by clicking on the magnifying glass icon in the navbar and entering their search criteria in the dropdown box provided.

#### Gin Shop
##### Add Product
Store Owners can add new products to the shop, by navigating to the 'my account' menu and selecting 'Add Product'. This directs the user to a simple form for them to enter all the product details rquired. 

##### Product Results
Products are displayed using bootstrap cards, with a large product image at top and the product name, price, rating and category detailed in the card body beneath. The large image is intended to draw attention to the product. 

Results are listed in rows of 4 on extra large screens, rows of 3 on large and rows of 2 on tablets whilst products are stacked on top of each other on mobile view. Rows are separated by a horizontal rule to improve user experience.

Store owners will also have the ability to edit or delete products for the store by clicking on with the small 'Edit' or 'Delete links on each product.

##### Category Filtering 
A small button indicating the category currently displayed in the results is situated at the top of the page under the 'Product' page heading. If the user has selected 'all products' from the navbar, they will see three buttons each referencing a category. Users will be able to click these buttons to filter the results to their chosen category.

##### Sorting Product Results
The product results page includes a select menu for users to sort the results by:

"Price: high to low" 
"Price: low to high"
"Rating: high to low" 
"Rating: low to high"
"Name: A-Z" 
"Name: Z-A"
"Category: A-Z" 
"Category: Z-A"

##### Back to Top button
Users will note a small button with a arrow point up at the bottom right of their view. When scrolling down the results, users can click on this button to return to the top quicky and easily.

#### Product Detail Page
Users can click on a product image to view full details for that particular product. On desktop view, users are presented with the product image to the left and all the product information on the right, whilst on mobile view the image is stacked on top of the product information. 

##### Quantity Select
From the product detail page, users can select a quantity of the product to add to their basket. Should a user try to select more than what is currently in stock by typing a value rather than using the buttons, they will be presented with a validation error notifying them that the value must be less than or equal to X number. Similarly if a user adds the maximum quantity to their basket and then returns to try and add more of that product, an error message will display in the top right corner advising them that there are only x number left in stock. 

##### Product Review Function
At the bottom of the product detail page, users can view reviews that have been left for that particular product. Logged in users will also be presented with a simple form including a star rating system to enable them to write a review and rate the product from 1-5, whilst those not currently logged in will be prompted to register or log in in order to leave a review.  Logged in users will have the ability to delete any reviews that they have written. 

Individual star ratings are used to calculate the average product rating which are displayed on product results and on the product detail page. 

#### Shopping Basket
The shopping basket icon is located to the far right of the navigation bar. Once a user (whether logged in or not) has added at least one item to their basket, the icon turns green and the grand total appears below the icon. This feature enables users to easily see the total cost of the items in their basket so they can keep track of their spending. The color green was chosen because it contrasts from the black icons whilst remaining consistant with the overall colour scheme. Users are also able to click on the icon to view the contents of their shopping basket. 

On the shopping basket page, desktop users will see 5 columns containing the product image, name, price, Quantity and subtotal. Different products are displayed in different rows. In the quantity column, users have the ability to adjust the number or remove the item from the basket. 

At the bottom users can see a summary of the cost broken down into Basket Total, Delivery cost and Grand Total, as well as buttons to continue to the secure checkout or keep shopping.

#### Secure Checkout
On the secure checkout page, users can view an order summary and enter their shipping and payment details. There is also a checkbox users can select to save their delivery details to their profile. This will enable faster payments in the future as delivery details will be pre-populated with their information. 

At the bottom, two buttons provide options to either 'adjust basket' or 'complete order' following which they will be directed to checkout success page notifying them that a confirmation email has been sent to their email address and detailing their order summary below. As indicated users should find a confirmation email in their inbox.  

The database is updated after checkout to deduct the products from the number in stock. 

#### Gin Cocktails
By navigating to the 'View Cocktails' page, users are presented with recipe results in the same bootstrap card format as the product results ensuring consistancy. They will see an image of the the cocktail and the recipe name below along with the number it serves and the tags. 

Users can click on the recipe image to view full details of the recipe including ingredients and the method. 

Logged in users will have the ability to add, edit and delete recipes of their own, thus enabling them to share their favourite gin recipes with other users. Store owners will have additional functionality to edit and delete any recipes that are added to the site regardless of who originally added the recipe. 

#### Gin Blog
Users can view a list of blog posts by click on the 'Blog Posts' menu in the navbar or the 'View Blog' button in the blog section on the home page. Results are listed in rows, with the blog image in a column tot he left and details of the post in a larger columm to the right. Users can read the first 50 words of the post and if they wish to read more they can click on the 'Read More' button to view the full blog post. 

Once a user has navigated to an individual blog post, they will be presented with the full article and a coments section below. Here they can read any comments left by other users about the article as well as leave comments of their own. Users must be looged in in order to leave a comment and logged in users will also have the ability to delete any comments that they have previously left. 

Additionally shop owners have the ability to add, edit and delete blog posts as well as delete any post comments regardless of who wrote them. This enables store owners to manage the blog and remove any inappropriate content from their site. 

#### My Account
Authentication and authorisation is implemeted here using the django Allauth package. 

Public users will click on the 'My Account' icon to find options to 'register' for or 'login' to an account. By clicking Register users are redirected to a sign up page containing a registration form requiring the following details:

* Email address
* Email address confirmation
* Username
* First Name
* Last Name
* Password 
* Password confirmation

Form validation is implemented to prevent users from omitting information or an invalid email address or password. If a password is too common or has less than 8 characters they will receive an error meesage. When a user successfully completes the registration form they will be redirected to a page requesting that they verify their email address by clicking on the link contained within their email to finalise the sign up process. 

The login page requires just a username / email and their passsword.

Once a user is logged in, they will find clicking on the 'My Account' provides options to access 'My Profile' or 'Logout'.  

#### My Profile
Registered users can view their profile by clicking on the link under My Account. The My Profile page includes the users login details, delivery information and order history. Here they can uchange their password and add or edit their default delivery information as well as see a list of all their previous orders. 

#### Messages
Messages have been implemented to provide feedback to the user when adding, editing or deleting products from the basket as well as when they add, edit or delete cocktail receipes or blog posts. Users will recive confirmation of a successful action or else be notified that an error has occured. 

#### Contact Form
The contact us page contains a short form for the user to fill in to send the shop owner an email. An Email address and message are the only fields required to contact the shop owner. Form validation has been applied to this so to ensure the form cannot be submitted if information is inclrrect or missing. 

#### Footer
Bootstrap Footer has been used to provide the user with links to the About Us, Contact Us, Privacy Policy and Terms and Conditions pages as well as the social medial links and copyright information. 

Every trustworthy online shop provides the legal documentation expected by the user on their site. Although these documents are a legal requirement of any online shop, including them also helps users to feel they can trust the outlet.

### Features Left to Implement

* Social Account - Giving users the ability to register and login via their social media account, thus streamlining the process. Additionally this will enable store owners to track users activity which will assist with email marketing and advertising.  

* Favourites - This would give logged in users the ability to add their favourite products to a 'wish list' which they can view, edit and delete. 

* Subscription Service - Users would be able to choose from a monthly, bi-monthly or quarterly subscription to a box of gin products delivered to their door. This would include a full sized bottle of the gin of the month, various mixers, garnish, snacks and recipes. This feature was originally intended for this project, but unfortunately had to be clipped from the current release due to time constraints.

* Additional payment methods - Allowing users to make payments with Paypal, apple pay or google pay. 

* Product rating - The average rating of a product is currently displayed as X/5 followed by 5 star icons. In a future release I would like the rating to be displayed by full, half or empty stars, for example a rating of 4/5 would be displayed as 4 full stars and one empty star. This is convention and is what the user would expect to see. It would also be more visually effective, enhancing user experience. 

* Staff Section - giving staff the ability to view all order information in one place, rather than having to visit the Stripe dashboard or admin panel. Functionality for this section might include an option to update an order as "shipped" in the database and an ability to handle cancellations and refunds.

## Technologies
All the languages, frameworks, libraries, and tools used to construct this project are listed below. I have also provided a relevant link and a brief overview of its usage.

### Languages
* <a target="_blank" href="https://en.wikipedia.org/wiki/HTML5">HTML5</a> – Used to write customised front-end content for the application.
* <a target="_blank" href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets">CSS3</a> – Used to customise the style of the web application. 
* <a target="_blank" href="https://en.wikipedia.org/wiki/JavaScript">JavaScript</a> - Used to add an onclick event to my cancel and return buttons within the application.
* <a target="_blank" href="https://www.python.org/">Python</a> - Used to build the back-end functionality.


### Frameworks
* <a target="_blank" href="https://getbootstrap.com/">Bootstrap v4.5.2</a> - A framework used to create the responsive grid system and various components within the site including the navbar, buttons and cards. 
* <a target="_blank" href="https://www.djangoproject.com">Django</a> - A python web framework used to construct and render pages within the application quickly and easily.


### Libraries
* <a target="_blank" href="https://jquery.com/">jQuery</a> - A JavaScript library used here to simplify DOM manipulation when initializing specific Bootstrap components within the application.
* <a target="_blank" href="https://fonts.google.com/">Google Fonts</a> – The font used was obtained from Google Fonts.
* <a target="_blank" href="https://fontawesome.com/">Font Awesome</a> - All icons used within the web application were sourced from Font Awesome.
* <a target="_blank" href="https://jinja.palletsprojects.com/en/2.11.x/">Jinja</a> - A templating language used to simplify the displaying of back-end data in a HTML markup format that is returned to the user via an HTTP response.
* <a target="_blank" href="https://api.mongodb.com/python/current/api/pymongo/index.html#module-pymongo">PyMongo</a> - A driver used to access the MongoDB database from Python and make communication between the two possible.


### Databases
* <a target="_blank" href="https://www.postgresql.org">PostgreSQL</a> - Used for production, provided by heroku.
* <a target="_blank" href="https://www.sqlite.org/index.html">SQlite3</a> - Used for development, provided by django.


### Tools 
* <a target="_blank" href="https://www.gitpod.io/">GitPod</a> – The online Integrated Development Environment (IDE) used for the development of this project.
* <a target="_blank" href="https://pip.pypa.io/en/stable/installing/">PIP</a> - For installation of tools needed in this project.
* <a target="_blank" href="https://django-crispy-forms.readthedocs.io/en/latest/">Django Crispy Forms</a> – to control the rendering behavior of Django forms in an elegant way.
* <a target="_blank" href="https://stripe.com">Stripe</a> – as payment platform to validate and accept credit card payments securely.
* <a target="_blank" href="https://travis-ci.org">Travis</a> – for continuous integration.
* <a target="_blank" href="https://aws.amazon.com">AWS S3 Bucket</a> – AWS S3 Bucket to store images entered into the database.
* <a target="_blank" href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html">Boto3</a> – to enable creation, configuration and management of AWS S3.
* <a target="_blank" href="https://pypi.org/project/django-heroku/">Django Heroku</a> – to ensure a seamless deployment and development experience.
* <a target="_blank" href="https://django-storages.readthedocs.io/en/latest/">Django Storages</a> – a collection of custom storage backends with django to work with boto3 and AWS S3.
* <a target="_blank" href="https://pypi.org/project/gunicorn/">Gunicorn</a> – WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
* <a target="_blank" href="https://pillow.readthedocs.io/en/stable/">Pillow</a> – as python imaging library to aid in processing image files to store in database.
* <a target="_blank" href="https://pypi.org/project/psycopg2/">Psycopg2</a> – as PostgreSQL database adapter for Python.
* <a target="_blank" href="https://www.google.co.uk/chrome/">Google Chrome</a> - This browser and its' developer tools were used throughout the development of the app. 
* <a target="_blank" href="https://www.google.co.uk/chrome/">Responsinator</a> - Website used to test responsiveness on different devices. 
* <a target="_blank" href="https://autoprefixer.github.io">Autoprefixer CSS Online</a> - Used to check for possible webkits required in the applications stylesheet ensuring Cross-browser support.
* <a target="_blank" href="https://github.com/">Git</a> – Used for version control
* <a target="_blank" href="https://github.com/">GitHub</a> – GitHub was used for hosting my repository
* <a target="_blank" href="https://github.com/">Heroku</a> – A cloud platform used for deployment
* <a target="_blank" href="https://validator.w3.org/">W3c Markup Validation Service</a> - The HTML code for this project was checked and validated by the W3c Markup Validation Service
* <a target="_blank" href="https://jigsaw.w3.org/css-validator/">W3c CSS Validation Service</a> - The CSS code for this project was checked and validated by the W3c CSS Validation Service


## Information Architecture

During development the project utilised the standard sqlite3 database installed with Django whilst on deployment it uses the PostgreSQL database provided by Heroku.

### Data Models

#### User
This project uses the standard User model provided by django.contrib.auth.models. Each user can:

* have one profile
* make numerous orders
* add numerous product reviews
* add numerous cocktail recipes
* add numerous blog posts
* add numerous post comments


#### Products App
This app has three models; Category, Product and Review which hold the data for the product itself, the product category and product reviews. The Product model uses a package called Pillow to store all image files in an AWS S3 bucket.

##### Category Model
Each category can link to numerous products but each product corresponds to just one category. 

| Name          | Key in DB     | Validation                            | Field Type |
|---------------|---------------|---------------------------------------|------------|
| Name          | name          | max_length=254                        | CharField  |
| Friendly Name | friendly_name | max_length=254, null=True, blank=True | CharField  |

##### Product Model
| Name         | Key in DB    | Validation                                       | Field Type                |
|--------------|--------------|--------------------------------------------------|---------------------------|
| Category     | category     | null=True, blank=True, on_delete=models.SET_NULL | ForeignKey to Category    |
| SKU          | sku          | max_length=254, null=True, blank=True            | CharField                 |
| Name         | name         | max_length=254                                   | CharField                 |
| Description  | description  |                                                  | TextField                 |
| Price        | price        | max_digits=6, decimal_places=2                   | DecimalField              |
| Image url    | image_url    | max_length=1024, null=True, blank=True           | URLField                  |
| Image        | image        | null=True, blank=True                            | ImageField                |
| Num in Stock | num_in_stock | validators=[MaxValueValidator(100)]              | PositiveSmallIntegerField |

##### Review Model
Each product can have numerous reviews but each review corresponds to just one product. 

| Name          | Key in DB     | Validation                                               | Field Type                |
|---------------|---------------|----------------------------------------------------------|---------------------------|
| Stars         | stars         | validators=[MaxValueValidator(5)], null=False, default=0 | PositiveSmallIntegerField |
| Title         | title         | max_length=100                                           | CharField                 |
| Review text   | review_text   |                                                          | TextField                 |
| Date Reviewed | date_reviewed | default=timezone.now                                     | DateTimeField             |
| User          | user          | on_delete=models.CASCADE                                 | ForeignKey to User        |
| Product       | product       | on_delete=models.CASCADE                                 | ForeignKey to Product     |


#### Checkout App
This app has two models; Order and OrderLineItem. An instance of the Order model is created before any OrderLineItems, as the OrderLineItem relies on the Order as a ForeignKey.

##### Order Model
| Name            | Key in DB       | Validation                                                              | Field Type                |
|-----------------|-----------------|-------------------------------------------------------------------------|---------------------------|
| Order Number    | order_number    | max_length=32, null=False, editable=False                               | CharField                 |
| User Profile    | user_profile    | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey to UserProfile |
| Full Name       | full_name       | max_length=50, null=False, blank=False                                  | CharField                 |
| Email           | email           | max_length=254, null=False, blank=False                                 | EmailField                |
| Phone number    | phone_number    | max_length=20, null=False, blank=False                                  | CharField                 |
| Country         | country         | blank_label='Country *', null=False, blank=False                        | CountryField              |
| Postcode        | postcode        | max_length=20, null=True, blank=True                                    | CharField                 |
| Town or city    | town_or_city    | max_length=40, null=False, blank=False                                  | CharField                 |
| Street address1 | street_address1 | max_length=80, null=False, blank=False                                  | CharField                 |
| Street address2 | street_address2 | max_length=80, null=False, blank=False                                  | CharField                 |
| County          | county          | max_length=80, null=False, blank=False                                  | CharField                 |
| Date            | date            | auto_now_add=True                                                       | DateTimeField             |
| Delivery cost   | delivery_cost   | max_digits=6, decimal_places=2, null=False, default=0                   | DecimalField              |
| Order total     | order_total     | max_digits=10, decimal_places=2, null=False, default=0                  | DecimalField              |
| Grand total     | grand_total     | max_digits=10, decimal_places=2, null=False, default=0                  | DecimalField              |
| Original basket | original_basket | null=False, blank=False, default=''                                     | TextField                 |
| Stripe pid      | stripe_pid      | max_length=254, null=False, blank=False, default=''                     | CharField                 |

##### OrderLineItem Model
An instance of OrderLineItem is created for each unique product in the users basket. It links to the users existing Order, the relevant product and the quantity the user wishes to buy.

| Name            | Key in DB      | Validation                                                                  | Field Type            |
|-----------------|----------------|-----------------------------------------------------------------------------|-----------------------|
| Order           | order          | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | ForeignKey to Order   |
| Product         | product        | null=False, blank=False, on_delete=models.CASCADE                           | ForeignKey to Product |
| Quantity        | quantity       | null=False, blank=False, default=0                                          | IntegerField          |
| Line Item Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False     | DecimalField          |


#### Profiles App
This app has one model; UserProfile. Each user can have one profile and each profile links to one user. 

##### UserProfile Model
| Name                    | Key in DB               | Validation                                   | Field Type    |
|-------------------------|-------------------------|----------------------------------------------|---------------|
| User                    | user                    | on_delete=models.CASCADE                     | OneToOneField |
| Default street address1 | default_street_address1 | max_length=80, null=True, blank=True         | CharField     |
| Default street address2 | default_street_address2 | max_length=80, null=True, blank=True         | CharField     |
| Default town or city    | default_town_or_city    | max_length=40, null=True, blank=True         | CharField     |
| Default county          | default_county          | max_length=80, null=True, blank=True         | CharField     |
| Default postcode        | default_postcode        | max_length=20, null=True, blank=True         | CharField     |
| Default country         | default_country         | blank_label='Country', null=True, blank=True | CountryField  |
| Default phone number    | default_phone_number    | max_length=20, null=True, blank=True         | CharField     |


#### Cocktails App
This app has one model; CocktailRecipe, which stores all the recipe data.  

##### CocktailRecipe Model
| Name           | Key in DB      | Validation                                  | Field Type                |
|----------------|----------------|---------------------------------------------|---------------------------|
| Name           | name           | max_length=200                              | CharField                 |
| Serves         | serves         | blank=False, default=1                      | PositiveSmallIntegerField |
| Ingredients    | ingredients    | blank=False                                 | TextField                 |
| Method         | method         | blank=False                                 | TextField                 |
| Tag            | tag            | max_length=30, blank=True, null=True        | CharField                 |
| Image          | image          | blank=True, null=True                       | ImageField                |
| Published date | published_date | blank=True, null=True, default=timezone.now | DateTimeField             |
| User           | user           | on_delete=models.CASCADE                    | ForeignKey to User        |


#### Blog App
This app has two models; Post and PostComments. The Post model stores all the data required for a blog post whilst the PostComment model stores the data of any comments left by users. 

##### Post Model
Each blog post can have several comments whist comments correspond to a single post. 

| Name           | Key in DB      | Validation                                  | Field Type    |
|----------------|----------------|---------------------------------------------|---------------|
| Title          | title          | max_length=200                              | CharField     |
| Content        | content        |                                             | TextField     |
| Create date    | create_date    | auto_now_add=True                           | DateTimeField |
| Published date | published_date | blank=True, null=True, default=timezone.now | DateTimeField |
| Views          | views          | default=0                                   | IntegerField  |
| Tag            | tag            | bmax_length=30, blank=True, null=True       | CharField     |
| Image          | image          | blank=True, null=True                       | ImageField    |

##### PostComment Model
| Name           | Key in DB      | Validation               | Field Type         |
|----------------|----------------|--------------------------|--------------------|
| Comment detail | comment_detail | max_length=200           | TextField          |
| Date commented | date_commented | default=timezone.now     | DateTimeField      |
| User           | user           | on_delete=models.CASCADE | ForeignKey to User |
| Post           | post           | on_delete=models.CASCADE | ForeignKey to Post |


## Testing
GitPod's preview, google chrome developer tools, Safari developer tools and [responsinator](https://www.responsinator.com/) were utilised throughout the development of the project to identify and successfully address any bugs, errors or style issues affecting UX on various screen resolutions. 

### Automated Testing
[W3c Markup](https://validator.w3.org/), [CSS Validation Services](https://jigsaw.w3.org/css-validator/) and [PEP8 online](http://pep8online.com) were used to check the validity of my HTML, CSS and python code.  However, the W3c validator throws errors in the HTML files where Jinja templating syntax is found. All other code returned fine. 

### Travis
Travis was used throughout the development of this project to provide continuous integration with the deployed site. The Travis Documentation provides all the info needed to set it up.

### Manual Testing
After the site was deployed, I tested it across various browsers including Chrome, Safari, Internet Explorer, FireFox, and on multiple devices (Samsung Galaxy J3, iPhone 7, 8, 11 pro, iPad 3, iPad Air, MacBook Air and iMac) as well as on Responsinator to ensure compatibility and responsiveness. Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected.

#### Elements on every page
##### Navbar
* Confirm that the navbar displays the Brand Name to top left, the 'Search', 'My Account' and 'Basket' icons to the top right and the dropdown menu links for "Gin Shop', 'Gin Cocktails' and 'Gin Blog' in a row below. 
* Confirm that the navbar displays the toggler / burger icon to top left, icons links to 'Search', 'My Account' and 'Basket' to the top right. 
* Click on the 'Search' icon and confirm that the search bar appears below.
* Confirm that the 'My Account' dropdown options "Register" and "Login" are visible to public users and that "My Profile" and "Logout" are not.
* Log into the site, confirm that options "Account" and "Log out" are visible and that "Register" and "Log in" are not.
* Add an item to the shopping basket, confirm that the icon changes colour and the basket grand total is displayed below. 
* Click on the basket icon and confirm that it leads you to the Shopping Basket page
* Click the "Gin Shop" link in the navbar, confirm that 'Gin', 'Mixers', Accessories' and 'All Products' are listed in the dropdown menu.
* Login as a superuser, click the "Gin Shop" link in the navbar and confirm that 'Add Product' is also listed in the dropdown menu.
* Logout, click on the "Gin Cocktails" link in the navbar and confirm that only 'View Cocktails' is listed in the dropdown menu.
* Login, click on the "Gin Cocktails" link in the navbar and confirm that both 'View Cocktails' and 'Add Recipe' are listed in the dropdown menu.
* Logout, click on the "Gin Blog" link in the navbar and confirm that only 'View Blog' is listed in the dropdown menu.
* Login as superuser, click on the "Gin Blog" link in the navbar and confirm that 'Blog Posts' and 'Add Blog Post' are listed in the dropdown menu.
* Click each link in the navbar to confirm that it leads to the correct page.

##### Footer
* Confirm Footer displays three headings; 'Gin Shed', 'Our Policies' and 'Follow Us' along with their relavent links. 
* Hover over links in the footer, confirm the color change animation works as expected.
* Click all links in the footer, confirm that they take the user to the relevant pages within the site.
* Click the social media icons, confirm that it opens a new tab and takes the user to relevant social media login page.
* Check date of copyright information, confirm year displayed matches the current year.

#### Home Page
* Confirm Home Page loads as expected
* Hover over call to action buttons and confirm the color changes as expected.
* Click on the 'Shop Now' button and confirm that it leads to the product results page
* Click on the 'View Cocktails' button and confirm that it leads to the cocktails results page
* Click on the 'View Blog' button and confirm that it leads to the blog results page

#### About Us Page
* Go to About Us page, confirm that the Page title, subheading and text are display in container to the centre as expected.
* Check that the background image is displayed as expected.

#### Contact Us Page
* Navigate to the contact page and confirm that the contact form is laid out as expected.
* Hover over the form and confirm that opacity changes as expected. 
* Try to send the form with no fields filled in, confirm that the user is alerted to fill in the required fields.
* Try to enter a non-email address into the email field, confirm that the user is alerted to fill in an email address.
* Send a complete valid form, confirm that the message is sent to my email address with all the information included.

#### Terms and Conditions Page
* Check that the page loads and displays as expected. Confirm that the links in the text work as needed.

#### Privacy Policy Page
* Check that the page loads and displays as expected. Confirm that the links in the text work as needed.

#### Register Page
* Try to go to the register url when already logged in, confirm that the user is redirected to the home page.
* Logout then go to the register page again. Confirm that the register form is displayed as expected.
* Fill in the form with a username already in the database, confirm that the user is informed that they must use a unique username.
* Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
* Fill in the form with two different emails, confirm the error is caught and the user is informed of their mistake.
* Fill in the form with two different passwords, confirm the error is caught and the user is informed of their mistake.
* Fill in the registration for correctly, confirm that the user is automatically directed to the verify email page.

#### Login Page
* Attempt to login with a username not in the database, confirm the relevant error message is shown.
* Attempt to login with a correct username but wrong password, confirm the relevant error message is shown.
* Login with a correct username and password, confirm that the user is logged in and that they are redirected to the home page.
* Try to return to the login page url when already logged in, confirm that the user is redirected to the home page.

#### Logout Page
* Click the 'Logout' link and confirm that it leads to the signout page.
* Click 'Signout' button and confirm that the user is logged out of their account
* Login again and add a new product to the shopping basket. Logout and confirm that the user is logged out and their basket has been cleared.

#### Add Product Page
* Logout then attempt to navigate to the add product url and confirm that user is redirected to login page. 
* Login in to an account without superuser status, attempt to navigate to the add product url and confirm that error message is displayed alerting user that they are not authorised. 
* Login as a superuser and navigate to the add product page. Confirm that the product form and background image display as expected. 
* Hover over the form and confirm that the opacity changes as expected. 
* Click on the category field and check all product categories are listed. 
* Click on the select image button and confirm it works as expected. 
* Attempt to submit form without completing required fields and confirm validation errors. 
* Complete form correctly. Confirm success message displayed and user redirected to the new product detail page. Check details are listed correctly. 

#### Product Results Page
* Navigate to the 'All Products' page and confirm that category buttons are listed under the Product Heading and that Gin, Mixers and Accessories products are displaying in the results.
* Confirm that products image and details are displaying as expected, with the details underneath the image. 
* Confirm that where there is an average rating it is displayed or else the text 'no rating' is displayed. 
* On desktop view, confirm that there are four products listed in a row and that rows are separated with a horizontal rule
* Confirm that the number of products listed in each row reduces as the screen size gets smaller, first down to three products per row, then two and finally one product per row on mobile views. 
* Check that there are no duplicates or missing products.  
* Login as a superuser and confirm that the 'Edit' and 'Delete' links are displaying. Click the edit link and confirm that the edit product page is displayed. 
* Select the different sorting options from the menu one by one, confirm that the products are sorted in the order selected.
* Click the product category buttons at the top of the 'All Products' page and confirm that product results are filtered to the desired category. 
* Select a category from the Gin Shop dropdown menu in the navbar and confirm that product results are filtered to the desired category.
* Hover over a product image and confirm that the curser changes to a pointer. 
* Click on product images and confirm that it redirects to that specific product detail page. 

#### Product Detail Page
* Navigate to a product detail page and confirm that the page is displayed as expected. On desktop image should be displayed on left and product info on the right, whilst on mobile view the image is stacked on top of the product info. 
* Confirm that the Image, name, price, category, rating and description match those in the database for the product.
* Adjust the quantity using the button and confirm that the highest number available to select matches the number in stock of this product.
* Confirm that the 'Keep Shopping' and 'Add to Basket' buttons work as expected. 
* Attempt to type in a quantity above the number in stock, press enter or 'Add to Basket' and confirm that validation message is received.
* Click the "add to basket" button. Confirm that the success message is launched, stating the name and quantity of the product added.
* Confirm that the success message provides a button to 'go to view basket'. Click to confirm it operates as expected.
* Add more of the same product to the basket, making the total quantity go over the max number in stock. Confirm that an error message alerts the user that there is not enough in stock and resets the value to 1. 
##### Reviews section
* Under the product details confirm that the reviews section is displaying any previous reviews or else the text 'No reviews'. 
* Confirm that the 'write review' form is displayed for logged in users and a message "Please Register or login to leave a review." is displayed if user is not logged in. 
* Confirm that the 'register' and 'login' links work as expected. 
* Once logged in, hover over the stars in the review form and confirm that they change colour as expected.
* Click the desired number of stars and confirm that the that number of stars have changed colour. 
* Try to submit the form with the title and review fields empty and confirm validation errors
* Complete the form correctly, click post and confirm that success message is displayed and review is now listed. Also confirm product rating has updated. 

#### Edit Product Page
* Logout, then attempt to navigate to the edit product url and confirm that user is redirected to login page. 
* Login to an account without superuser status, then attempt to navigate to the edit product url and confirm that error message is displayed alerting user that they are not authorised. 
* Login as a superuser and navigate to the edit product page. Confirm that the edit product form and background image display as expected, with the fields pre-populated with the specified product.
* Hover over the form and confirm that the opacity changes as expected. 
* Select new image, save and confirm image has been updated.
* Click to remove the image, save and confirm the image has been removed and the 'no image' pic is displayed instead. 
* Remove data from a required field, attempt to save it and confirm validation errors.
* Edit and complete form correctly. Confirm success message displayed and user redirected to the updated product detail page. Check product details are listed correctly. 

#### Shopping Basket Page
* Go to the shopping basket page with nothing added, confirm "Your basket is empty" message and 'keep shopping' button redirects to product results.
* Add items to the basket and return to the shopping basket page, confirm that all items in the basket are displayed correctly, with the correct amounts requested by the user.
* Confirm that the basket total, delivery and grand total are displaying the correct amount. 
* Adjust the quantity field, confirm that the shopping basket subtotal is updated to reflect the change.
* Adjust the quantity field up higher than the number of that item in stock. Confirm that a modal alerts the user to the maximum number available and adjust the basket to reflect that amount.
* Click the remove link on a item, confirm that the basket is reloaded with that item removed.
* Remove all items from the basket, confirm that the shopping basket page is reloaded to reflect the empty basket.

#### Secure Checkout Page
* Navigate to the checkout page url without anything in the basket. Confirm that the user is redirected to the product results page and error message appears notifying user that basket is empty.
* Navigate to the checkout page url with items in the basket. On desktop view, confirm that the Details, Delivery and Payment form are displayed on the left and order summary on the right. On mobile view confirm that the order summary is diaplayed first and that the form is stacked underneath. 
* Confirm Order Summary is diaplaying correctly
* Click the 'Adjust Basket' button and confirm taht it redirects to the shopping basket page.
* Try to send the form without all the required fields filled in. Confirm that the appropriate error message is given to the user.
* Use the stripe checkout test card numbers to check the various responses to different errors.
* Complete order and confirm that user is directed to the Checkout Success page, detailing their order information. Click the "keep shopping" button, confirm that the user is taken back to the product results page.

#### Profile Page
* Go to the profile page of a newly created user. On desktop, confirm that the page loads with the forms on the left and Order History on the right. On mobile confirm that forms are stacked on top of the order history. 
* Confirm logon details form is populated with the users username and email address. 
* Confirm that password field contains asterisks and 'Edit' button. Click button and confirm that user is taken to change password page. 
* Attempt to change password using wrong password and confirm validation messgae.
* Create new password using less than 8 characters and confirm validation message. 
* Create new password similar to username and confirm validation message.
* Complete change password form as required and confirm success message received. 
* Fill in the My Delivery Information form and click update. Confirm that "Profile updated successfully" success message is shown to the user and that the reloaded form is now populated with the new data.
* Confirm that a user with no previous orders has no orders displayed in the Orders section.
* Make an order on the website, return to the profile page and confirm that the orders are displayed in date order the Order History section. Click on the order number to show the full details.
* Confirm that all data in the orders on the profile page are accurate.

#### Add Cocktail Recipe Page
* Logout then attempt to navigate to the add cocktail recipe url and confirm that user is redirected to login page. 
* Login and navigate to the add recipe page. Confirm that the recipe form and background image display as expected.
* Hover over the form and confirm that the opacity changes as expected. 
* Attempt to submit form without completing required fields and confirm validation errors.
* Click on the select image button and confirm it works as expected. 
* Complete form correctly. Confirm success message displayed and user redirected to the new recipe page. Check recipe details are listed correctly. 

#### Cocktail Results Page
* Navigate to the 'View Recipes' page and confirm that recipe results are displaying as expected, with the recipe details underneath the image. 
* On desktop view, confirm that there are four recipes listed in a row and that rows are separated with a horizontal rule.
* Confirm that the number of recipes listed in each row reduces as the screen size gets smaller, first down to three recipes per row, then two and finally one recipe per row on mobile views. 
* Check that there are no duplicates or missing recipes.  
* Login in and add a recipe. View recipe results page and confirm that the 'Edit' and 'Delete' links are displaying for the recipe you added. Click the edit link and confirm that the edit recipe page is displayed. 
* Login as a superuser and confirm that the 'Edit' and 'Delete' links are displaying for all recipes. Click the edit link and confirm that the edit recipe page is displayed. 
* Hover over a recipe image and confirm that the curser changes to a pointer. 
* Click on multiple recipe images and confirm that it redirects to that specific recipe page. 

#### Cocktail Recipe Detail Page
* Navigate to a recipe detail page and confirm that the page is displayed as expected. On desktop image should be displayed on left and recipe info on the right, whilst on mobile view the image is stacked on top of the recipe info. 
* Confirm that the details match those in the database for the cocktail recipe.
* Login in and add a recipe. View that particular cocktail recipe page and confirm that the 'Edit' and 'Delete' links are displaying. Click the edit link and confirm that the edit recipe page is displayed. 
* Click the delete link and confirm that a success message is displayed and the recipe is now gone from the recipe results. 
* Confirm that the 'Back to receipes' button work as expected.

#### Edit Cocktail Recipe Page
* Logout then attempt to navigate to the edit cocktail recipe url and confirm that user is redirected to login page. 
* Login and navigate to the edit recipe page. Confirm that the recipe form and background image display as expected, with the fields pre-populated with the specified recipe.
* Hover over the form and confirm that the opacity changes as expected. 
* Select a new image, save and confirm image has been updated.
* Click to remove the image, save and confirm the image has been removed and the 'no image' pic is displayed instead. 
* Remove data from a required field, attempt to save it and confirm validation errors.
* Complete form correctly. Confirm success message displayed and user redirected to the updated recipe page. Check recipe details are listed correctly. 

#### Add Blog Post Page
* Logout then attempt to navigate to the add blog post url and confirm that user is redirected to login page. 
* Login to an account without superuser status, attempt to navigate to the add blog post url and confirm that error message is displayed alerting user that they are not authorised. 
* Login as a superuser and navigate to the add blog post page. Confirm that the blog post form and background image display as expected.
* Hover over the form and confirm that the opacity changes as expected. 
* Confirm published date is pre-populated with the current date and time. 
* Attempt to submit form without completing required fields and confirm validation errors. 
* Click on the select image button and confirm it works as expected. 
* Complete form correctly. Confirm success message displayed and user redirected to the new blog post page. Check post details are listed correctly. 

#### Blog Results Page
* Navigate to the 'Blog Posts' page and confirm that all blog posts are displaying as expected, with the blog image to the left and details to the right on larger screens and the details underneath the image on mobiles.   
* Check that there are no duplicates or missing blog posts.  
* Click on the 'read more' buttons and confirm that it redirects to that specific blog post page. 

#### Blog Post Detail Page
* Navigate to a blog post detail page and confirm that the page is displayed as expected. Image should be displayed at the top, the publish date, views and tags listed underneath and then the post below that.
* Confirm that the details match those in the database for the blog post.
* Login as a superuser and confirm that the 'Edit' and 'Delete' links are displaying for all blog posts. Click the edit link and confirm that the edit blog page is displayed. 
* Click the delete link and confirm that a success message is displayed and the blog post is now gone from the results page. 
* Confirm that the 'Back to blog' button work as expected. 
###### Blog Post Comments
* Under the blog Post, confirm that the comments section is displaying any previous comments or else the text 'No comments'. 
* Confirm that the 'add a comment' form is displayed for logged in users or else a message saying "Please Register or login to leave a comment" is displayed if user is not logged in. 
* Confirm that the 'register' and 'login' links work as expected. 
* Try to submit an empty form and confirm validation errors
* Complete the form, click post and confirm that success message is displayed and comment is now listed.

#### Edit Blog Post Page
* Logout, then attempt to navigate to the edit blog post url and confirm that user is redirected to login page. 
* Login to an account without superuser status, then attempt to navigate to the edit blog post url and confirm that error message is displayed alerting user that they are not authorised. 
* Login as a superuser and navigate to the edit blog post page. Confirm that the blog post form and background image display as expected, with the fields pre-populated with the specified blog post.
* Hover over the form and confirm that the opacity changes as expected. 
* Select new image, save and confirm image has been updated.
* Click to remove the image, save and confirm the image has been removed and the 'no image' pic is displayed instead. 
* Remove data from a required field, attempt to save it and confirm validation errors.
* Edit and complete form correctly. Confirm success message displayed and user redirected to the updated blog post page. Check post details are listed correctly. 

### User scenarios


### Bugs


## Deployment
Before starting you must have Git, PIP and Python3 installed on your machine. You will also need to ensure you have created free accounts with the following services: [Stripe](https://dashboard.stripe.com/register), [AWS](https://aws.amazon.com) including setting up an [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html). Please click the links for documentation on how to set these up and retrieve the necessary environment variables.

### To run the project locally

1. Go to [my GitHub repository](https://github.com/Carly07/the_gin_shed) and click on the green 'Code' button at top right of the repository and copy the URL for the repository in the 'Clone with HTTPs' section.

2. Now open your prefered Integrated Development Environment (I used GitPod for this project) and with Git installed on your system, you can clone the repository with the following command in the terminal.

`git clone https://github.com/Carly07/the_gin_shed`

3. If needed, Upgrade pip locally with
`pip install --upgrade pip`

4. Install all required modules with the command
`pip -r requirements.txt`

5. Set up the environment variables within your IDE by creating an env.py file and entering the environment variables listed below:

SECRET_KEY= "<enter_your_secret_key>"
STRIPE_PUBLIC_KEY= "<enter_your_secret_key>"
STRIPE_SECRET_KEY= "<enter_your_secret_key>"
STRIPE_WH_SECRET= "<enter_your_secret_key>"

Ensure the env.py is living in the root of your project directory and then add it to .gitignore to ensure your secret details aren't exposed. Then restart your machine to activate your environment variables or your code will not be able to see them.

6. Migrate the admin panel models to create your database template with the terminal command:
`python manage.py migrate`

7. Create your superuser to access the django admin panel and database with the following command:
`python manage.py createsuperuser`
and then follow the steps to add your admin username and password

8. Run the following command in the terminal to launch the Django project:
`python3 manage.py runserver`
Click the URL link that appears and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.

9. Once the application is running in a browser, add /admin to the end of the url and log in to the admin panel with your superuser account.  

10. Create instances of Products, Cocktails and Blog Posts within the new database so the local site runs as expected. 

### Deploying to Heroku
Having followed the steps above to run the project locally, you can then deployed the project to Heroku for hosting. In order to achieve this, follow the step below: 

1. Create a new app on the [Heroku website](https://id.heroku.com/login) by clicking the 'New' button on dashboard. Give the app a name and set the region to that nearest to you. 

2. Then, select the 'Resources' tab on the Heroku dashboard, search for Heroku Postgres in the 'Add-Ons' section and select the free Hobby level.

3. From the heroku dashboard, click on 'Settings' > 'Reveal Config Vars' and then add the following config vars:

| Key | Value |
| ----- | ------- |
| AWS_ACCESS_KEY_ID | <"your secret key"> |
| AWS_SECRET_ACCESS_KEY | <"your secret key"> |
| DATABASE_URL | <"your postgres database url"> |
| EMAIL_HOST_PASS | <"your secret key"> |
| EMAIL_HOST_USER | <"email address"> |
| SECRET_KEY | <"your secret key"> |
| STRIPE_PUBLIC_KEY | <"your secret key"> |
| STRIPE_SECRET_KEY | <"your secret key"> |
| STRIPE_WH_SECRET | <"your secret key"> |
| USE_AWS | True |

4. Migrate the database models using the command `python3 manage.py migrate` in the terminal.

5. Create a superuser using the command `python3 manage.py createsuperuser` and entering a username and password.

6. Create a `Procfile` file  with the command `echo web: python app.py > Procfile`

7. Commit the code to a local Git repository using the `git add` and `git commit -m 'message'` commands. 

8. Push the code to the [GitHub repository](https://github.com/Carly07/the_gin_shed) using `git push`, initalise the heroku repository using `heroku git:remote -a your_app_name` and then push to Heroku using `git push heroku master`.

9. From the heroku dashboard click on 'Deploy' > "Deployment method" and select GitHub, ensuring you confirm the correct GitHub repository and then select 'Enable Automatic Deploys'. 

10. Once the app has finished building, click the 'Open App' button provided.

11. Add /admin to the end of the website url, log in to the admin panel with your superuser account and then create instances of Products, Cocktails and Blog Posts within the new database to the site runs as expected. 


## Credits

### Content
* The product images and detail were taken from craft [Craft Gins](https://craftgins.co.uk/).
* All the cocktail recipes including the images used within this site were sourced from [BBC Good Food](https://www.bbcgoodfood.com/). 
* The blog posts were taken from a book called, The Bartender's Guide to Gin.
* Terms and conditions template was provided by <a target="_blank" href="https://www.nibusinessinfo.co.uk/content/sample-website-terms-and-conditions-use">NIBusinessInfo.co.uk</a>
* Example privacy policy was provided by <a target="_blank" href="https://gdpr.eu/privacy-notice/">GDPR.EU</a>

### Media
* All other photographs used throughout this site were found on [Google Images](https://www.google.com/imghp?hl=en).

### Acknowledgements

This YouTube video tutorial,  <a target="_blank" href="https://www.youtube.com/watch?v=4mfPjGb6y84">CSS Star Rating System - No JavaScript by UM Tutorial</a> was used to create the CSS Star Review system for this project. 

I have also made use of a number of websites in my pursuit to wire the all the functions necessary for this app, but particularly
* [Stack Overlflow](https://stackoverflow.com/)
* [W3School](https://www.w3schools.com/)

Finally a special thanks to my mentor, Antonio Rodriguez, the tutors at Code Institute and the Stack community for their help and advice with this project.

**This is for educational use.** 