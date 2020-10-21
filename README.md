# Phonebook Kivy App

## About

It's just the first time attempt to create cross-platform app using [Kivy](https://kivy.org/#home)

Following features have been implemented at the moment:
- Create(add) contact
- Search by name
- Search by phone
- A contact could have many phones attached to it
- Delete contacts
- Contacts are stored in sqlite DB via SQLAlchemy ORM

## Install

1. clone project and cd to project dir
1. [instructions](https://kivy.org/#download) to install Kivy
1. The easiest way to install - [using wheels](https://kivy.org/downloads/appveyor/kivy/)
1. create venv and activate it
    ```zsh
    #linux/mac
    python3 -m venv env
    source ./env/bin/activate
    ```
    ```bash
    #win cmd
    python -m venv env
    .\env\Scripts\activate
    ```
1. Install dependensies:
    ```zsh
    pip install kivymd sqlalchemy
    ```

## Run it

1. cd to `src` directory
1. run
    ```zsh
    #linux/mac
    python3 main.py
    ```
    ```bash
    #win cmd
    python main.py
    ```

## Video explanation[RUS]

[Crossplatform Kivy Phonebook app](https://youtu.be/PxT8c7qP-o0)

## Previous step
- [Phonebook console app](https://github.com/dvk-net/phone-book)

## Next steps

- Create the same app as web-app usind Django
