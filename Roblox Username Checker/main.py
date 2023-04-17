
import requests, json, os
def clear():
  os.system("clear")
  os.system("cls")
  os.system("title cuts")
clear()

def checkuser(user):
	r = requests.get("https://auth.roblox.com/v1/usernames/validate?birthday=2000-01-01T00:00:00.000Z&context=Signup&username=" + user)
	resp = json.loads(r.text)
	res = resp['message']
	return res

with open("users.txt") as f:
	lines = f.readlines()
	for line in lines:
		user = line.rstrip()
		response = checkuser(user)
		if response == "Username is valid":
			print(f" O [SUCCESS] [{user}] : {response}")
			with open("checked\\valid.txt", "a") as f:
				f.write(user + "\n")
		else:
			print(f" X [INVALID] [{user}] : {response}")
			if response == "Username not appropriate for Roblox":
				with open("checked\\inappropriate.txt", "a") as f:
					f.write(user + "\n")
			elif response == "Username is already in use":
				with open("checked\\used.txt", "a") as f:
					f.write(user + "\n")
			else:
				with open("checked\\invalid.txt", "a") as f:
					f.write(user + "\n")
		f.close()