from chat.app import app, run_app, utils  # noqa
import logging
import eventlet
from flask_session import Session
from chat.config import get_config
from flask_cors import CORS
from flask_socketio import SocketIO
from chat.socketio_signals import io_connect, io_disconnect, io_join_room, io_on_message

utils.init_redis()
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.logger.debug('this will show in the log')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config.from_object(get_config())
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", allow_headers="*", manage_session=False)

# this was rewritten from decorators so we can move this methods to another file
socketio.on_event("connect", io_connect)
socketio.on_event("disconnect", io_disconnect)
socketio.on_event("room.join", io_join_room)
socketio.on_event("message", io_on_message)

if __name__ == "__main__":
    # monkey patch is "required to force the message queue package to use coroutine friendly functions and classes"
    # check flask-socketio docs https://flask-socketio.readthedocs.io/en/latest/
    
    eventlet.monkey_patch()
    run_app(socketio)
