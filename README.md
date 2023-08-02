# Streamlit MotherDuck connection

Connect to MotherDuck from your Streamlit app. Powered by `st.experimental_connection()`

## Develop locally

First, install the requirements `pip install`. 

1. Add a folder `.streamlit` in the root directory.
2. Add a file `secrets.toml`.
3. Paste your service token from Motherduck.

```
MOTHERDUCK_SERVICE_TOKEN="ey********"
```

4. streamlit run apps.py

## Deploy to Streamlit Community Cloud

1. Create a new app at [https://share.streamlit.io/](https://share.streamlit.io/).
2. Set the Main file path to `app.py`
3. Deploy.
4. You should get an error that MOTHERDUCK_SERVICE_TOKEN is undefined.
5. Go to your Streamlit app settings and paste the contents of your local `secrets.toml` file. 

```
MOTHERDUCK_SERVICE_TOKEN="ey********"
```