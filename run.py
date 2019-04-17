from flaskblog import create_app
import os
app = create_app()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
