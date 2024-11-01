# Digishop

Welcome to **Digishop**, a comprehensive backend application designed for an e-commerce platform. This application allows users to register, log in, manage a shopping cart
## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Features](#features)
- [Usage](#usage)

## Introduction
digishop digital Ecommerce

## Technologies Used

This project is built using the following technologies:


- **Django 5.1.2**
- **Django REST Framework 3.15.2**
- **djangorestframework-simplejwt 5.3.1** for JWT authentication
- **Django CORS Headers 4.5.0** for handling Cross-Origin Resource Sharing
- **Pillow 11.0.0** for image processing
- **Python Dotenv 1.0.1** for managing environment variables
- **sqlparse 0.5.1** for SQL parsing
- **asgiref 3.8.1** for asynchronous support
- **tzdata 2024.2** for timezone support
- **PyJWT 1.7.1** for encoding and decoding JSON Web Tokens

## Setup

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd digishop


2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the root directory and add the necessary environment variables, such as your secret keys and database configurations.

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Features

- **User Registration and Login**: Users can create accounts and log in securely.
- **Shopping Cart Functionality**:
  - Users can add items to their cart.
  - The cart displays each product's image and amount.
  - The total quantity updates when items are added or removed.
- **Product Management**:
  - Admins can add, edit, and delete products in the database.

Usage
After setting up the project, you can access the API endpoints for the following features:

## Usage

After setting up the project, you can access the API endpoints for the following features:

### User Management
- **Registration**: `POST /api/users/`
- **Login**: `POST /api/token/`
- **Refresh Token**: `POST /api/token/refresh/`

### Shopping Cart
- **Add to Cart**: `POST /api/carts/<cart_id>/cart-items/` (create a cart item for a specific cart)
- **View Cart**: `GET /api/carts/<cart_id>/` (view items in a specific cart)
- **Update Cart Item**: `PUT /api/cart-items/<item_id>/` (update a specific cart item)
- **Delete from Cart**: `DELETE /api/cart-items/<item_id>/` (remove a specific item from the cart)

### Product Management
- **List Products**: `GET /api/products/`
- **Add Product**: `POST /api/products/`
- **Update Product**: `PUT /api/products/<product_id>/`
- **Delete Product**: `DELETE /api/products/<product_id>/`


