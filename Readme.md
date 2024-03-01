# Event Finder Application

Welcome to the Event Finder Application! This API-driven application serves as a platform for users to effortlessly create, search, and attend events. Powered by Django Rest Framework and leveraging PostgreSQL as its robust database solution, this application ensures efficient event management. With JWT tokens enhancing security measures and Docker facilitating seamless deployment, managing events has never been easier.

## Getting Started

### Prerequisites

Before getting started, ensure you have the following installed:

- Docker
- Docker Compose

### Running the Application

1. **Clone the Repository:**

    ```shell
    git clone https://github.com/anGahade/Events_Finder.git
    ```

2. **Set Environment Variables:**

    Create a `.env` file in the project root and set the necessary environment variables:

    ```
    SECRET_KEY=
    DB_PASSWORD=
    DB_NAME=
    DB_USER=
    DB_HOST=
    DB_PORT=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    ```

3. **Build and Run the Docker Containers:**

    ```shell
    docker-compose up --build
    ```

4. **Create a Superuser:**

    ```shell
    docker-compose exec backend python manage.py createsuperuser
    ```

5. **Access API Documentation:**

    Explore the API documentation at [http://localhost:8000/swagger](http://localhost:8000/swagger) or [http://localhost:8000/redoc](http://localhost:8000/redoc) (for FastAPI).

## Project Structure

The project is meticulously organized into separate applications, each responsible for distinct functionalities:

- **users:** Manages user authentication and profiles.
- **events:** Handles event creation, retrieval, updating, and deletion.
- **tickets:** Manages ticket reservations and user ticket history.
- **reviews:** Deals with event reviews and ratings.
- **notifications:** Handles notifications for users.

## Database Structure

The database schema comprises the following tables:

- Users
- Events
- Tickets
- Reviews
- Notifications

Feel free to navigate through these structured components to streamline your event management process efficiently.