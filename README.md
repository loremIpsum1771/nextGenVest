# Scholarship Selection API

This solution features a REST API made using the Django REST framework 

## Quickstart/Setup:

1. Clone the repository/ Download the .zip file
2. Open a terminal window
3. cd nextGenVest

4. Create and activte a virtualenv to isolate the package dependencies locally
```virtualenv api_env
   source api_env/bin/activate  *For mac and linux*
```
5. Install Django/Django REST framework and dependencies into the virtualenv
```
   pip install -r requirements.txt
```
6. Change into project source and runserver
```
   cd ngv_challenge
   python manage.py runserver
```
7. Open your browser and navigate [to this url](http://127.0.0.1:8000/scholarship-api)

8. Once on the page, you will see a form where you can enter in JSON data and submit a request. Enter in sample JSON and
   the "POST" button. Once this is done, you will see the following page:
   
 
## Some notes on the Code/Algorithm

The code for the REST API and the class is located in: 
```
nextGenVest/ngv_challenge/scholarship_list/views.py
```
The URL routing for the API is located in 
```
nextGenVest/ngv_challenge/ngv_challenge/urls.py
```

The algorithm operates by visiting each integer/node exactly once per direction and because the number of directions is constant, the time complexity is:

```
O(rows * columns)
```
There are only a couple of variables used to keep track of the max/current path value and a couple of lists to store the best scholarships so the  space complexity is constant in the number of scholarships allowed (i.e. 11)

