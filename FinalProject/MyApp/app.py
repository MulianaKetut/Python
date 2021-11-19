"""
Main module of the server file
"""

# Local modules
import config


# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")

# create a URL route in our application for "/"


@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        hello
    """
    return "<h1>Deployed to Heroku</h1>"


if __name__ == "__main__":
    # connex_app.run(debug=True)
    connex_app.run(host='127.0.0.1', port=5000, debug=True)
