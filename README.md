# IP Lookup Tool

A simple IP WHOIS lookup tool that queries public WHOIS data for both IPv4 and IPv6 addresses. The tool is built with Azure Static Web Apps and Azure Functions using Python, HTML, CSS, and JavaScript.

## What does this tool do?

- Accepts any valid IPv4 or IPv6 address
- Queries public WHOIS information using RDAP protocol (no API key required)
- Displays ownership and registration details such as:
  - IP range (inetnum)
  - Netname
  - Description
  - Country
  - Administrative contacts
  - Technical contacts
  - Status
  - Creation date
  - Last modified date
  - Source registry
- No personal or private information is retrieved — only publicly available IP ownership data.

## How to use

1. Enter any valid IP address (IPv4 or IPv6) in the search field.
2. Click the **Lookup** button.
3. The public WHOIS information will be displayed in a structured table format.

## Clone and deploy your own version

You can easily host your own copy of this tool using Azure Static Web Apps.

### Clone this repository

```bash
git clone https://github.com/your-username/IPLookupTool.git
cd IPLookupTool
```

### Azure deployment steps

1. Create a new **Azure Static Web App** in your Azure portal.
2. Link your GitHub repository to the Static Web App.
3. Use the following build settings:
   - **App location:** `frontend`
   - **API location:** `api`
   - **Output location:** leave empty
4. Azure will automatically detect the Azure Function and install dependencies from `requirements.txt`.

## License

This project is licensed under the MIT License.