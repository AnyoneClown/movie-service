## Deployed Website
Explore the deployed Task Manager web application on [Render](https://movie-service-63ce.onrender.com/api/schema/swagger/)! Happy task managing!


## Getting Started

Create a `.env` file in the root of your project and define the necessary variables. You can use `.env.sample` as a template.


1. **Clone the Repository:**
    ```bash
    git clone https://github.com/AnyoneClown/Airport-API-Service.git
    ```

2. **Create venv:**
    ```bash
    python -m venv venv
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Database Migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Fill the database with data from python console:**
    ```bash
    from movie.scraper import main
    main()
    ```

6. **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```