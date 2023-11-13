***Instructions***

I ran the code in version Python 3.8. No additional requirements needs to be installed. I have included
the tests in a separate file: **test_highscoringwords.py**

I have also included a Dockerfile in case needed to run the tests in Docker. 
Use the following command to build the image and run the container which is going to run
the tests on build:
~~~
docker build -t lyst_task . && docker run lyst_task    
~~~

I have also included a main.py file to run the methods.
If you have set up Python, you can try this by running  :
~~~
python main.py
~~~
Or alternatively with Docker Image that you have built previously
with the command:
~~~
 docker run lyst_task python main.py
~~~