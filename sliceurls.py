# python paramspider.py -d testphp.vulnweb.com
# create urls.txt file
# python sliceurls.py
# nuclei -l /home/kali/ParamSpider/output/{{Domain}}.txt -t /home/kali/fuzzing-critical-templates/path-*-test.yaml

import re

with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

clean_urls = set()
for url in urls:
    pattern = r'(\?|\&)[^\=]+\=[^\&]*'
    clean_url = re.sub(pattern, '', url)
    
    clean_url = clean_url.strip()
    
    clean_urls.add(clean_url)

with open('clean_urls.txt', 'w') as file:
    file.write('\n'.join(clean_urls))
