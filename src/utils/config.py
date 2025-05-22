import os

def get_base_url(environment):
    environments = {
        "swagLabs": "https://www.saucedemo.com/"

    }
    return environments.get(environment, "https://default.example.com")
