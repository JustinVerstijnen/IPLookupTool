import logging
import whois
import socket
import requests
import azure.functions as func

def get_ip_info(ip_address):
    # WHOIS informatie ophalen
    whois_info = whois.whois(ip_address)
    
    # DNS hostname ophalen
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        hostname = "N/A"
    
    # Geolocatie-informatie ophalen (via een openbare API)
    geolocation_url = f"http://ip-api.com/json/{ip_address}"
    geo_response = requests.get(geolocation_url)
    geo_info = geo_response.json()
    
    # Gegevens verzamelen
    info = {
        'ASN': whois_info.get('asn', 'N/A'),
        'Hostname': hostname,
        'Range': whois_info.get('range', 'N/A'),
        'Company': whois_info.get('org', 'N/A'),
        'IP Geolocation': {
            'City': geo_info.get('city', 'N/A'),
            'State': geo_info.get('regionName', 'N/A'),
            'Country': geo_info.get('country', 'N/A'),
            'Postal': geo_info.get('zip', 'N/A'),
            'Local Time': geo_info.get('timezone', 'N/A'),
            'Coordinates': f"{geo_info.get('lat', 'N/A')},{geo_info.get('lon', 'N/A')}"
        }
    }
    
    return info

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Haal het IP-adres uit de query string
    ip = req.params.get('ip')
    if not ip:
        return func.HttpResponse("Please pass an IP address in the query string", status_code=400)
    
    info = get_ip_info(ip)
    
    return func.HttpResponse(
        str(info),  # Je kunt de output ook als JSON formatteren
        mimetype="application/json"
    )
