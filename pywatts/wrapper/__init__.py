from pywatts.wrapper.sklearn_wrapper import SKLearnWrapper
from pywatts.wrapper.keras_wrapper import KerasWrapper
try:
    from pywatts.wrapper.pytorch_wrapper import PyTorchWrapper
except ModuleNotFoundError:
    pass

from pywatts.wrapper.function_module import FunctionModule
