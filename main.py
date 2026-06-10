PORTS = {
    15: "Netstat - Medium Risk ⚠️",
    20: "FTP - High Risk 🟥",
    21: "FTP - High Risk 🟥",
    22: "SSH - Secure 🟢",
    23: "Telnet - High Risk 🟥",
    25: "SMTPn - Medium Risk ⚠️",
    53: "DNS - Medium Risk ⚠️",
    67: "BOOTP - Medium Risk ⚠️",
    68: "BOOTP - Medium Risk ⚠️",
    69: "TFTP - High Risk 🟥",
    79: "TACACS+ - High Risk 🟥", 
    49: "TACACS+ - High Risk 🟥",
    80: "HTTP - High Risk 🟥",
    88: "Kerberos - Secure 🟢",
    109: "POP3 - High Risk 🟥", 
    110: "POP3 - High Risk 🟥",
    111: "Port Map - Medium Risk ⚠️",
    119: "NNTP - Medium Risk ⚠️",
    123: "NTP - Medium Risk ⚠️",
    135-139: "NetBIOS - High Risk 🟥",
    143: "IMAP - High Risk 🟥",
    161: "SNMP - Medium Risk ⚠️",
    389: "LDAP - Medium Risk ⚠️",
    443: "SSL - Secure 🟢",
    445: "SMB - High Risk 🟥",
    500: "IPSec/ISAKMP - Secure 🟢",
    520: "RIP - Medium Risk ⚠️",
    546: "DHCP - Medium Risk ⚠️", 
    547: "DHCP - Medium Risk ⚠️",
    636: "SLDAP - Secure 🟢",
    1512: "WINS - High Risk 🟥",
    1701: "L2TP -  Secure 🟢",
    1720-323: "Medium Risk ⚠️",
    1723: "PPTP - High Risk 🟥",
    1812: "RADIUS - Secure 🟢",
    1813: "RADIUS - Secure 🟢",
    3389: "RDP - High Risk 🟥",
    5004: "RTP - Medium Risk ⚠️",
    5005: "RTP - Medium Risk ⚠️",
    5060: "SIP - Medium Risk ⚠️",
    5061: "SIP-TLS - Secure 🟢"

}

def vulnerability_scanner(port):
    if port in PORTS:
        return PORTS[port]
    else:
        return"Unknown Port"
input = input("Enter a port number: ")

port = int(input)

result = vulnerability_scanner(port)
print(f"Port: {result}") 

