#Euva
An journal writing web app that uses sentimental analysis to analyze journal entries over time.
<p align="center">
  <img src="https://github.com/sohan-py/Euva/blob/main/static/images/app/app.svg">
</p>

## Inspiration
A lot of times, we write journal entries about things that stood out to us during our day. Unfortunately, reflecting back on them after a while is difficult, because it requires us to reread what we wrote a while back. With this as my motive, I have created Euva, a journal app that allows users to reflect on their emotional behavior over a period of time.

## What it does
### 100% Confidential ― Write In Private
Your journals, your privacy. Euva requires users to login with a Google Account to strengthen account protection. 
Journals are also saved in an encrypted format, so not only will getting hands on them be a problem, but so will comprehending them.

### Not Just A Text Editor ― It's A Block Editor
While typing in a plain text editor can be boring, Euva offers an intuitive block editor. Block editors allow users to create and organize sections within an entry. Additionally, they allow users to move, edit, and delete blocks easily.

### Sentimental Analysis Charts
Upon saving a journal, Euva uses a sentimental artificial intelligence model to determine the overall sentiment of your day. Afterwards, Euva displays its predictions on an interactive doughnut chart.

### Sentimental Scores Tracked Over Time
Over time, Euva saves sentimental progress from a user and displays it on an interactive graph allowing the user to reflect on their emotional progress over a period of time. Euva allows users to analyze graphs with a line graph and bar chart.

## How I built it
I used Python3 as my backend language and connected it to my frontend using Flask. To build my user interface, I used HTML, CSS, Javascript, and Jinja.  I used Bootstrap.css to quickly make user friendly components. To create interactive graphs such as the line graph, bar chart, and doughnut chart, I used the Chartjs Javascript framework. For building a block editor, I use the Editorjs Javascript framework and I styled it using my own CSS.  I used Google's service account API to allow users to login with a one click sign in with Google.  In addition, logging in with Google strengthens account protection.  I saved user information and journal entries in an encrypted format into a MYSQL database.  Finally, to perform sentimental analysis upon journal entries, I used a transformers based neural network.

## Challenges I ran into
I am not a frontend expert, so while creating this project I ran into many issues.  Many of these issues involved styling my website with CSS.  There were times when I was frustrated that components didn't look the way I imagined them to look like.  Other times, components didn't align properly and they were randomly positioned.  Apart from CSS, I also had some troubles with Javascript.  I wanted to use my Flask server as a REST API for my Javascript to be able to access, but there was always some error that came upon trying to do so.  After a long time, I found a stackoverflow solution that told my to turn of CORS on my Flask app and I was able to use my Flask app as a REST API and my Javascript was able to access it.

## Accomplishments that I'm proud of
While making this project, there are many things I believe I have accomplished.  For starters, I was able to create a full stack application while using many frameworks and languages.  I am also proud of the UI I built for this application and the color combination I chose.  I am also proud of how I was able to use Flask and its features.  In addition, I believe that while building this project, I gained lots of experience with handling data with MYSQL.

## What I learned
Building this project taught me lots of things.  I learned a lot about frontend development and CSS.  In addition, I learned how to use Chartjs and Editorjs to build interactive components.  This app was also the first time I used the Google service account API to validate users, so learning how to do that was also fun.  I also learned more about Flask and neural networks in this project.  This project was the first time I touched the concept of neural networks, so doing so taught me a lot about them.  Finally, I improved my Python and MYSQL skills upon building this project.

## What's next for Euva
Eventually, I hope to host Euva live on the internet for people to use.  I really hope you enjoyed my project and please let me know what you thought of it in the comments below.
