from datamodels import NetworkHop
from scapy.layers.inet import UDP, traceroute
import argparse
from sys import argv
from re import match


def mapRoute(dest: str):
    result, err = traceroute(target=dest)
    print(result, err)

def initializeArgparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options] ip_or_dns_host",
        description="Trace a route and create a graph of the hops!"
    )
    parser.add_argument("-t", "--type")
    parser.add_argument("-d", "--domain-name")
    parser.add_argument("-i" ,"--ip-address")
    return parser

if __name__ == "__main__":
    parser = initializeArgparser()
    args = parser.parse_args()
    if not args.type:
        print("Please choose an action type")
    if args.type == "map":
        if args.domain_name:
            targetDomain = args.domain
            print(f"Mapping route to domain {targetDomain}")
        elif args.ip_address:
            targetIp = args.ip_address
            if match("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", targetIp):
                print(f"Mapping route to IPv4 address {targetIp}")
                mapRoute(targetIp)
            else:
                print(f"Your entered IP did not pass verification, please enter a valid IPv4 address.")



