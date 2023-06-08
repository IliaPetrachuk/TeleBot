from .custom_handlers import history
from . import custom_handlers
from . import callback_handlers
#Все функции прописываем перед default_handlers, во избежание срабатывания echo
from . import default_handlers
