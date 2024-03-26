from flask import Flask, request, redirect
import requests

# Flask web server setup
app = Flask(__name__)

# Discord application details
CLIENT_ID = '1221661755529232404'
CLIENT_SECRET = '-7j3prDYS_rsTz2u9Rw6RWxTe841wdnq'
REDIRECT_URI = 'https://discord.com/channels/@me'  # Update with your redirect URI
SCOPE = 'identify email'  # Update with the scopes you need

# Discord OAuth2 authorization URL
AUTH_URL = f'https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}'

# Endpoint to redirect users to Discord OAuth2 for authorization
@app.route('/authorize')
def authorize():
    # Redirect user to Discord OAuth2 authorization URL
    return redirect(AUTH_URL)

# Endpoint to handle OAuth2 callback from Discord
@app.route('/callback')
def callback():
    # Get authorization code from the query parameters
    code = request.args.get('code')

    # Exchange authorization code for access token
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': SCOPE
    }
    response = requests.post('https://discord.com/api/oauth2/token', data=data)
    access_token = response.json()['access_token']

    # Use access token to fetch user data
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get('https://discord.com/api/users/@me', headers=headers)
    user_data = user_response.json()

    # Print user data
    print('User ID:', user_data['id'])
    print('Username:', user_data['username'])
    print('Discriminator:', user_data['discriminator'])
    if 'email' in user_data:
        print('Email:', user_data['email'])

    return 'User data printed in console.'

if __name__ == '__main__':
    app.run(debug=True)
