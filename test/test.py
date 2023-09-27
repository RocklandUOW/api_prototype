import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('test_img2.jpg', 'rb')})

print(resp.json())