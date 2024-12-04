# Flask Blog and Hotel Management System

A full-featured web application built with Flask that combines a blog platform with hotel management capabilities.

## Features

- User Authentication System
  - User registration and login
  - Password reset functionality
  - Profile management with avatar support

- Blog System
  - Create, read, update, and delete blog posts
  - Rich text editor for post content
  - User-specific post management

- Hotel Management
  - Hotel information management
  - Room inventory and booking
  - Menu management system

- RESTful API
  - Complete API coverage for all features
  - Token-based authentication
  - JSON response format

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd flask-blog
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python init_db.py
```

5. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5001`

## API Endpoints

### User Management
- GET `/api/user/<id>` - Get specific user
- GET `/api/user/all` - Get all users
- POST `/api/user` - Create new user
- PUT `/api/user/<id>` - Update user
- DELETE `/api/user/<id>` - Delete user

### Blog Posts
- GET `/api/post/<user_id>` - Get user's posts
- GET `/api/post/all` - Get all posts
- POST `/api/post` - Create new post
- PUT `/api/post/<id>` - Update post
- DELETE `/api/post/<id>` - Delete post

### Hotel Management
- GET `/api/hotel` - Get all hotels
- POST `/api/hotel` - Add new hotel
- PUT `/api/hotel/<id>` - Update hotel
- DELETE `/api/hotel/<id>` - Delete hotel

### Room Management
- GET `/api/kamar` - Get all rooms
- POST `/api/kamar` - Add new room
- PUT `/api/kamar/<id>` - Update room
- DELETE `/api/kamar/<id>` - Delete room

### Menu Management
- GET `/api/menu` - Get all menu items
- POST `/api/menu` - Add new menu item
- PUT `/api/menu/<id>` - Update menu item
- DELETE `/api/menu/<id>` - Delete menu item

## Configuration

The application can be configured through environment variables or by modifying `config.py`:

- `SECRET_KEY` - Application secret key
- `SQLALCHEMY_DATABASE_URI` - Database connection URI
- `MAIL_SERVER` - SMTP server for email functionality
- `MAIL_PORT` - SMTP port
- `MAIL_USE_TLS` - Enable/disable TLS
- `MAIL_USERNAME` - SMTP username
- `MAIL_PASSWORD` - SMTP password

## Database Models

### User
- username (string, unique)
- email (string, unique)
- image_file (string)
- password (string, hashed)
- posts (relationship)

### Post
- title (string)
- date_posted (datetime)
- content (text)
- user_id (foreign key)

### Hotel
- nama (string, unique)
- alamat (string)
- image_file (string)

### Kamar (Room)
- nama (string, unique)
- harga (string)
- image_file (string)
- fasilitas (string)
- stok (integer)

### Menu
- menu (string)
- keterangan (string)
- image_file (string)

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please create an issue in the repository or contact the maintainers.
