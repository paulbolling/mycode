#!/bin/usr/env python3

#My list 
#By Paul Bolling

my_list = [ "192.168.0.5", 5060, "UP" ]

print("The first item in the list (UP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print( "The last item in the list (state): " + my_list[2] )

#New list

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]


print('When I have ports ' + str(new_list[0]) + ' ' + str(new_list[1]) + ' '+ str(new_list[2]) + ' open, it lets ' + str(new_list[3]) + " " + str(new_list[4]) + ' be my IP ' + ' as long as I am using ' + str(new_list[5]))