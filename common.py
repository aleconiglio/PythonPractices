import base64

def str_base64(src):
    b = base64.b64encode(bytes(src, 'utf-8'))
    return b.decode('utf-8')

def base64_str(src):
    b = base64.b64decode(bytes(src, 'utf-8'))
    return b.decode('utf-8')

def str_ip_host(src):
    iphost = src.split(":")
    ip = iphost[0]
    p = iphost[1]
    return (ip, int(p))