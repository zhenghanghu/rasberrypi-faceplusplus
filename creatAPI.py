import requests

url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'

payload = {

    'api_key':'Fn1QM4LuKANpi6l4ehA7x2A4NZxKoR8P',

    'api_secret':'c7LboSUdXAtkVpOckLNVjmbOU_nKF5h5',

    'display_name': 'face_group',

    'outer_id': 'face_group',

    'face_tokens':'7f111da2c352c379a6bfc5949ae96677,57cbd02ef3dcd0699e12ee780f9abbc9'

}



r = requests.post(url,data=payload)

print r.text
