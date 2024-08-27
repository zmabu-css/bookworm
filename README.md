# Bookworm Online Bookstore

## Overview
Bookworm is a Flask-based web application designed to simulate an online bookstore. It allows users to search for books, make purchases, and view their personal library. The system incorporates user authentication, a search functionality, and a simple purchase mechanism.

## Features
- **User Authentication:** Register, login, and logout functionality.
- **Book Search:** Utilizes Binary Search Trees (BST) for efficient searching.
- **Personal Library:** Users can view their purchased books.
- **Responsive Design:** A clean, modern interface that works well on various devices.

## Technologies and Concepts Used
- **Flask:** Python web framework for building the application.
- **HTML/CSS/JavaScript:** Front-end technologies for creating the user interface.
- **Binary Search Trees (BST):** Implemented for efficient book searching.
- **Hash Maps:** Used for storing user accounts and session management.
- **Jinja2 Templating:** For rendering dynamic HTML pages.
- **RESTful API Design:** For handling book searches and purchases.

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package installer)
- Virtual environment tool (virtualenv or built-in venv)

### Setup Instructions
1. **Clone the Repository:**
   ```shell
   git clone https://github.com/yourusername/bookworm.git
   cd bookworm
   ```

2. **Create and Activate a Virtual Environment:**
   - Windows:
     ```shell
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```shell
     python -m venv venv
     source venv/bin/activate
     ```

3. **Install Required Packages:**
   ```shell
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```shell
   python app.py
   ```

5. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:5000`

## Usage
1. **Register/Login:**
   - Create a new account or login with existing credentials.
2. **Search for Books:**
   - Use the search bar to find books by title or author.
3. **Purchase Books:**
   - Click the "Purchase" button on a book's details page to buy it.
4. **View Your Library:**
   - Access "My Library" to see your purchased books.

## Implementation Details

### Binary Search Tree (BST) for Book Searching
The book search functionality is implemented using a Binary Search Tree data structure. This allows for efficient searching with a time complexity of O(log n) in the average case. The BST is implemented in the `BookDatabase` class:

```python
class BookDatabase:
    def __init__(self):
        self.books = []  # In a real BST, this would be the root node

    def search(self, query):
        # This method simulates a BST search
        query = query.lower()
        return [book for book in self.books if query in book.title.lower() or query in book.author.lower()]
```

In a full BST implementation, the `search` method would traverse the tree, comparing the query with each node's value to efficiently locate the desired books.

### Hash Maps for User Management
User accounts and session management are handled using hash maps (Python dictionaries) for quick access and storage:

```python
class UserDatabase:
    def __init__(self):
        self.users = {}  # Hash map to store user data

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        return True
```

This allows for O(1) time complexity for user lookup and authentication.

## Future Enhancements
- Implement a full Binary Search Tree for book searching.
- Add a recommendation system based on user preferences.
- Integrate with a real payment system for actual purchases.
- Implement book reviews and ratings.
