import requests

# URL của trang web để lấy IP
url_ip_score = "https://ip-score.com/spamjson"

# Hàm để lấy IP từ API ip-score
def get_ip_from_ip_score():
    try:
        # Gửi yêu cầu GET tới trang
        response = requests.get(url_ip_score)

        # Kiểm tra mã phản hồi
        if response.status_code == 200:
            # Chuyển đổi nội dung phản hồi thành đối tượng JSON
            data = response.json()

            # Trích xuất IP
            ip = data.get("ip", "Không tìm thấy IP")
            blacklists = data.get("blacklists", {})

            # In ra các thông tin IP và blacklists
            print(f"IP: {ip}")
            return ip, blacklists  # Trả về cả IP và blacklists
        else:
            print(f"Có lỗi xảy ra khi lấy IP. Mã trạng thái: {response.status_code}")
            return None, None

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        return None, None

# Hàm để truy cập API ipqualityscore và in phản hồi
def get_data_from_ip_quality_score(ip):
    api_key = "JT3At1bimLGTklpSH7nAbFbVg0JqBgEd"  # Thay bằng API key của bạn
    url = f"https://ipqualityscore.com/api/json/ip/{api_key}/{ip}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Trích xuất các thông tin cần thiết
            fraud_score = data.get('fraud_score', 'Không tìm thấy Fraud Score')
            city = data.get('city', 'Không tìm thấy City')
            region = data.get('region', 'Không tìm thấy Region')
            proxy = data.get('proxy', 'Không tìm thấy Proxy')
            vpn = data.get('vpn', 'Không tìm thấy VPN')
            tor = data.get('tor', 'Không tìm thấy Tor')
            zip_code = data.get('zip_code', 'Không tìm thấy Zip Code')  # Lấy zip_code

            # In ra các thông tin với màu sắc
            print("Nội dung phản hồi từ API ipqualityscore:")

            # In Fraud Score với màu sắc
            if isinstance(fraud_score, (int, float)):
                if fraud_score > 50:
                    print("\033[91m" + f"Fraud Score: {fraud_score}" + "\033[0m")  # Màu đỏ
                else:
                    print("\033[92m" + f"Fraud Score: {fraud_score}" + "\033[0m")  # Màu xanh lá
            else:
                print(f"Fraud Score: {fraud_score}")

            print(f"City: {city}")
            print(f"Region: {region}")

            # In Zip Code
            print("\033[91m" + f"Zip Code: {zip_code}" + "\033[0m")  # In Zip Code

            # In Proxy, VPN, Tor với màu sắc theo yêu cầu
            if proxy is False:
                print("\033[92m" + f"Proxy: {proxy}" + "\033[0m")  # Màu xanh lá
            elif proxy is True:
                print("\033[91m" + f"Proxy: {proxy}" + "\033[0m")  # Màu đỏ

            if vpn is False:
                print("\033[92m" + f"VPN: {vpn}" + "\033[0m")  # Màu xanh lá
            elif vpn is True:
                print("\033[91m" + f"VPN: {vpn}" + "\033[0m")  # Màu đỏ

            if tor is False:
                print("\033[92m" + f"Tor: {tor}" + "\033[0m")  # Màu xanh lá
            elif tor is True:
                print("\033[91m" + f"Tor: {tor}" + "\033[0m")  # Màu đỏ

        else:
            print(f"Có lỗi xảy ra khi truy cập API. Mã trạng thái: {response.status_code}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Main function
if __name__ == "__main__":
    ip, blacklists = get_ip_from_ip_score()
    if ip and blacklists:
        # In các thông tin blacklists với màu sắc
        print("Thông tin Blacklists:")
        for name, status in blacklists.items():
            if status == "clear":
                print("\033[92m" + f"{name.capitalize()}: {status}" + "\033[0m")  # Màu xanh lá
            else:
                print("\033[91m" + f"{name.capitalize()}: {status}" + "\033[0m")  # Màu đỏ

        # Gọi hàm lấy dữ liệu từ API ipqualityscore sau khi in blacklists
        get_data_from_ip_quality_score(ip)
