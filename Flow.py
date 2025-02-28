from flask import Flask, request, jsonify, render_template
import csv
import os
import requests

app = Flask(__name__)

CSV_FILE = 'brokerage_data.csv'

# Telegram Bot configuration
TELEGRAM_BOT_TOKEN = '7857604095:AAHTTbABRMYUd4cswvNK3xmkGOkOR61qRyQ'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

# Initialize CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Broker Name', 'Mobile No.', 'Center', 'Seller Party', 'Buyer Party', 
                         'Seller Station', 'Buyer Station', 'Item', 'Weight', 'Rate', 
                         'Date', 'Brokerage Rate', 'Brokerage Amount'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    data = request.json
    try:
        row = [
            data.get('name', ''),
            data.get('mobileNo', ''),
            data.get('center', ''),
            data.get('sellerParty', ''),
            data.get('buyerParty', ''),
            data.get('sellerStation', ''),
            data.get('buyerStation', ''),
            data.get('item', ''),
            data.get('weight', ''),
            data.get('rate', ''),
            data.get('date', ''),
            data.get('brokerageRate', ''),
            data.get('brokerageAmount', '')
        ]
        
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(row)
        
        return jsonify({"message": "Data saved successfully!"}), 200
    except Exception as e:
        print(f"Error saving data: {e}")  # Log the error
        return jsonify({"error": str(e)}), 500

@app.route('/send_telegram', methods=['POST'])
def send_telegram():
    data = request.json
    seller_chat_id = data.get('sellerChatId')
    buyer_chat_id = data.get('buyerChatId')
    contract_details = data.get('contractDetails')

    if not seller_chat_id or not buyer_chat_id or not contract_details:
        return jsonify({"error": "Missing required fields"}), 400

    message = f"📄 *Contract Details*\n\n{contract_details}\n\nThank you!"
    
    def send_message(chat_id, text):
        payload = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'Markdown'
        }
        try:
            response = requests.post(TELEGRAM_API_URL, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error sending Telegram message: {e}")
            return {"error": str(e)}
    
    # Send messages to seller and buyer
    seller_response = send_message(seller_chat_id, message)
    buyer_response = send_message(buyer_chat_id, message)

    return jsonify({
        "seller_response": seller_response,
        "buyer_response": buyer_response
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
