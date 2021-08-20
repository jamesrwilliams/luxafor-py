# Luxafor via Python

import usb.core
import usb.util

dev = usb.core.find(idVendor=0x5345, idProduct=0x1234)


def main():
    # find our device
    dev = usb.core.find(idVendor=0x04d8, idProduct=0xf372)

    # was it found?
    if dev is None:
        raise ValueError('Device not found')

    # Linux kernel sets up a device driver for USB device, which you have
    # to detach. Otherwise trying to interact with the device gives a
    # 'Resource Busy' error.
    try:
        dev.detach_kernel_driver(0)
    except Exception as e:
        pass

    dev.set_configuration()

    dev.write(1, [0, 0])

    # "red" == 82
    # "green" == 71
    # "blue" == 66
    # "yellow" == 89
    dev.write(1, [0, 82])


if __name__ == "__main__":
    main()
