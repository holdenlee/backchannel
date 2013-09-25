Backchannel
===========

Backchannel for online lectures -- A simple customizable interface that has a video (possibly from YouTube) on one side and a list of questions and comments that people have about the video on the other side. At any time, a watcher can pause the video and type a question or comment, and it will be arranged chronologically in the document, with the video’s time stamp. People can upvote and downvote questions and comments.

This is a vast improvement over online lectures with no interactivity, and addresses several concerns over the “online lecture”-ification of classes as well as flipped classrooms: specifically, students cannot ask questions in real-time, and hence there is no personalization of the lecture, and no ability to go on interesting tangents. However, neither does in-person lecture accomplish this completely because there are too many people and one instructor. Now students get to ask ALL their questions, in a time-specific manner, and a teacher can address them during class (or by commenting on the questions). This also provides the instructor with very specific feedback to improve the online lecture.

I imagine that someone could turn a YouTube video into a commentable video in this sense just by dropping a YouTube link at the website, possibly setting a password for students. This immediately makes the existing wealth of educational videos available vastly more powerful.

This extends to other media besides videos. What if we did the same for every major textbook, ordered by page number? Reading a textbook no longer has to be a very independent activity; you could be connected to the corpus of all questions and ideas that other people have had while reading the textbook. A reading group’s best friend!

(Note: I am actually implementing this for readings first because it doesn't involve embedding video.)

Tags: #education #<->Piazza #<->TodaysMeet #<->Concrete Mathematics, Graham, Patashnik, Knuth (one of my favorite math books; they incorporated class comments into the margins of their textbook) ~holden1@mit.edu 

Current progress
----------------
Right now you can log in, add a comment, filter comments, and edit your comments. There is voting but votes are not linked to the user.
Backchannel refreshes every 2 seconds.

Currently the project uses SQLite 3.

TODO:
* Display tags.
* Display from x to y, and at most n entries.
* Be able to respond to comments.
* Make categories for comments.
* Make a database from a text file.
* Associate users with votes.
* Implement multiple "circles" for different videos/readings. Give users permissions.
* Embed YouTube video and extract time
* Allow users to choose a color, and have their comments show up with that color background.
* Make a nice GUI.
* Allow a teacher to choose video link.
* Move to MySQL.

BUG: Sometimes the left pane will vanish when you change the database by clicking a link.

Configuration
-------------
Change backchannel/settings.py:

    'NAME': '<file path>/database.db'

First make the database:

    python manage.py syncdb

Then run the server:

    python manage.py runserver

Admin: Go to http://localhost:8000/admin/
Go to http://localhost:8000/comments/ to play around.

