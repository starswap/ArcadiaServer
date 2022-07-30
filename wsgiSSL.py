from arcadia import init_app

app = init_app()

if __name__ == "__main__":
    app.run(ssl_context="adhoc",threaded=True,debug=True)