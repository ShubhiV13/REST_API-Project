## Weather Forecast Application


## Overview
- Weather Forecast Application is a web-based application developed using Django that allows users to check real-time weather information for different cities. The application fetches weather data from a Weather API and displays details such as temperature, weather conditions, and forecast information through a clean and user-friendly interface.

## Features
- Search weather by city name
- Real-time weather information
- Displays temperature and weather conditions
- User authentication (Login/Logout)
- Responsive and intuitive interface
- Weather forecast display

## Technologies Used
- Python
- Django
- HTML
- CSS
- Javascript

## Project Objective
- The purpose of this project is to provide users with quick and accurate weather information through a simple web application. This project helped me learn API integration, Django development, user authentication, and dynamic data rendering.

## Installation/Setup
1. Clone the repository:
- git clone https://github.com/ShubhiV13/REST_API-Project.git
2. Navigate to the project directory:
- cd weather-forecast-app
3. Install dependencies:
- pip install -r requirements.txt
4. Run the server:
- python manage.py runserver
5. Open your browser:
- http://127.0.0.1:8000

## Files

### Project Configuration

- **manage.py**
  - Django's command-line utility for managing the project.
- **requirements.txt**
  - Contains the required Python packages and dependencies.
- **Procfile**
  - Configuration file used for deployment.
- **.gitignore**
  - Specifies files and folders ignored by Git.
- **deployed link**
  - Contains the deployed application URL.

### Config Folder

- **__init__.py**
  - Marks the directory as a Python package.
- **settings.py**
  - Contains project settings and configurations.
- **urls.py**
  - Defines the project's URL routing.
- **asgi.py**
  - ASGI configuration for asynchronous deployment.
- **wsgi.py**
  - WSGI configuration for deployment.

### Weather Application

- **admin.py**
  - Registers models with the Django admin panel.
- **apps.py**
  - Application configuration settings.
- **models.py**
  - Defines database models.
- **serializers.py**
  - Handles data serialization for API responses.
- **tests.py**
  - Contains test cases for the application.
- **urls.py**
  - Defines application-specific URL routes.
- **views.py**
  - Contains the business logic and API integration.

### Templates

- **templates/weather/**
  - Contains HTML templates used to render weather information and user interface pages.

## ScreenShots
<img width="300" height="640" alt="image" src="https://github.com/user-attachments/assets/2fb479d4-2953-4207-ba5f-6ca3e85c8411" />
<img width="300" height="640" alt="image" src="https://github.com/user-attachments/assets/5ef637b5-ed11-41b6-b3c5-9fd2e661a0c0" />


## Key Functionalities
- Enter a city name
- Fetch weather data using API
- View temperature and weather conditions
- Secure user login and logout
- Responsive weather dashboard
  
## Future Enhancements
- 7-Day Weather Forecast
- Weather Alerts and Notifications
- Location-Based Weather Detection
- Air Quality Index (AQI)
- Dark Mode Support

## Contact
- Author: Shubhangi Vishwakarma
- GitHub: ShubhiV13
- Email: [vishwakarmashubhangi75@gmail.com]
