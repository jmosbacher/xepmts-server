# -*- coding: utf-8 -*-
import os
# from xepmts.api.server.v1.settings import get_settings_dict

from xepmts_server.sc import settings as settings
settings_file = settings.__file__

def make_app(settings=settings_file, auth=None, app=None,
             swagger=False, fs_store=False,
             export_metrics=False):

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
        PrometheusMetrics(app)

    return app