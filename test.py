from utils import Utils

user = Utils()

user_data = user.create_user()
response = user.auth_user(user_data["email"], user_data["password"])
token = response.json()['accessToken']

order = user.get_order_created_number(token)
print(order)

