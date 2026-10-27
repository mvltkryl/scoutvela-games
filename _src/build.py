import re, sys
S = sys.argv[1]
src = open(S + '/index.html').read()
head = src.split('<main>')[0]
foot = '<footer>' + src.split('<footer>')[1]
pages = {
  'privacy.html': ('Privacy Policy · ScoutVela Games', 'Privacy policy for Donut Destroyer, Strategic Rescue Operation and Block Isles by ScoutVela Games.'),
  'support.html': ('Support · ScoutVela Games', 'Player support and account deletion for ScoutVela Games.'),
}
for name, (title, desc) in pages.items():
    body = open(S + '/_src/' + name.replace('.html', '.body.html')).read()
    h = head.replace('<title>ScoutVela Games</title>', '<title>' + title + '</title>')
    h = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + desc + '">', h)
    h = h.replace('href="#games"', 'href="./#games"').replace('href="#studio"', 'href="./#studio"')
    h = h.replace('<a href="' + name + '">', '<a href="' + name + '" aria-current="page">')
    f = foot.replace('href="#games"', 'href="./#games"')
    open(S + '/' + name, 'w').write(h + '<main class="doc">\n' + body + '</main>\n\n' + f)
