"""Read public production routes and fail if expected page content is absent."""
import urllib.request
checks={
 'https://aaowasi.pages.dev/':'Clear evidence.',
 'https://aaowasi.pages.dev/work/':'data-project',
 'https://aaowasi.pages.dev/profile/':'Professional profile',
 'https://aaowasi-projects.pages.dev/':'Governance,',
 'https://aaowasi-projects.pages.dev/work/audit-readiness/':'Audit readiness',
 'https://aaowasi-projects.pages.dev/tools/vendor-review/':'vendor-form',
 'https://aaowasi-projects.pages.dev/assurance/':'Synthetic sample',
}
for url,expected in checks.items():
 request=urllib.request.Request(url,headers={'User-Agent':'AAO-Deployment-Check/1.0'})
 with urllib.request.urlopen(request,timeout=30) as response:
  text=response.read(2_000_000).decode()
  assert response.status==200,(url,response.status)
  assert expected in text,(url,'unexpected page content')
  print('PASS',url)
