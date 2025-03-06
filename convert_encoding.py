import codecs
import os

def convert_file(infile, outfile, source_enc='utf-16', target_enc='utf-8'):
    with codecs.open(infile, 'r', source_enc) as fin:
        content = fin.read()
    with codecs.open(outfile, 'w', target_enc) as fout:
        fout.write(content)
    print(f"Convertido {infile} a {outfile} con codificación {target_enc}.")

# Rutas relativas a la raíz del proyecto
convert_file(
    os.path.join('pages', 'fixtures', 'initial_pages.json'),
    os.path.join('pages', 'fixtures', 'initial_pages_utf8.json'),
    source_enc='utf-16', target_enc='utf-8'
)

convert_file(
    os.path.join('blog', 'fixtures', 'initial_posts.json'),
    os.path.join('blog', 'fixtures', 'initial_posts_utf8.json'),
    source_enc='utf-16', target_enc='utf-8'
)
