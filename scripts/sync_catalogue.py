"""Pull the public projects catalogue; validate before replacing the local snapshot."""
from pathlib import Path
import json, urllib.request
root=Path(__file__).resolve().parents[1]
url='https://raw.githubusercontent.com/aaowasi/aaowasi-projects/main/content/projects.json'
with urllib.request.urlopen(url,timeout=30) as response:
 data=json.loads(response.read(2_000_000))
assert isinstance(data,list)
for p in data:
 assert all(isinstance(p.get(k),str) for k in ('id','slug','title','type','domain','summary'))
(root/'content/projects.json').write_text(json.dumps(data,indent=2))
