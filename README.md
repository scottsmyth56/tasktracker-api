# Task Tracker

Task Tracker API is a RESTful API built with Django REST Framework. The API provides endpoints for managing tasks and events, allowing users to create, edit, and delete tasks and events. It also provides endpoints for user management, including user registration and authentication.

The objective of this site is to help people increase their day-to-day productivity by organizing their tasks in one place.

This project was aligned with the tasktracker-app project. The Client Side app was built using React. Repository can be found [HERE](https://github.com/scottsmyth56/tasktracker-app).

The Deployed React App is available [HERE](https://tasktracker-app-273d99460b58.herokuapp.com/)

## Table of Contents

- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Testing](#testing)
  - [PEP8 Validation](#pep8-validation)
  - [Manual Tests](#manual-tests)
- [Credit](#credit)
  - [Code](#code)

## Testing

### PEP8 Validation

By Using Black Formatter throughout the whole development process. I was easily able to adhere to PEP8 standards.

### Manual Tests

Manual Tests were carried out on both the Client side App to test API connectivity and on Postman to test the API endpoints.

## Manual Testing Procedures for User Interface

## Revised Manual Testing Procedures for User Interface

| Test Case                         | Process                                                                       | Expected Result                                                                           | Actual Result |
| --------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------- |
| **Create Event (UI)**             | Navigate to the event creation page and fill out the form.                    | A new event should be added to the event list.                                            | Works         |
| **Edit Event (UI)**               | Select an event from the list and edit details.                               | The selected event's details should be updated.                                           | Works         |
| **Delete Event (UI)**             | Click the delete button on an event and confirm deletion.                     | The event should be removed from the event list.                                          | Works         |
| **Create Task (UI)**              | Navigate to the task creation page and fill out the form.                     | A new task should be added to the task list.                                              | Works         |
| **Edit Task (UI)**                | Select a task from the list and edit details.                                 | The selected task's details should be updated.                                            | Works         |
| **Delete Task (UI)**              | Click the delete button on a task and confirm deletion.                       | The task should be removed from the task list.                                            | Works         |
| **Event List View (UI)**          | Navigate to `/events/`.                                                       | The page should display a list of all events.                                             | Works         |
| **Event Detail View (UI)**        | Navigate to `/events/<int:pk>/` with a valid event ID.                        | The page should display detailed information about the specified event.                   | Works         |
| **Event Invitation (UI)**         | Navigate to `/events/invite/` and fill out the invitation form.               | A new event invitation should be created and sent.                                        | Works         |
| **Accept Event Invitation (UI)**  | Navigate to `/event-invitations/<int:pk>/accept/` with a valid invitation ID. | The invitation should be accepted, and the user's status for the event should be updated. | Works         |
| **Event Invitation Details (UI)** | Navigate to `/event-invitations/<int:pk>/` with a valid invitation ID.        | The page should display detailed information about the specified event invitation.        | Works         |
| **Task List View (UI)**           | Navigate to `/tasks/`.                                                        | The page should display a list of all tasks.                                              | Works         |
| **Task Detail View (UI)**         | Navigate to `/tasks/<int:pk>/` with a valid task ID.                          | The page should display detailed information about the specified task.                    | Works         |
| **Admin Panel Access (UI)**       | Navigate to `/admin/`.                                                        | The admin panel should be accessible for authorized users.                                | Works         |
| **API Authentication (UI)**       | Navigate to `/api-auth/`.                                                     | The page should provide options for API authentication.                                   | Works         |
| **User Authentication (UI)**      | Navigate to `/auth/`.                                                         | The page should provide user authentication options, such as login and logout.            | Works         |
| **User Registration (UI)**        | Navigate to `/auth/registration/`.                                            | The page should provide user registration options.                                        | Works         |
| **User Login (UI)**               | Navigate to `/auth/login/`.                                                   | The user should be able to log in with valid credentials.                                 | Works         |

## Revised Manual Testing Procedures for Postman (API Endpoints)

| Test Case                             | Process                                                                      | Expected Result                                                 | Actual Result |
| ------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------- |
| **Event List Endpoint (GET)**         | Send a GET request to `/events/`.                                            | The response should return a list of all events.                | Works         |
| **Event Detail Endpoint (GET)**       | Send a GET request to `/events/<int:pk>/` with a valid event ID.             | The response should return details of the specified event.      | Works         |
| **Create Event Endpoint (POST)**      | Send a POST request to `/events/` with event details.                        | The response should confirm creation of a new event.            | Works         |
| **Edit Event Endpoint (PUT/PATCH)**   | Send a PUT/PATCH request to `/events/<int:pk>/` with updated event details.  | The response should confirm the event details were updated.     | Works         |
| **Delete Event Endpoint (DELETE)**    | Send a DELETE request to `/events/<int:pk>/`.                                | The response should confirm the event was deleted.              | Works         |
| **Task List Endpoint (GET)**          | Send a GET request to `/tasks/`.                                             | The response should return a list of all tasks.                 | Works         |
| **Task Detail Endpoint (GET)**        | Send a GET request to `/tasks/<int:pk>/` with a valid task ID.               | The response should return details of the specified task.       | Works         |
| **Create Task Endpoint (POST)**       | Send a POST request to `/tasks/` with task details.                          | The response should confirm creation of a new task.             | Works         |
| **Edit Task Endpoint (PUT/PATCH)**    | Send a PUT/PATCH request to `/tasks/<int:pk>/` with updated task details.    | The response should confirm the task details were updated.      | Works         |
| **Delete Task Endpoint (DELETE)**     | Send a DELETE request to `/tasks/<int:pk>/`.                                 | The response should confirm the task was deleted.               | Works         |
| **Create Event Invitation (POST)**    | Send a POST request to `/events/invite/` with invitation details.            | The response should confirm creation of a new event invitation. | Works         |
| **Accept Event Invitation (POST)**    | Send a POST request to `/event-invitations/<int:pk>/accept/`.                | The response should confirm the acceptance of the invitation.   | Works         |
| **User Registration Endpoint (POST)** | Send a POST request to `/auth/registration/` with user registration details. | The response should confirm the user's registration.            | Works         |
| **User Login Endpoint (POST)**        | Send a POST request to `/auth/login/` with user login credentials.           | The response should confirm the user's successful login.        | Works         |

## Technologies Used

### Languages & Frameworks Used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

### Libraries, Packages & Tools Used

- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django REST Framework Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Django REST Framework CORS Headers](https://pypi.org/project/django-cors-headers/)
- [Heroku](https://www.heroku.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Git](https://git-scm.com/)
- [ElephantSQL](https://www.elephantsql.com/)
- [Black Formatter]
- [Cloudinary](https://cloudinary.com/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)

## Deployment

The Site was deployed using Heroku Hosting Platform. A really powerful platform at that.

### Deployment Steps

#### Local Workspace Steps

- Add a Procfile to the root of the project with the following content: `release: python manage.py makemigrations && python manage.py migrate
  web: gunicorn tasktracker_api.wsgi`
- Add a requirements.txt file to the root of the project with the following content: `pip3 freeze > requirements.txt`
- Turn Debug to False in settings.py
- Add your Client Side app URL to ALLOWED_HOSTS in settings.py
- Add your Client Side app URL to CSRF_TRUSTED_ORIGINS in settings.py
- Add your Client Side app URL to CORS_ALLOWED_ORIGINS in settings.py
- Add your Prod Database URL to DATABASES in settings.py
- Run python3 manage.py makemigrations
- Run python3 manage.py migrate
- Change your Database settings to use PostgreSQL - This will be your Prod Database
- Commit and Push to Github

#### Heroku Steps

- Create a new project on Heroku
- Connect Github Repo
- In settings, configure Environment Variables lilke Database URL, Cloudinary URL, SecretKey etc..
- In Deploy, configure your automatic deploys or not.
- Deploy App

### Cloning for Further Development(Codeanywhere)

- Open Codeanywhere.
- Click on "File" in the top menu bar, then select "New Connection" > "From Git, GitHub, Bitbucket, Gitlab, URL".
- In the pop-up dialog box, paste the repository URL you want to clone: https://github.com/scottsmyth56/tasktracker-api and click "Next".
- Give your new connection a name and click "Create".
- Codeanywhere will create a new container with your cloned repository. It may take a few minutes.
- Once it's done, click on the "Folder" icon on the left sidebar to find your cloned repository.
- You can start working on the codebase, make changes and save them.
- When you are ready to push your changes, right click on your container and select "SSH Terminal" to open the terminal.
- In the terminal, navigate to your project folder (if you're not already there).
- Run git add . to add all the changes.
- Commit your changes by running git commit -m "your commit message".
- Push your changes by running git push.

### Cloning for Further Development ( Locally )

- Make sure you have Git installed on your computer. If you don't have it already, you can download it from the official website (https://git-scm.com/)
- Open a terminal window (on Windows, Git Bash is a good option)
- Navigate to the directory where you want to clone the repository using the cd command. For example, to navigate to the Documents folder, you would use the command cd Documents.
- Use the following command to clone the repository: git clone https://github.com/scottsmyth56/tasktracker-api.git
- The command will create a new directory called "tasktracker-api" in the current directory, and will copy all the files from the repository into that directory.
- Navigate into the newly cloned directory by running cd tasktracker-app
- you can check the content of the cloned repository by running ls command
- Make sure to update your local copy with the remote repository by running git pull command
- you can start to use the cloned repository as you wish

## Credit

### Code

- Permission Classes for Events and Tasks - [Stack Overflow](https://stackoverflow.com/questions/49174493/django-rest-framework-permission-classes)
- Django REST Framework Simple JWT - [Django REST Framework Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- Django REST Framework CORS Headers - [Django REST Framework CORS Headers](https://pypi.org/project/django-cors-headers/)
- Django REST Framework - [Django REST Framework](https://www.django-rest-framework.org/)
- to_representation() method - [Stack Overflow](https://stackoverflow.com/questions/49174493/django-rest-framework-permission-classes)