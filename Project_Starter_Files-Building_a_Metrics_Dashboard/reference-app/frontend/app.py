from flask import Flask, render_template, request
from jaeger_client import Config
from flask_opentracing import FlaskTracing
from opentracing_instrumentation.client_hooks import install_all_patches

app = Flask(__name__)
# creating my configuration object for all requests
logging.get.Logger('').handlers = []
logging.basicConfig(format='%(message)s', level=logging.DEBUG)
config = Config(
    config={
        'sampler':
        {'type': 'const',
         'param': 1},
                        'logging': True,
                        'reporter_batch_size': 1,}, 
                        service_name="frontend")
jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer, True, app)

#i also want to trace all requests 
install_all_patches()
test()

@app.route("/")
def homepage():
    return render_template("main.html")

def test():
    # Adding the span feature...
     with tracer.start_span('frontSpan') as span:
        req = requests.get('https://147.182.198.136:3000.com') # ping my own grafana
        span.set_tag('http.method;', req)
        def format():
            with tracer.start_span('front-span') as span:
                try:
                    print("started tracing!")
                except:
                    print("start jaeger tracing!")

if __name__ == "__main__":
    app.run()
