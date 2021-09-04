# Tell ME what to EAt
#### Video Demo:  https://www.youtube.com/watch?v=DSYacJm9cnQ
#### Description:
Have you ever feel troubled to decide what to eat next, already get tired to the food you eat everyday and wanna try something new?
Yes! That's what we do, we help users to find out what to eat by taking a simple quiz. This webpage has included using python, html, css, sql, and flask.
This project is using the same html template with the problem set 8 finance and I have made some change on it.
I do a lot of research about the way to generate the most suitable food for according to the user preference.

#### Reason of doing this project
-In this modern era, more people are not willing to spend time on their meals. I hope through my project people can pay more attention to their meals, spend a little more time when you deciding what to eat.

-For me, food is the bridge linking different people from different culture, and I am willing to try different food from all around the world.

#### Explaining the project
-This website is basically help user to make a decision on what should eat. I used Flask web framework based in Python and flask-sqlalchemy for manage SQL database with sqlite. At the homepage, the user need to click the "Go" button to start. Next user need to answer four quizs about very simple daily question.According to different combination the user choose, the website will suggest the most suitable meal for the user.

-I used 6 columns in food.db database, which are id, food, price, special, type and portion, to specify different features of the food. I have added 50 different foods, into the database, from diffrent cuisine, different price range, and different portion of food.

-If the user does not like the selected food, user can click the "Try again" button to stat over.

-There are two folder in my project, the first project name static containc three document: hungry.png, style.css, sucks to be you.jpg. The hungry.png is the logo of this website, and sucks to be you.jpg is a picture that will redirect to if user cannot find a sastified food for his meal. The style.css is the css for the whole website.

-The second folder is template, it contains 6 html documents: apology.html, index.html, layout.html, quiz.html, result.html and stby.html.

-The apology.html contain a photo of cat it appear when the webpage goes wrong, or the user did not answer all the four quizzes.

-index.html is the hoomepage of the website, it contain a simple instruction for the user and a "go" button.

-layout.html is a the general general frame for other webpages, it contains the header and footer of the webpages.

-quiz.html contains the quizzes need to be answer by user. There are four questions in total and ech question have three selections, it also contain a "submit" at the bottom to submit the answers.

-result.html contains the result to be shown to the users, and also a "try again" that will redirect to the quiz in case the user does not like the suggestion. At the button there is a button redirect to stby.html.

-stby.html contains a picture of spongebob.

-The application.py is the main flask python documentation of whole website.

-The helpers.py contain only the apology function provided by CS50.

-And the README.md is this what you looking at.

#### Obstacles
-The biggest obstacle I faced is to decide how to randomly select the food for the user. I try to import random in python and use random fuction but it did not work well, thefore I replace it with adding random in the db.execute SELECt function.

#### About CS50x
-CS50x was the first time I step into the domain of computer science and frankly it was a quite big challange for me. Anyway, I look forward to continue in this path and take some other course in future.
