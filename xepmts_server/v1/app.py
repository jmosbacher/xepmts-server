# -*- coding: utf-8 -*-
import os
# from xepmts.api.server.v1.settings import get_settings_dict

from xepmts_server.v1 import settings
# from xepmts_server.v1.auth import XenonTokenAuth

SETTINGS_FILE = settings.__file__
from xepmts_server.utils import clean_dict

def make_app(settings=SETTINGS_FILE, auth=None, app=None,
             swagger=False, fs_store=False,
             export_metrics=True, healthcheck=True):

    kwargs = {}
    # if fs_store:
    #     from eve_fsmediastorage import FileSystemMediaStorage
    #     kwargs["media"] = FileSystemMediaStorage

    if app is None:
        from eve import Eve
        app = Eve(settings=settings, auth=auth, **kwargs)

    if swagger:
        # from eve_swagger import swagger as swagger_blueprint
        from eve_swagger import get_swagger_blueprint
        
        swagger_blueprint = get_swagger_blueprint()
        app.register_blueprint(swagger_blueprint, url_prefix=f'/{app.config["API_VERSION"]}')
        app.config['SWAGGER_INFO'] = {
            'title': 'XENON PMT API',
            'version': '1.0',
            'description': 'API for the XENON PMT database',
            'termsOfService': 'https://opensource.org/ToS',
            'contact': {
                'name': 'Yossi Mosbacher',
                'url': 'https://pmts.xenonnt.org',
                "email": "joe.mosbacher@gmail.com"
            },

            'license': {
                'name': 'BSD',
                'url': 'https://github.com/nicolaiarocci/eve-swagger/blob/master/LICENSE',
            
            },
            'schemes': ['http', 'https'],

        }

    if export_metrics:
        from prometheus_flask_exporter import PrometheusMetrics
        PrometheusMetrics(app, path=f'/{app.config["API_VERSION"]}/metrics')

    if healthcheck:
        from eve_healthcheck import EveHealthCheck
        hc = EveHealthCheck(app, f'/healthcheck')

    @app.route(f'/{app.config["API_VERSION"]}/endpoints')
    def endpoints():
        return clean_dict(app.config['DOMAIN'])
    # print("made app for  v1")
    return app


def make_local_app():
    import eve

    app = eve.Eve(settings=SETTINGS_FILE)
    return app
    
def list_roles():
    app = make_local_app()
    settings = app.config
    roles = set()
    for resource in settings["DOMAIN"].values():
        roles.update(resource["allowed_read_roles"])
        roles.update(resource["allowed_item_read_roles"])
        roles.update(resource["allowed_write_roles"])
        roles.update(resource["allowed_item_write_roles"])
    roles = list(roles)
    roles.sort(key=lambda x: x.split(":")[-1])
    return roles