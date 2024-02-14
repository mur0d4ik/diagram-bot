import io
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


async def string_to_list(name: str, input_string: str) -> list[list: list]:

    pairs = [pair.split(':') for pair in input_string.split(',')]

    key_list = [str(pair[0]) for pair in pairs]
    value_list = [int(pair[1]) for pair in pairs]

    return [key_list, value_list]

async def generate_diagrams(name: str, key: list, value: list):
    buffer = io.BytesIO()
    fig, ax = plt.subplots()

    if name == 'defalute':
        ax.plot(key, value)

    elif name == 'circle':
        ax.pie(value, labels=key, autopct='%1.1f%%')

    elif name == 'stek':
        ax.bar(key, value)

    elif name == 'dot':
        ax.scatter(key, value)

    elif name == 'stack':
        ax.stackplot(key, value, labels=key, alpha=0.8)

    plt.savefig(buffer, format='png', dpi=300)
    buffer.seek(0)

    return buffer.read()
