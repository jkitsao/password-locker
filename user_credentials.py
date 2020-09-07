import pyperclip
import random
import string

# Global Variables
global users_list 
class User:
	
	users_list = []
	def __init__(self,first_name,last_name,password):
		

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		
		User.users_list.append(self)
		
class Credential:
	
	credentials_list =[]
	user_credentials_list = []
	@classmethod
	def check_user(cls,first_name,password):
		
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,user_name,site_name,account_name,password):
		

		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_credentials(self):
		
		Credential.credentials_list.append(self)
	
	def generate_password(self,size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass

	@classmethod
	def display_credentials(cls,user_name):
		
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list
				

	
	@classmethod
	def find_by_site_name(cls, site_name):
		
		for credential in cls.credentials_list:
			if credential.site_name == site_name:
				return credential

	@classmethod
	def copy_credential(cls,site_name):
		
		find_credential = Credential.find_by_site_name(site_name)
		return pyperclip.copy(find_credential.password)