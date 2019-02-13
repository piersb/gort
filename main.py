#!/usr/bin/python


print( 'Gort speaking.' )

fp = open('./writers_list', 'r')

members = fp.read().splitlines()

fp.close()