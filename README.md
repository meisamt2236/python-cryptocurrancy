**Install requirements:**
```
pip3 install -r requirements.txt
```
**Making virtual environment in directory using:**
```
python3 -m venv blockchain-env
```
**Activating virtual environment:**
```
source blockchain-env/bin/activate
```
**To test modules:**
```
python3 -m pytest backend/tests
```
**To run modules:**
```
python3 -m backend.blockchain.block
```
**To run the application(API):**
```
python3 -m backend.app
```
**Sign up in pubnub.com and make an app. Then make a file in backend folder called pubnub.py**
**Write these code in that file:**
```
PUBLISH_KEY = 'Your application publish key'
SUBSCRIBE_KEY = 'Your application subscribe key'
```
**To run a peer instance:**
```
export PEER=True && python3 -m backend.app
```
**Postman:( localhost:5000/wallet/transact -> POST -> body -> raw -> JSON )**
```
{"recipient": "foo", "amount": 15}
```
**To run the frontend go to frontend directory and run this:**
```
npm install && npm start
```
**To seed the backend with data:**
```
export SEED_DATA=True && python3 -m backend.app
```