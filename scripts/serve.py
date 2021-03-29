from xepmts_server import create_app
from werkzeug.serving import run_simple

def run(address='0.0.0.0', port=5000, debug=True, reload=True, evalex=True):
    app = create_app()
    run_simple(address, port, app,
                use_reloader=debug, use_debugger=reload, use_evalex=evalex)

if __name__ == '__main__':
    run()

