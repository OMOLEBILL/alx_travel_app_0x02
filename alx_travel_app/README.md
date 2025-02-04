# **ALX Travel App**

## **Description**

ALX Travel App is a Django-based API that allows users to manage travel-related data such as listings, bookings, and reviews. The application uses Django REST Framework for API functionality and Swagger for API documentation.

---

## **Features**
- **Listings Management**:
  - Create, read, update, and delete travel listings.
  - Store details such as title, description, price per night, location, and availability.
- **Bookings Management**:
  - Create, read, update, and delete bookings associated with listings.
  - Store details such as user name, check-in date, and check-out date.
- **Reviews Management**:
  - Create, read, update, and delete reviews associated with listings.
  - Store details such as user name, rating, and comments.

---

## **API Endpoints**

### **Listings Endpoints**
| Method | Endpoint              | Description                 |
|--------|-----------------------|-----------------------------|
| GET    | `/api/listings/`      | Retrieve all listings       |
| POST   | `/api/listings/`      | Create a new listing        |
| GET    | `/api/listings/<id>/` | Retrieve a specific listing |
| PUT    | `/api/listings/<id>/` | Update a specific listing   |
| DELETE | `/api/listings/<id>/` | Delete a specific listing   |

### **Bookings Endpoints**
| Method | Endpoint              | Description                 |
|--------|-----------------------|-----------------------------|
| GET    | `/api/bookings/`      | Retrieve all bookings       |
| POST   | `/api/bookings/`      | Create a new booking        |
| GET    | `/api/bookings/<id>/` | Retrieve a specific booking |
| PUT    | `/api/bookings/<id>/` | Update a specific booking   |
| DELETE | `/api/bookings/<id>/` | Delete a specific booking   |

### **Reviews Endpoints (Optional for Future Development)**
| Method | Endpoint              | Description                 |
|--------|-----------------------|-----------------------------|
| GET    | `/api/reviews/`       | Retrieve all reviews        |
| POST   | `/api/reviews/`       | Create a new review         |
| GET    | `/api/reviews/<id>/`  | Retrieve a specific review  |
| PUT    | `/api/reviews/<id>/`  | Update a specific review    |
| DELETE | `/api/reviews/<id>/`  | Delete a specific review    |

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/alx_travel_app.git
cd alx_travel_app