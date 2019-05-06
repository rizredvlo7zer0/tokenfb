import requests, json, time, os
hees = raw_input("Username/Email/ID Facebook: ")
molor = raw_input("Password: ")
gaskeun = requests.get("https://b-api.facebook.com:443/method/auth.login?format=json&device_id=fa0agkaj-zgzs-ih1j-rs00-6etvjwmgv9va&email="+(hees)+"&password="+(molor)+"&cpl=true&family_device_id=fa0agkaj-zgzs-ih1j-rs00-6etvjwmgv9va&sim_serials=%5B%2289014103478080510720%22%5D&credentials_type=password&generate_session_cookies=1&error_detail_type=button_with_disabled&locale=en_US&client_country_code=US&method=auth.login&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662")
try:
	komenk = json.loads(gaskeun.text)
	ucuy = gaskeun.content
	if "EA" in ucuy:
		print ("Your token is:")
		print (komenk['access_token'])
	elif "405" in ucuy:
		print ("Generate Failed!, Your Account Checkpoint")
	else:
		print ("Wrong Username Or Password")
except:
	pass
