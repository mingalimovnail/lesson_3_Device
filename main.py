from devices.Device import *

if __name__ == '__main__':
    Num_Device = str(input('Введите номер устройства: '))
    try:
        device: Device = open_device('/devices/dev' + Num_Device)
        write_line(device)
        for i in range(len(device.data)):
            print(device.data[i])

    except Exception as exception:
        print(f'Error: {exception}')






#if __name__ == '__main__':
#    try:
#        device: Device = open_device('/devices/dev3')
#
#        for i in range(3):
#            print(read_line(device))
#
#
#        print('-----')
#
#        for i in range(3):
#            print(read_line(device))
#
#    except Exception as exception:
#        print(f'Error: {exception}')
