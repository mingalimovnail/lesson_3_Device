from dataclasses import dataclass
from typing import List

from devices.DeviceMode import DeviceMode


def __take_line(collection: List[str]) -> str:
    try:
        return collection.pop(0)
    except IndexError:
        raise IOError('No more for reading')

def __write_line(collection) -> str:
    try:
        collection.append('add_line')

    except IndexError:
        raise IOError('Cannot writing device')
@dataclass
class Device:
    mode: DeviceMode
    data: List[str]


def is_readable_device(device: Device) -> bool:
    """Показывает, можно ли читать из устройства."""
    return DeviceMode.ReadOnly in device.mode


def is_writable_device(device: Device) -> bool:
    """Показывает, можно писать в устройство."""
    return DeviceMode.WriteOnly in device.mode


def read_line(device: Device) -> str:
    """
    Читает строку текста из устройства
    :param device: устройство
    :return: считанная строка
    :exception IOError если строка не может быть прочитана из устройства
    :exception PermissionError если устройство не открыто на чтение
    """
    if not is_readable_device(device):
        raise PermissionError('Reading from the devices not allowed.')

    return __take_line(device.data)

def write_line(device: Device) -> str:
    """
    Записать строку на устройство
    """
    if not is_writable_device(device):
        raise PermissionError('Writing to the device is not allowed..')

    return __write_line(device.data)

def open_device(name: str) -> Device:
    """
    Открывает указанное устройство.
    :param name: имя устройства
    :return: открытое устройство
    :exception KeyError если устройство не зарегистрировано в таблице
    """
    devices = {
        '/devices/dev0': Device(DeviceMode.ReadOnly, ['line_1', 'line_2']),
        '/devices/dev1': Device(DeviceMode.WriteOnly, ['']),
        '/devices/dev2': Device(DeviceMode.ReadWrite, []),
        '/devices/dev3': Device(DeviceMode.ReadWrite, ['1', '2', '**', 'asdf', 'Nail']),
        '/devices/dev4': Device(DeviceMode.ReadOnly, ['line_1', 'line_2']),
    }

    try:
        return devices[name]
    except KeyError:
        raise IOError('Device not found')
