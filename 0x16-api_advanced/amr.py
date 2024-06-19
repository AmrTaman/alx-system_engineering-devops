import requests

def get_user_agent():
        url = "https://httpbin.org/user-agent"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['user-agent']
        else:
            return f"Failed to retrieve user agent: {response.status_code}"
if __name__ == "__main__":
    user_agent = get_user_agent()
    print(f"Your user agent is: {user_agent}")
