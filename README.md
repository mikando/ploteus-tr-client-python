## Python Client for Ploteus Turkey Integration Pool

##$ Example usage:

```python
from ploteus_tr_client import ploteus_client

with open('lo_full_sample.xml', 'r', encoding='utf-8-sig') as file:
    loXmlContent =  file.read()
    ploteus_client = ploteus_client("USER_NAME", "PASSWORD")
    result = ploteus_client.upload_learning_opportunities_xml(loXmlContent)
```
