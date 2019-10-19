# primitiveAPI
Project for learning basics of API and connecting it with SQL database

## Installation

### Setup virtualenv

- Install virtualenvwrapper, link `python` command to `python3`.

    ```bash
    sudo pip3 install virtualenvwrapper && \
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1 && \
    source /usr/local/bin/virtualenvwrapper.sh
    ```

- Make virtualenv and switch to it

    ```bash
    mkvirtualenv flask && \
    chmod -R +x ~/.virtualenvs/ && \
    activate
    ```

- Install Flask

    ```bash
    pip3 install flask
    ```

- Create `app.py` with code and run

    ```bash
    python app.py
    ```

    