#!/usr/bin/env python3

import connexion
import os

from ios_xe_switch_connector import encoder
from dotenv import load_dotenv

load_dotenv()
PORT = os.getenv('PORT') or 8080
MODE = os.getenv('MODE') or 'development'
def main():
    from waitress import serve
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('connector.yaml', arguments={'title': 'IOS-XE switches connector'}, pythonic_params=True)
    serve(app, host="0.0.0.0", port=PORT) if MODE=='production' else app.run(port=PORT)


if __name__ == '__main__':
    main()
