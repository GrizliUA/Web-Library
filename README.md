# Web-Library
The main idea of this project, to create web-library where you can anime you are interested in, or animes which you watched and marked them with you own notations.


## Used technologies
-Django
-MySQL
-Djoser


## Featured routes
    http://127.0.0.1:8000/admin/				- Admin panel


    POST
    http://127.0.0.1:8000/auth/users/			- Create New User


    http://127.0.0.1:8000/auth/login/			- Log in
    http://127.0.0.1:8000/auth/logout/			- Log out

    POST
    http://127.0.0.1:8000/auth/token/login/			- username,password -> token

    GET
    http://127.0.0.1:8000/library/anime/1/			- authorization Token + token -> GET

    POST
    http://127.0.0.1:8000/auth/token/logout/		- authorization Token + token -> Token deactivation



    http://127.0.0.1:8000/library/				- WIP




    http://127.0.0.1:8000/library/anime/			- Show all anime
    http://127.0.0.1:8000/library/anime/<int:pk>/		- Show anime with special ID
    http://127.0.0.1:8000/library/animedelete/<int:pk>/	- Delete anime with special ID



    auth/login/->
    http://127.0.0.1:8000/accounts/profile/			- Return a adress to user list

    GET
    http://127.0.0.1:8000/auth/users/			- User list
    http://127.0.0.1:8000/auth/users/me/			- User info


## Known bugs
 - It's imposibble to post anime with empty info field


## Roadmap
 - Add more genres to one title
 - HTML + CSS page view for each urls