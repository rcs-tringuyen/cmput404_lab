1) https://github.com/rcs-tringuyen/cmput404_lab/tree/main/Lab4-django
2) Django welcome page
3) At '/' we got 404 not found. At '/polls' we got the "Hello World" message
4) Django migration make us update our database and models.
5) We see the authentication database (contain users) and the polls database (with questions and choices columns). To add custom models you can add it in polls/models.py then do a migration.
6) We can see the response string variable when go to the urls. We get 404 Not Found when using string. We can use "str" instead of "int".
7) When URL get complex, hardcode URL will lead to 404 and other side effect. It is very hard to debug this as well. 
