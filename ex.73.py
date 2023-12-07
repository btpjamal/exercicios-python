times_brasileirao= ('palmeiras','botafogo','gremio','bragantino','atlético-mg','flamengo','atlético-pr','fluminense','cuiabá','são paulo','corinthians','fortaleza','internacional','santos','vasco','cruzeiro','bahia','goiás','coritiba','américa-mg')

print(f'Os 5 primeiros times são: {times_brasileirao[:5]}')
print(f'Os ultimos 4 colocados são: {times_brasileirao[16:]}')
print(f'Times em ordem alfabética: {sorted(times_brasileirao)}')
print(f'O são paulo aparece na posição: {times_brasileirao.index('são paulo')}')