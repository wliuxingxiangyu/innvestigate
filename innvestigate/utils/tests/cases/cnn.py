# Get Python six functionality:
from __future__ import\
    absolute_import, print_function, division, unicode_literals


###############################################################################
###############################################################################
###############################################################################


import numpy as np

from .... import backend

from . import helper


__all__ = [
    "cnn_1dim_c1_d1",
    "cnn_1dim_c2_d1",
    "cnn_2dim_c1_d1",
    "cnn_2dim_c2_d1",
    "cnn_3dim_c1_d1",
    "cnn_3dim_c2_d1",
]


###############################################################################
###############################################################################
###############################################################################


def _cnn(dim, n_conv, n_dense):
    # Add one additional axis for the channels.
    if dim == 1:
        input_shape = (1, 16, 16)
        kernel_size = (2,)
    elif dim == 2:
        input_shape = (1, 16, 16, 16)
        kernel_size = (2, 2)
    elif dim == 3:
        input_shape = (1, 16, 16, 16, 16)
        kernel_size = (2, 2, 2)
    else:
        raise ValueError("Dimensionality must be either 1, 2, or 3.")
    data = np.random.rand(*input_shape)

    if backend.name() == "tensorflow":
        layers = backend.keras.layers
        if dim == 1:
            Conv = layers.Conv1D
            Pool = layers.MaxPooling1D
        elif dim == 2:
            Conv = layers.Conv2D
            Pool = layers.MaxPooling2D
        elif dim == 3:
            Conv = layers.Conv3D
            Pool = layers.MaxPooling3D

        inputs = layers.Input(shape=input_shape[1:])
        tmp = inputs
        for i in range(n_conv):
            tmp = Conv(2, kernel_size, activation="relu")(tmp)
        tmp = Pool()(tmp)
        for i in range(n_dense):
            tmp = layers.Dense(units=1, activation="linear")(tmp)
        outputs = tmp
        model = helper.build_keras_model(inputs, outputs)
    else:
        raise NotImplementedError()

    return model, data


def cnn_1dim_c1_d1():
    return _cnn(1, 1, 1)


def cnn_1dim_c2_d1():
    return _cnn(1, 2, 1)


def cnn_2dim_c1_d1():
    return _cnn(2, 1, 1)


def cnn_2dim_c2_d1():
    return _cnn(2, 2, 1)


def cnn_3dim_c1_d1():
    return _cnn(3, 1, 1)


def cnn_3dim_c2_d1():
    return _cnn(3, 2, 1)
