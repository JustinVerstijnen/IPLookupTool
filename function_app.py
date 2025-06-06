import logging
import whois
import socket
import requests
import azure.functions as func
import json

def get_ip_info(ip_address):
    try:
        whois_info = whois.whois(ip_address)
    except Exception as e:
        logging.error(f"Error fetching WHOIS data for {ip_address}: {e}")
        whois_info = {}

    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
    except socket.herror as e:
        logging.error(f"Error fetching hostname for {ip_address}: {e}")
        hostname = "N/A"
    
    try:
        geolocation_url = f"http://ip-api.com/json/{ip_address}"
        geo_response = requests.get(geolocation_url)
        geo_info = geo_response.json()
    except Exception as e:
        logging.error(f"Error fetching geolocation for {ip_address}: {e}")
        geo_info = {}

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
    ip = req.params.get('ip')
    if not ip:
        return func.HttpResponse(
            json.dumps({"error": "IP address not provided"}), 
            status_code=400, 
            mimetype="application/json"
        )

    try:
        info = get_ip_info(ip)
        return func.HttpResponse(
            json.dumps(info), 
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"Error processing IP {ip}: {e}")
        return func.HttpResponse(
            json.dumps({"error": "Error processing IP address"}), 
            status_code=500, 
            mimetype="application/json"
        )
