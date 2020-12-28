# allauth

I want a demo that shows how to use django-allauth for:

1. email + password registration
2. social login for Facebook, Twitter, Google, LinkedIn, Microsoft (hotmail account)
3. A separate profile table to store user profile (for now, the profile table will just contain screenname)
4. Provide examples of overriding:
	i. The login/registration forms and template
	ii The password recovery template
5. Functional and unit tests to show that the requested functionality works as expected

The detailed requirements are set out below:

## functional requirements
1.  user can register using ONLY email
	i.  email is checked against banned lists of emails and verification fails if email is in banned domain list. If email is in banned domain list, fail SILENTLY. However, if domain passes proceed to registration workflow (next step below)
	
	ii. registration workflow:
	unique token (with time expiry set in settings.py) is sent to email address
	alert notification given on front end saying 'thank you, email sent to xxx'
	user logs in using URL+token
	user is then required to provide:
	first name and surname and password (password + confirm password field on form)
	UNIQUE alphanumeric screename (settings.MIN_SCREENNAME_LEN, settings.MAX_SCREENNAME_LEN) which is checked against a list of badnames before user is created in the system (also checked for uniqueness against database, and alternatives suggested - with numbers appended for example, if screenname already exists - user given choice to enter new screenname or select one of the suggested alternatives)
    user has option to load profile picture - else gravatar is used to fetch user profile image (if user dosen't provide photo)
    iii. lost password workflow:
        a). timed expiring token sent to email, user allowed to click link and reset password

2. A successfully registered user can login using email and password
   i). test email + pwd login is protected against DOS attacks


3. user can register using either of these:
   FB, Twitter, LinkedIn, Google, MS Live (hotmail account)

   i. When registering new user through social login, grab profile picture from social image if possible (if fails, use gravatar - based on social account email)
   ii. auto generate UNIQUE screen name based on first_name and last_name (whilst checking that generated name is not in banned list of words)

4.  A (previously) registered user who has lost their password can request a link to be sent to them.
    i. A message will be displayed saying that 'If the email is registered to us, you will receive link'
    ii. A time restricted (interval in settings.py) token is sent to user, if user clicks on before expiry, they are allowed to reset their password, if clicked after password, they should directed to a page informing them that 'link expired' and presented with option to ask for new link to be sent.

5. If someone attempts to login with a social account that has an email that is already in the database (with a registered user), they should be informed 'A user with this email account already exist' and redirected to a page that asks for email and password login.

6. If someone attempts to register with an email that already has a social media account associated with it, they should be informed:  'A user with this email account already exist' and redirected to a page that asks for email and password login.