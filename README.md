# Goodreads Clone

This is a Django-based web application that replicates some of the core functionalities of Goodreads. It allows users to browse books, view book details, post reviews, and manage their profiles. The project also includes a REST API for accessing book review data.

## Features

*   **User Authentication**: Users can register, log in, and log out.
*   **User Profiles**: Users have profiles with their information and a profile picture.
*   **Book Listings**: Browse a list of all books.
*   **Book Details**: View detailed information for each book, including its cover, description, and user reviews.
*   **Book Reviews**: Users can add, edit, and delete their own book reviews.
*   **REST API**: A RESTful API to manage book reviews.

## Technologies Used

*   **Backend**: Django, Django REST Framework
*   **Database**: SQLite3 (default), PostgreSQL (optional)
*   **Asynchronous Tasks**: Celery
*   **Frontend**: HTML, CSS, JavaScript, Bootstrap5
*   **Form Rendering**: django-crispy-forms, crispy-bootstrap5
*   **Image Processing**: Pillow
*   **Environment Variables**: django-environ
*   **Web Server**: Gunicorn

## Prerequisites

*   Python 3.9+
*   pip
*   PostgreSQL (if you choose to use it)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/goodreads-clone.git
    cd goodreads-clone
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    - Create a file named `.env` in the project root directory.
    - Copy the contents of `.env.example` (you will need to create this file, see below) into `.env` and fill in the required values.

5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Environment Variables

Create a `.env` file in the project root and add the following variables.

```
SECRET_KEY='your-secret-key'
DEBUG=True

# Optional: PostgreSQL Database Configuration
# DB_NAME='your_db_name'
# DB_USER='your_db_user'
# DB_PASSWORD='your_db_password'
# DB_HOST='localhost'

# Optional: Email Configuration (for password reset, etc.)
# EMAIL_HOST_USER='your-gmail-address'
# EMAIL_HOST_PASSWORD='your-gmail-app-password'
```
To use PostgreSQL, you will also need to uncomment the corresponding lines in `greads/settings.py`.

## API Endpoints

The application provides a REST API for book reviews. The base URL for the API is `/api/`.

*   `GET /api/reviews/`: List all book reviews.
*   `POST /api/reviews/`: Create a new book review.
*   `GET /api/reviews/<id>/`: Retrieve a specific book review.
*   `PUT /api/reviews/<id>/`: Update a specific book review.
*   `PATCH /api/reviews/<id>/`: Partially update a specific book review.
*   `DELETE /api/reviews/<id>/`: Delete a specific book review.

You can browse the API at `/api-auth/` in your browser.

## A Note on NGROK

The `greads/settings.py` file contains a hardcoded `NGROK_URL`. This is used for development purposes, for example, to expose the local server to the internet for testing webhooks. You may need to change this URL to match your own ngrok tunnel. For production, this should be removed and handled properly with environment variables.
