from project import app, config


if __name__ == '__main__':
    app.run(host=config.flask.host, port=config.flask.port, debug=True)