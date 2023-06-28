import scapy.all as scapy
import optparse
# create arp request
# broadcast
# response
#scapy.ls(scapy.ARP()) scapy'nin help komutu

def get_user_input():
    parser = optparse.OptionParser()
    parser.add_option("-i","--ipadress",dest="ip_adress",help="Choose the IP adress.")
    (user_input,arguments) = parser.parse_args()
    if not user_input.ip_adress:
        print("Please enter an IP adress!!!")
    return user_input

def scan_network(ip_adress):
    arp_request_packet = scapy.ARP(pdst=ip_adress)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet  # scapy dilinde iki paketi tek paket haline getir anlamına geliyor.
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()  # özet olarak göster

user_ip_adress = get_user_input()
scan_network(user_ip_adress.ip_adress)




