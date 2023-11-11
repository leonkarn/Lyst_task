***Instructions***

I ran the code in version Python 3.8. No additional requirements needs to be installed. I have included
the tests in a separate file: **test_highscoringwords.py**

I have also included a Dockerfile in case needed to run the tests. 
To run the code in Docker use the following command to build the image and run the container which is going to run
the tests:
~~~
docker build -t lyst_task . && docker run lyst_task    
~~~