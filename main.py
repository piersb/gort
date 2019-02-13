#!/usr/bin/python


print( 'Gort speaking.' )


def get_members(file):
    fp = open(file, 'r')
    members = fp.read().splitlines()
    fp.close()
    return members

members = get_members('./writers_list')

print(members[:4])
