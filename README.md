Python REST APIs With Flask, Connexion, Marshmallow and SQLAlchemy 


Once done, This is how the Flask REST API EndPoints can be accessed:
Base URL : http://localhost:8000/
Example  : http://localhost:8000/people/Banerjee 
---------------------------------------------------------------------------
Action	|HTTP Verb	|URL Path	            |Description                  |
---------------------------------------------------------------------------
Read	|GET	    |/api/people	        |Read a collection of people. |
Create	|POST	    |/api/people	        |Create a new person.         |
Read	|GET	    |/api/people/<lname>	|Read a particular person.    |
Update	|PUT	    |/api/people/<lname>	|Update an existing person.   |
Delete	|DELETE	    |/api/people/<lname>	|Delete an existing person.   |
---------------------------------------------------------------------------

Example -- http://localhost:8000/api/notes/1 
----------------------------------------------------------------------------
Action	|HTTP Verb	 |URL Path	            |Description                   |
----------------------------------------------------------------------------
Create	|POST	     |/api/notes	        |URL to create a new note      |
Read	|GET	     |/api/notes/<note_id>	|URL to read a single note     |
Update	|PUT	     |api/notes/<note_id>	|URL to update a single note   |
Delete	|DELETE	     |api/notes/<note_id>	|URL to delete a single note   |
----------------------------------------------------------------------------

You can use a sqlite3 database. The SQLs are in createDB.py file

Contact Info : Feel free to contact me to discuss any issues, questions, or comments. My contact info can be found on my GitHub page.

License : I am providing code and resources in this repository to you under an open source license. Because this is my personal repository, the license you receive to my code and resources is from me and not my employer (Morgan Stanley Asia Bank Ltd).

Copyright : Copyright 2022 Kaushik Banerjee

Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

https://creativecommons.org/licenses/by-sa/4.0/