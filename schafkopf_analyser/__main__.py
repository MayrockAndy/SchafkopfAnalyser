from waitress import serve

from schafkopf_analyser import create_app

serve(create_app(), host='127.0.0.1', port="5000")
