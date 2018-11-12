# client_clp.py
# Read and decode PLC S7-1200 digital and Analog inputs
# Author: Bruno Duarte <brduarte95@gmail.com>

from pymodbus.client.sync import ModbusTcpClient as ModbusCLient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
from time import sleep
import mel_debug as debug


def main():
    # IP = input("Slave IP: ")
    # ID = input("Slave ID: ")
    IP = "192.168.0.13"
    ID =2

    client = ModbusCLient(IP,port = 502)


    if client.connect() == False:
        debug.error("Unable to connect to PLC")
        return
    while True:


        payload = client.read_holding_registers(0,1, unit = ID)
        # print(payload.bits)

        decoder = BinaryPayloadDecoder.fromRegisters(payload.registers,
                                                        byteorder = Endian.Little,
                                                        wordorder = Endian.Big)
        port_0 = decoder.decode_bits()

        payload = client.read_holding_registers(1,1, unit=ID)

        decoder = BinaryPayloadDecoder.fromRegisters(payload.registers,
                                                        byteorder = Endian.Big,
                                                        wordorder = Endian.Little)
        port_1 = decoder.decode_bits()

        debug.info("Input 0: {}".format(port_0))
        q_0 = port_0[0]
        debug.debug(q_0)
        debug.info("Input 1: {}".format(port_1))

        # decoded = OrderedDict([
        # ('Port_0', decoder.decode_bits()),
        # ('Port_1', decoder.decode_bits()),
        # # # ('Analog_1', decoder.decode_32bit_int()),
        # # # ('Analog_2', decoder.decode_16bit_int()),
        # ])
        #
        # for name,value in iteritems(decoded):
        #     debug.info("{}: {}\t".format(name,value))
        # print("vida: {}".format(decoder.decode_bits()))
        # print(payload.registers)
        # print("Bits: {}".format(decoder.decode_bits(1)))

        payload = client.read_holding_registers(2,2, unit = ID)

        debug.debug("Payload: {} {}".format(payload.getRegister(0),payload.getRegister(1)))

        # decoder = BinaryPayloadDecoder.fromRegisters(payload.registers,
        #                                                 byteorder = Endian.Little,
        #                                                 wordorder = Endian.Little)
        # decoded = OrderedDict([
        # # ('Port_0', decoder.decode_bits()),
        # # ('Port_1', decoder.decode_bits()),
        # ('Analog_1', decoder.decode_16bit_int()),
        # ('Analog_2', decoder.decode_16bit_int()),
        # ])
        #
        #

        sleep(10)


        builder = BinaryPayloadBuilder(byteorder = Endian.Big,
                                        wordorder = Endian.Little)

        builder.add_bits([1,1,0,0,0,0,1,0])

        payload = builder.to_registers()

        debug.debug(payload)


        client.write_registers(4,payload,unit = ID)







        # builder = BinaryPayloadBuilder(byteorder = Endian.Big,
        # wordorder = Endian.Little)
        #
        # builder.add_bits([1,0,0,1,0,0,1,1])
        # debug.debug("Payload sent: {}".format(builder.to_registers()))
        # casa = builder.to_registers()
        #
        #
        # client.write_registers(5, casa, unit = 2)
        #
        # sleep(5)


if __name__ == '__main__':
    main()
