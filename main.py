import interface
from interface import app
import config

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.FLASK_PORT_NUMBER,debug=True)