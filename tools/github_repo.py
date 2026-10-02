"""Create the requested private repository using the existing Git credential manager."""
import json, subprocess, urllib.request, urllib.error

def request(method, path, body=None):
    result = subprocess.run(['git','credential','fill'], input='protocol=https\nhost=github.com\n\n', text=True, capture_output=True, check=True)
    fields = dict(line.split('=',1) for line in result.stdout.splitlines() if '=' in line)
    req = urllib.request.Request('https://api.github.com'+path, method=method,
        data=None if body is None else json.dumps(body).encode(),
        headers={'Authorization':'Bearer '+fields['password'], 'User-Agent':'vpn-aion-onl','Accept':'application/vnd.github+json','Content-Type':'application/json'})
    with urllib.request.urlopen(req) as response: return json.load(response)

if __name__ == '__main__':
    assert request('GET','/user')['login'] == 'wanmeixx', 'Wrong GitHub account'
    try: repo = request('GET','/repos/wanmeixx/vpn.aion.onl')
    except urllib.error.HTTPError as error:
        if error.code != 404: raise
        repo = request('POST','/user/repos', {'name':'vpn.aion.onl','private':True,'description':'Aion updater restricted Cloudflare acceleration service','auto_init':False})
    print(repo['html_url'])
