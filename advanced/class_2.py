class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class AdminUser(User):
    def __init__(self, username, email, role):
        # this row means that this paramaters will be taken from higher class
        # since 'AdminUser' is extension of 'User', [username, email] will be taken from og class
        super().__init__(username, email)
        self.role = role
        self.is_admin = True


my_admin = AdminUser('admin123', 'admin@admin.com', 'Administrator')
my_user = User('user123', 'user@user.com')

my_admin.__dict__
# {'username': 'admin123', 'email': 'admin@admin.com', 'role': 'Administrator', 'is_admin': True}
my_user.__dict__
# {'username': 'user123', 'email': 'user@user.com'}
