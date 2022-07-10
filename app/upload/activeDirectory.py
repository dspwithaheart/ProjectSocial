import getpass
from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES

print("Authentifizierung gegen ein Active Directory")

def active_directory_auth(user, pwd):
	# Eingaben 
	# dom = input("Domain [ADS1]:") or "ADS1"
	# user = input("User [hofmannol]:") or "hofmannol"
	# print('Password:', end='')
	# pwd = getpass.getpass()
	dom = "ADS1"
	user = user
	print('Password:', end='')
	pwd = pwd

	# Binden an das AD
	server = Server('gso1.ads1.fh-nuernberg.de', get_info=ALL)
	conn = Connection(
		server, 
		user=dom+"\\"+user, 
		password=pwd, 
	#	authentication=NTLM,
	)

	conn.bind()
	print(conn)
	print(conn.extend.standard.who_am_i())
	print(conn.bound)
	auth = conn.bound
	# Suche nach dem gerade verbundenen User
	if auth:
		conn.search(
			search_base='DC='+dom+',DC=fh-nuernberg,DC=de', 
			search_filter='(&(objectclass=user)(CN='+user+'))', 
			attributes=ALL_ATTRIBUTES)
		print(conn.entries[0])

	conn.unbind()

	return auth