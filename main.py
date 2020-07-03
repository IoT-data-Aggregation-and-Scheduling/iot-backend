import api
import os


def fetch_credentials(env):
    config = {}
    if env in ['local', 'dev']:
        config['env'] = env
        
        return config

if not os.getenv('DEPLOYMENT_ENVIRONMENT'):
    os.environ['DEPLOYMENT_ENVIRONMENT'] = "local"

config = fetch_credentials(os.environ["DEPLOYMENT_ENVIRONMENT"])
app = announce.create_app(config)

if __name__ == '__main__':
    
    if os.getenv('DEPLOYMENT_ENVIRONMENT') != "local":
        app.run(host='127.0.0.1', port=8080)
    else:
        app.run(host='127.0.0.1', port=8080, ssl_context="adhoc")