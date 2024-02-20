# Event Manager Api

Event Manager Api is a RESTful API built with Django Rest Framework that allows users to create, manage, and subscribe to events.

## Features

- Create, update, and delete events
- Subscribe and unsubscribe from events
- List events organized by the user
- List events subscribed to by the user

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/zhenyamisyuryow/event-management-api
    ```

2. Install and activate virtual environment:

    ```
    python3 -m venv .env
    ```
    For Windows:
    ```
    .env\Scripts\activate
    ```

    For MacOS/Linux:
    ```
    source venv/bin/activate
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```
    python3 manage.py migrate
    ```

5. Start the development server:

    ```
    python3 manage.py runserver
    ```

## Usage

### API Endpoints

### Event Manager API

This API allows users to manage events and subscriptions.

#### Auth

- **Register User**
  - Method: POST
  - URL: `http://localhost:8000/api/v1/auth/register`
  - Body:
    ```json
    {
        "email": "john.doe@example.com",
        "password": "testpass123",
        "password2": "testpass123"
    }
    ```

- **Obtain Token Pair**
  - Method: POST
  - URL: `http://localhost:8000/api/v1/auth/token/obtain`
  - Body:
    ```json
    {
        "email": "john.doe@example.com",
        "password": "testpass123"
    }
    ```

- **Refresh Access Token**
  - Method: POST
  - URL: `http://localhost:8000/api/v1/auth/token/refresh`
  - Body:
    ```json
    {
        "refresh": "<refresh_token>"
    }
    ```

#### Events

- **Manage Events**

  - **List All Events**
    - Method: GET
    - URL: `http://localhost:8000/api/v1/events`

  - **Get Event Details**
    - Method: GET
    - URL: `http://localhost:8000/api/v1/events/{event_id}`

  - **Create Event**
    - Method: POST
    - URL: `http://localhost:8000/api/v1/events/`
    - Body:
      ```json
      {
          "title": "First Event",
          "description": "This is a new event",
          "date": "2024-12-12",
          "location": "New York"
      }
      ```

  - **Update Event**
    - Method: PUT
    - URL: `http://localhost:8000/api/v1/events/{event_id}/`
    - Body:
      ```json
      {
          "title": "Updated Event",
          "description": "This is an updated event",
          "date": "2024-12-12",
          "location": "California"
      }
      ```

  - **Update Event Partially**
    - Method: PATCH
    - URL: `http://localhost:8000/api/v1/events/{event_id}/`
    - Body:
      ```json
      {
          "title": "Updated Event Partially"
      }
      ```

  - **Delete Event**
    - Method: DELETE
    - URL: `http://localhost:8000/api/v1/events/{event_id}/`

  - **List Events By User**
    - Method: GET
    - URL: `http://localhost:8000/api/v1/events/list_my_events`

#### Event Subscriptions

- **List Subscribed Events**
  - Method: GET
  - URL: `http://localhost:8000/api/v1/events/list_subscribed_events`

- **Subscribe for Event**
  - Method: POST
  - URL: `http://localhost:8000/api/v1/events/subscribe`
  - Body:
    ```json
    {
        "event": "{event_id}"
    }
    ```

- **Unsubscribe from Event**
  - Method: DELETE
  - URL: `http://localhost:8000/api/v1/events/unsubscribe`
  - Body:
    ```json
    {
        "event": "{event_id}"
    }
    ```

### Authentication

The API uses JWT (JSON Web Token) authentication. Users need to obtain a token by logging in before accessing protected endpoints.

### Signals

A signal is triggered after successful event registration, sending an email confirmation to the user (to terminal console in development).

### Testing

To run tests:

```
python manage.py test
```

## Dependencies

- Django
- Django REST Framework
- Django REST Framework Simple JWT
