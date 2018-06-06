#!/usr/bin/env python3
firewallports = [ 5060, 5061, 80, 443, 22, 25565 ]
def addTen(x):
    return x%10
print('Currently firewallports looks like this: ' + str(firewallports))
print('\nThe results of sorted(firewallports, key=addTen) function:', sorted(firewallports, key=addTen))
print('\nBut firewallports has not actually changed:', firewallports)