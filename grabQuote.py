import urllib.request
import random

sample_url = 'https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=parks-and-recreation&episode=s02e12'

def parse_script(url):
    uf = urllib.request.urlopen(url)
    html = uf.read()

    html = html.decode('utf-8').splitlines()
    scriptDiv = False
    for line in html:
        if scriptDiv:
            if '</div>' in line:
                scriptDiv = False
                break
            if line != '':
                script = line
        if "<div class=\"scrolling-script-container\">" in line:
            scriptDiv = True
    
    script = script.split('<br>')
    return script

def get_quote(script):
    rand_len = random.randrange(150, 200, 1)
    rand_i = random.randrange(1, len(script)-10, 1)

    q = []
    for i in range(rand_i, len(script), 1):
        q.append(script[i])

        quote = ''.join(q)
        if len(quote) > rand_len:
            quote = quote.lstrip()
            return quote


script = parse_script(sample_url)
quote = get_quote(script)

