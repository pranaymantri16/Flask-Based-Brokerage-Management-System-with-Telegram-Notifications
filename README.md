# Flask-Based Brokerage Management System with Telegram Notifications

## Overview
This project is a **Flask-based backend system** that facilitates brokerage management by:
- Collecting seller, buyer, and item details.
- Storing data in a CSV file.
- Calculating brokerage amounts.
- Sending contract details to both the seller and buyer via Telegram.

## Features
- **Data Storage**: Saves brokerage details into a CSV file.
- **Automated Brokerage Calculation**: Handles brokerage rate and amount.
- **Telegram Notifications**: Sends contract details to the buyer and seller using the Telegram Bot API.
- **RESTful API**: Provides endpoints for saving data and sending Telegram messages.

## Installation
### Prerequisites
Ensure you have Python installed on your system. Install the required dependencies using:

```bash
pip install flask requests
```

### Clone the Repository
```bash
git clone https://github.com/your-repo/brokerage-management.git
cd brokerage-management
```

## Configuration
1. **Set up Telegram Bot**
   - Create a bot using [BotFather](https://t.me/BotFather) on Telegram.
   - Obtain the bot token and replace `TELEGRAM_BOT_TOKEN` in `flow.py`.

2. **Run the Flask Application**
```bash
python flow.py
```

The application will run on `http://127.0.0.1:5000/` by default.

## API Endpoints
### `GET /`
Serves the frontend interface (index.html).

### `POST /save`
Saves the brokerage transaction details to `brokerage_data.csv`.
- **Request Body (JSON)**:
  ```json
  {
    "name": "John Doe",
    "mobileNo": "1234567890",
    "center": "ABC Market",
    "sellerParty": "Seller Pvt Ltd",
    "buyerParty": "Buyer Pvt Ltd",
    "sellerStation": "Station A",
    "buyerStation": "Station B",
    "item": "Wheat",
    "weight": "100kg",
    "rate": "50",
    "date": "2024-02-28",
    "brokerageRate": "2%",
    "brokerageAmount": "100"
  }
  ```

### `POST /send_telegram`
Sends contract details to the seller and buyer via Telegram.
- **Request Body (JSON)**:
  ```json
  {
    "sellerChatId": "123456789",
    "buyerChatId": "987654321",
    "contractDetails": "Brokerage contract details here."
  }
  ```

- **Response**:
  ```json
  {
    "seller_response": { "ok": true },
    "buyer_response": { "ok": true }
  }
  ```

## Technologies Used
- **Flask** (Backend API)
- **CSV** (Data Storage)
- **Telegram Bot API** (Notifications)

## Future Enhancements
- Store data in a database instead of CSV.
- Implement a frontend dashboard.
- Add authentication and user management.

## License
This project is licensed under the MIT License.

