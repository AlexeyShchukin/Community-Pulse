# Community-Pulse

## Description
This project is a RESTful API for managing polls, categories, and votes, built with Flask. It allows users to create, manage, and participate in polls, while also tracking voting statistics. The API is designed to be robust and scalable, utilizing SQLAlchemy for database interactions and following modern Python best practices.

## Features
* **Category Management:** Create, retrieve, update, and delete poll categories.
* **Poll Management:** Create, retrieve, update, and delete polls.
* **Voting System:** Users can cast votes on poll options.
* **Poll Statistics:** Track total votes and unique voters for polls, and vote counts/percentages for options.
* **Database ORM:** Utilizes SQLAlchemy 2.0 style for database interactions.
* **API Endpoints:** Clearly defined RESTful endpoints for all core functionalities.
* **Error Handling:** Centralized exception handling for various API operations.

## Technologies
The project is built using the following key technologies:
* **Python 3.11+**
* **Flask:** Web framework for building the API.
* **SQLAlchemy 2.0:** ORM for database interactions.
* **Flask-SQLAlchemy:** Flask extension for SQLAlchemy integration.
* **Flask-Migrate / Alembic:** Database migrations.
* **Pydantic:** Data validation.
* **PyMySQL:** MySQL driver.
* **python-dotenv:** Environment variable management.

## Structure
```
.
├── src/
│   ├── api/
│   │   ├── controllers/
│   │   │   ├── category.py       # Handles HTTP requests for categories
│   │   │   ├── poll.py           # Handles HTTP requests for polls
│   │   │   └── vote.py           # Handles HTTP requests for votes
│   │   └── routes/
│   │       ├── __init__.py       # Registers API blueprints
│   │       ├── categories.py     # Defines API routes for categories
│   │       ├── polls.py          # (Assumed) Defines API routes for polls
│   │       └── votes.py          # (Assumed) Defines API routes for votes
│   ├── core/
│   │   ├── app_runner.py         # Initializes and configures the Flask application
│   │   ├── config.py             # Manages application settings and environment variables
│   │   ├── db.py                 # Initializes SQLAlchemy and Flask-Migrate
│   │   └── exceptions.py         # Defines custom exceptions for the application
│   ├── dto/                      # Data Transfer Objects (Pydantic models for API data)
│   │   ├── __init__.py           # Exports DTOs for easy import
│   │   ├── base.py               # Base DTOs, timestamp mixin, pagination DTOs
│   │   ├── category.py           # Category-specific DTOs
│   │   ├── poll.py               # Poll-specific DTOs
│   │   └── vote.py               # Vote-specific DTOs
│   ├── models/
│   │   ├── __init__.py           # Exports models for easy import
│   │   ├── base.py               # Base SQLAlchemy model with timestamp mixin
│   │   ├── user.py               # User model
│   │   ├── poll.py               # Poll and PollOption models (inferred from imports)
│   │   ├── vote.py               # Vote model (inferred from imports)
│   │   └── statistics.py         # Poll and Option statistics models
│   ├── repositories/             # Data access layer for database operations
│   │   ├── base.py               # Generic base repository with CRUD operations
│   │   ├── category.py           # Repository for Category model
│   │   ├── poll.py               # Repository for Poll and PollOption models
│   │   └── vote.py               # Repository for Vote model
│   └── services/
│       ├── category.py           # Business logic for category operations
│       ├── poll.py               # Business logic for poll operations
│       └── vote.py               # Business logic for vote operations
├── main.py                       # Entry point for running the Flask application
├── manage.py                     # Flask CLI entry point for commands like migrations
├── requirements.txt              # Project dependencies
├── .env.example                  # Environment variables (example)
└── README.md
```