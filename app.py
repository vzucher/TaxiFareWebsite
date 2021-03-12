import time
import streamlit as st
import requests
import datetime
import geocoder

'''
# I ❤️️NY Taxi Fare Calculator 🔢🚖

'''

st.markdown('''
It's a plazer to meet you''')

'''
## When exatcly is the date of your trip? 📅
'''

date = st.date_input(
    "Insert the travel day here:",
    datetime.date(2021, 3, 12))

st.write('We will pick you up at:', date)

'''
## Which time would you like for us to pick you up? ⏰
'''

timet = st.time_input('Be as precise as possible :)', datetime.time(14, 30))

st.write('The current time is', timet)

'''
## Where's the specific Longitude of your pickup locs?🎯
'''
pickup_longitude = st.number_input('Insert your longitude :)')

st.write('The Longitude number is ', pickup_longitude)

'''
## Where's the specific Latitude of your pickup locs?🎯
'''
pickup_latitude = st.number_input('Insert your latitude :)')

st.write('The Latitude number is ', pickup_latitude)


'''
## Where is the specific Longitude of your dropoff locs?🚕
'''
dropoff_longitude = st.number_input('Insert your longitude')

st.write('Your destiny´s Longitude number is ', dropoff_longitude)

'''
## Where is the specific Latitude of your dropoff locs?🚕
'''
dropoff_latitude = st.number_input('Insert your latitude')

st.write('Your destiny´s Latitude number is ', dropoff_latitude)

'''
## How many passengers are travelling together?👤👥
'''
passenger_count = st.number_input('Including you yourself!', value=1)

st.write('Passenger Number:', passenger_count)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

pickup_datetime = datetime.datetime.combine(date,timet).strftime("%Y-%m-%d %H:%M:%S UTC")

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

def predict(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count):

  dictionary = {

  'key': '2012-10-06%2012:10:20.0000001',
  'pickup_datetime': pickup_datetime,
  'pickup_longitude': pickup_longitude,
  'pickup_latitude': pickup_latitude,
  'dropoff_longitude': dropoff_longitude,
  'dropoff_latitude': dropoff_latitude,
  'passenger_count': passenger_count

  }

  url = f'http://taxifare.lewagon.ai/predict_fare/'

  response = requests.get(url, params=dictionary).json()
  return response['prediction']

if st.button('Get predictions'):
    # print is visible in server output, not in the page
    prediction = predict(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count)

    'Calculating the amount of jabá it will cost you 💸💸💸...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'
    st.markdown(f''' # Your fare´s prediction is U${round(prediction, 2)} 💰''' )
    st.write('Uhul 🎉')
else:
    st.write('I was not clicked 😞')

