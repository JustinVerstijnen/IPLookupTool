document.getElementById('lookup-btn').addEventListener('click', function() {
    const ip = document.getElementById('ip-address').value;
    if (!ip) {
        alert('Please enter an IP address');
        return;
    }

    fetch(`https://<YOUR-FUNCTION-URL>/api/iplookup?ip=${ip}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `
                <h2>IP Information</h2>
                <p><strong>ASN:</strong> ${data.ASN}</p>
                <p><strong>Hostname:</strong> ${data.Hostname}</p>
                <p><strong>Company:</strong> ${data.Company}</p>
                <p><strong>City:</strong> ${data.IP_Geolocation.City}</p>
                <p><strong>Country:</strong> ${data.IP_Geolocation.Country}</p>
                <p><strong>Coordinates:</strong> ${data.IP_Geolocation.Coordinates}</p>
            `;
        })
        .catch(error => {
            document.getElementById('result').innerHTML = 'Error fetching data.';
        });
});
