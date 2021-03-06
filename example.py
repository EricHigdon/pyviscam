#! /usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from pyviscam.broadcast import v_cams, Camera

print('----- visca bus initialisation -----')
# create a visca bus object
cams = v_cams()
# get a list of serial ports available and select the last one
ports = cams.serial.listports()
# open a connection on the serial object
cams.reset(ports[0])
v1 = cams.get_instances()[0]
print('available parameters : ')
print('-------------------------')
prop_list = [p for p in dir(Camera) if isinstance(getattr(Camera, p),property)]
for prop in prop_list:
	print(prop, v1._query(prop))


"""
v1.power = False
sleep(1)
v1.power = True
sleep(10)
v1.left()
sleep(4)
v1.stop()
sleep(0.2)
v1.home()
sleep(1)"""