# recursive_url_crawler

Python2.7 based recursive URL crawler which users `urllib2` and `beautifulsoup`
to extract information from a URL, store it in an `.html` file and then extract
URL from it and repeat the process on all the urls returned.

# Questions: 

- How to run the programme
- How are the source files organized? Where can we begin to read the code and how to navigate through it?
- What resources did you use to do research for this project?
- What development tools did you do use to complete the project?
- How did you test & debug the project?
- What other features can you think of that will enhance the program?
- Please mention the dependencies and relevant commands/ steps to install the same.

# Answers (in same order): 
1.) It's a single file program. One can run it on any Python Interpreter. I have designed it using Python2.7.
       So if you are using Unix, it's already installed in the system. Please repeat the following steps to run it :
     - Unzip the file.
     - There are two files. Easy_understand.py and Parser.py. Although both does the same job but easy_understand.py is made in         such a way that it'll help developers see what's going on in the backend. It has a lot of comments and print statements to               show execution of program. On the other hand "Parse.py" is following industrial standard. It won't show any output but will           create Unique files in your system with the response code.
     -  To execute any of files, run:
           $ python Parser.py  or $ python easy_understand.py (without "$" sign)

2.)  As I mentioned, There is only one file to run. Proper Documentation is provided to help anyone understand the code even if the person is not familiar with Python.

3.)  The resources I used are:
           https://www.quora.com/Can-you-make-Scrapy-keep-all-the-HTML-it-downloads
           https://www.crummy.com/software/BeautifulSoup/bs4/doc/
           http://stackoverflow.com/questions/38624681/how-to-use-beautifulsoup-to-save-html-of-a-link-in-a-file-and-do-the-same-with-a
           http://stackoverflow.com/questions/26328971/how-to-use-beautifulsoup-to-scrape-links-in-a-html
           http://doc.scrapy.org/en/1.1/intro/tutorial.html
           
4.)  I developed the programme using Pycharm, an IDE for Python by Jetbrains. 
5.)  I tested the project by running over multiple websites and manually comparing the files generated, the content downloaded to       the files and the number of links returned. For the debugging purpose, I used easy_understand.py file which kept printing             everything which was being executed. Pycharm assisted me as well.
6.)   I chose Python because I love working with Python. Python is a pretty good choice for projects where you need to complete          the task under a given time span and time complexity is not very much of an issue. It's fast and you have to code exactly                what you need. 
7.)   I faced a problem while developing the program, If there is a broken link on the site, the programme has no clue what to do            and It'll eventually fail. This feature can be added to the project. One other feature that can be implemented is extracting the          text in normal human readable form rather than saving it in HTML format.
8.)   You will have to install BeautifulSoup at your system. Please follow the link: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
to install it. Other than this, the program has no dependencies. Thanks a lot again. It was a pretty amazing task. I enjoyed doing it a lot. Although it took more than 2-3 hours as you said :)

Commands to run it: 
  $ sudo apt-get install zip unzip
  $ unzip Rakesh.Verma.zip
  $ cd Rakesh.Verma
  $ python easy_understand.py (To understand what is going on)
  $ python Parser.py (If you just want the files created in your system)

P.S: I have tried to make it as stable as possible but there are a lot of mistakes in the code. Following two are the most encountered errors are : 
1.) HTTP Error 404: Not Found - Means the link is broken or you don't have the permission to visit it.
2.) HTTP Error 403: Forbidden - Crawlers are disabled on the website.(Google)
