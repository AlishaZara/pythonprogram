user={
    'username':'alisha',
    'password':'alisha123'
}
username=input('user name please...')
password=input('password please...')
if username!=user['username']:
    print('username is valid')
else:
    print('username is invalid')
if password!=user['password']:
    print('password is valid')
else:
    print('password is invalid')
    