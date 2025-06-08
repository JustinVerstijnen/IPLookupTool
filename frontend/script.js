async function lookup() {
    const ip = document.getElementById('ipInput').value;
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = 'Loading...';
    try {
        const res = await fetch(`/api/function_app?ip=${ip}`);
        const data = await res.json();
        if (data.error) {
            resultDiv.innerHTML = `<p style='color:red;'>${data.error}</p>`;
            return;
        }
        let html = '<table>';
        for (const [key, value] of Object.entries(data)) {
            html += `<tr><th>${key}</th><td>${value}</td></tr>`;
        }
        html += '</table>';
        resultDiv.innerHTML = html;
    } catch (err) {
        resultDiv.innerHTML = `<p style='color:red;'>${err}</p>`;
    }
}