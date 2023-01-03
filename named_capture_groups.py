import re
# The P indicates that it's specific to Python
m = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Lucia Kelley')
print(m.groupdict())

# You can use any name you want between < and >  It doesn't have to be "domain".
# This regex is for finding ONLY the domain name portion of a URL (See Codewars)
def domain_name(url):
    return re.search('(?P<protocol>https?://)?(www\d?\.)?(?P<domain>[\w-]+)\.', url).group('domain')

print(domain_name("https://www.nytimes.com"))
print(domain_name("http://regex101.org"))
print(domain_name("http://troykelley.online"))
print(domain_name("http://www.slas.edu"))
print(domain_name("http://www2.netflix.tv"))