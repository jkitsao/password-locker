import unittest
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
	
	def setUp(self):
		
		self.new_user = User('Ted','davis','teddy21')

	def test__init__(self):
		
		self.assertEqual(self.new_user.first_name,'Ted')
		self.assertEqual(self.new_user.last_name,'davis')
		self.assertEqual(self.new_user.password,'teddy21')

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
	
	def test_check_user(self):
		
		self.new_user = User('Jackson','kitsao','123four')
		self.new_user.save_user()
		user2 = User('Kevin','kahiga','12three')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

	def setUp(self):
		
		self.new_credential = Credential('Ken','Facebook','kenna','ken23')

	def test__init__(self):
		
		self.assertEqual(self.new_credential.user_name,'Ken')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'kenna')
		self.assertEqual(self.new_credential.password,'ken23')

	def test_save_credentials(self):
		
		self.new_credential.save_credentials()
		twitter = Credential('Dave','twitter','davy','davy21')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)


	def tearDown(self):
		
		Credential.credentials_list = []
		User.users_list = []

	def test_display_credentials(self):
		
		self.new_credential.save_credentials()
		twitter = Credential('Dave','twitter','davy','davy21')
		twitter.save_credentials()
		instagram = Credential('James','instagram','juicyme','juicy23')
		instagram.save_credentials()
		self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

	def test_find_by_site_name(self):
		
		self.new_credential.save_credentials()
		twitter = Credential('Dave','twitter','davy','davy21')
		twitter.save_credentials()
		credential_exists = Credential.find_by_site_name('Twitter')
		self.assertEqual(credential_exists,twitter)

	def test_copy_credential(self):
		
		self.new_credential.save_credentials()
		twitter = Credential('Dave','twitter','davy','davy21')
		twitter.save_credentials()
		find_credential = None
		for credential in Credential.user_credentials_list:
				find_credential =Credential.find_by_site_name(credential.site_name)
				return pyperclip.copy(find_credential.password)
		Credential.copy_credential(self.new_credential.site_name)
		self.assertEqual('davy21',pyperclip.paste())
		print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity=2)