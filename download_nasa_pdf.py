import requests

URL = "https://www.nasa.gov/wp-content/uploads/2021/12/sls_fact_sheet.pdf"

response = requests.get(URL, headers={'userid': 'credential-value'})
if response.ok:
    with open('nasa_brochure.pdf', 'wb') as nasa_out:
        nasa_out.write(response.content)
