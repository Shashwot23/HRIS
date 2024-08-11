# Human Resource Management System (HRIS)

## Overview
The Human Resource Management System (HRIS) is a web-based application developed to streamline and automate various HR functions within an organization. This system is built using Python and Django and is designed to assist HR professionals and managers in managing employment details, tracking performance, scheduling company events, and handling leave management efficiently.

## Features
### 1. **Dashboard**
   - A centralized dashboard providing an overview of the HR activities.
   - Displays key metrics such as the number of employees, upcoming events, pending leave requests, and recent announcements.
   - Quick access to various modules of the HRIS.
   - ![dashboard](https://i.imgur.com/LoWjJU6.png)

### 2. **Employment Management**
   - Manage employee profiles with detailed information like personal details, job titles, department, salary, etc.
   - Easily add, update, or remove employee records.
   - Search and filter employees based on various criteria.
   - ![employment management](https://photos.google.com/search/_tra_/photo/AF1QipPk0yDsrjDgfZSQhE7UazW8y9UZjnV5URfWVh2I)

### 3. **Announcements**
   - Post company-wide announcements to keep everyone informed.
   - Set expiry dates for announcements to automatically remove outdated information.

### 4. **Company Event Calendar**
   - Schedule and manage company events.
   - View all upcoming events in a calendar format.
   - Send reminders and notifications to employees regarding events.
   - ![calendar](https://photos.google.com/search/_tra_/photo/AF1QipPNMMSfNgA8-_DCraMxpi9PWkC8concfil_GR5U)

### 5. **Performance Appraisal**
   - Conduct and track employee performance reviews.
   - Set appraisal criteria and evaluate employees based on these metrics.
   - Generate performance reports and provide feedback to employees.
   - ![performance](https://photos.google.com/search/_tra_/photo/AF1QipPP7Gv1n7z9ZpOuOlCtcgxQLqysNRbYDGUR8YN6)
   - ![performance](https://photos.google.com/search/_tra_/photo/AF1QipOgi0vnuZdwqJfC7AN_NUQ0oy9oetxBrB16zZpZ)

### 6. **Leave Management**
   - Manage employee leave requests with ease.
   - Employees can apply for leave, and managers can approve or reject requests.
   - Track leave balances, leave history, and generate leave reports.

## Installation
To get a local copy up and running, follow these simple steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Shashwot23/HRIS.git
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install django
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (admin account):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    - Open your browser and go to `http://127.0.0.1:8000/`
    - Login with the superuser account you created where you have access to everything and can create empoyees or managers.

## Usage
- Once logged in, you will be taken to the dashboard where you can navigate through different HR functions such as employment management, leave management, performance appraisal, and more.
- The admin has access to all features, while employees can manage their profiles, view announcements, and apply for leave.
- Managers can manage only the employee of their department and can rate goals and functional areas of the employee.

## Contact
For any inquiries, you can reach me at [shashwothapa@gmail.com](mailto:shashwothapa@gmail.com).

---

**GitHub Repository:** [HRIS](https://github.com/Shashwot23/HRIS)

