import socket
from OpenSSL import SSL
import certifi
import datetime


hostname = 'services.bq.com'
port = 443
now = datetime.datetime.now()



context = SSL.Context(method=SSL.TLSv1_METHOD)
context.load_verify_locations(cafile=certifi.where())

conn = SSL.Connection(context, socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM))
conn.settimeout(5)
conn.connect((hostname, port))
conn.setblocking(1)
conn.do_handshake()
conn.set_tlsext_host_name(hostname.encode())
certs = conn.get_peer_cert_chain()
for (idx, cert) in enumerate(certs):
    formated_date_after = datetime.datetime.strptime(cert.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
    formated_date_before = datetime.datetime.strptime(cert.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
    print(f'{idx} subject: {cert.get_subject()}')
    print(f'  issuer: {cert.get_issuer()})')
    print(f'  Valido-Desde :'  , formated_date_before)
    print(f'  Valido-Hasta :'  , formated_date_after)
    print( ' --> Expira en : ' , formated_date_after - now)
    #if (now - formated_date_after) > now:
    #    print("ERRROR Expired")
    #print(f'  fingerprint: {cert.digest("sha1")}')
    #print('----',formated_date_after)
    print()

conn.close()
