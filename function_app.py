import logging
import json
from ipwhois import IPWhois
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('WHOIS lookup function processed a request.')

    ip_address = req.params.get('ip')

    if not ip_address:
        return func.HttpResponse(
            json.dumps({'error': 'No IP address provided.'}),
            status_code=400,
            mimetype='application/json'
        )

    try:
        obj = IPWhois(ip_address)
        res = obj.lookup_rdap(depth=1)

        network = res.get('network', {})
        output = {
            'inetnum': f"{network.get('startAddress', '')} - {network.get('endAddress', '')}",
            'netname': network.get('name', ''),
            'descr': network.get('remarks', [{}])[0].get('description', '') if network.get('remarks') else '',
            'country': network.get('country', ''),
            'status': network.get('status', ''),
            'admin-c': network.get('entities', []),
            'tech-c': network.get('entities', []),
            'created': network.get('events', [{}])[0].get('eventDate', '') if network.get('events') else '',
            'last-modified': network.get('events', [{}])[-1].get('eventDate', '') if network.get('events') else '',
            'source': res.get('objectClassName', '')
        }

        return func.HttpResponse(
            json.dumps(output),
            status_code=200,
            mimetype='application/json'
        )

    except Exception as e:
        logging.error(f"Error performing WHOIS lookup: {e}")
        return func.HttpResponse(
            json.dumps({'error': str(e)}),
            status_code=500,
            mimetype='application/json'
        )
