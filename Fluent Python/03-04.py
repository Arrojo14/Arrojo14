# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:00:27 2021

@author: larro
"""

if 1==-1: # Crear un diccionario rápidamente a partir de una lista  múltiple con varios intraelementos  
    DIAL_CODES = [ 
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
    ] 
    
    dCountCode={country: code for code, country in DIAL_CODES}
    print(dCountCode)
    
    dUPPERCountCode= {country.upper(): code for code, country in DIAL_CODES}
    print(dUPPERCountCode)

if 1==-1: # El código simplemente tiene demasiados agujeros aunque sea un ejemplo, bastante inutil.
    import sys
    import re
    WORD_RE = re.compile('\w+')
    index = {}
    with open(sys.argv[1], encoding='utf-8') as fp:
     for line_no, line in enumerate(fp, 1):
         for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location) 
    
    for word in sorted(index, key=str.upper):
     print(word, index[word])


if 1==-1:
    
    dic={
    "Alfombra": 13,
    "Cascos": 12,
    "Pendientes": 11,
    "key":9
    }
    
    if "key" not in dic:
        dic["key"]=10
    
    print(dic)
     

if 1==-1: # Aprovechándote de la subclase "dict" creas una nueva clase de deccionarios con los añadidos deseados, en este caso la posibilidad de buscar sin diferenciar int o str en la key de entrada
    class StrKeyDict0(dict):
        def __missing__(self,key):
            if type(key)==str:
                return KeyError(key)
            else:
                return self[str(key)]
        
        def get(self, key, default=None):
            try:
                return self[key] 
            except KeyError:
                return default 
            def __contains__(self, key):
                return key in self.keys() or str(key) in self.keys()
            
    
    d = StrKeyDict0({
    "2":"dos",
    "4":"cuatro"
    })
    
    print(d.get(2))
    print(4 in d)


if 1==-1: #Crea un diccionario con entrada cada letra que aparezca y salida el nº de veces que se repite
    import collections
    
    ct=collections.Counter("abracadabra") 
    print(ct)
    ct.update("ddddd") #Añade al conteo de letras sin eliminar las marcas anteriores
    print(ct)
    print(ct.most_common(1))



if 1==-1: #Similar a la clase creada anteriormente pero guarda cada nueva entrada y salida como str
    import collections
    
    class StrKeyDict(collections.UserDict): 
        def __missing__(self, key): 
         if isinstance(key, str):
             raise KeyError(key)
         return self[str(key)]
    
        def __contains__(self, key):
            return str(key) in self.data
        
        def __setitem__(self, key, item):
            self.data[str(key)] = item
    
    
    
if 1==-1:  # Básicamente el MappingProxyType crea una ventana hacía el diccionario original desde la cual se puede leer pero no editar, algo parecido al memoryview con los arrays
    
    import types as t
        
        
    d= {1:"A"}
    dt= t.MappingProxyType(d)
    print(d[1])
    print(d)
    
    

if 1==-1: # Un set es una colección de elementos no repetidos que se puede usar para eliminar items que se reptien varias veces en un array *TODOS SUS ELEMENTOS DEBEN SER HASHABLES, SIN EMBARGO EL SET EN SÍ NO ES HASHABLE A MENOS QUE APLIQUEMOS FROZENSET*
    
    x=[1,2,3,4,1,1,3,4,1,1] # Creo un list
    x=set(x) # Lo puedo convertir a set para eliminar repetidos ya que todos sus elementos son hashables
    print(x)
    x=list(x) # Lo transformo a lista otra vez ya que ya he eliminado los repetidos
    print(x)
    x=frozenset(x) # Ahora quiero saber el hash de la nueva lista, así que la transformo en frozenset
    print(hash(x)) # Listo

    
if 1==-1: # En caso de tener dos sets con distintos datos y querer comprobar cuantos coincide, podremos usar la función len(obj1 $ obj2)
    number_haystack={1,2,3,4,5,6,7,8,9}
    needles={1,2,4,9}
      
    # Método 1
    found = 0
    for n in needles:
     if n in number_haystack:
         found += 1 
    print(found)
    
    # Método 2 (mejor)
    print(len(needles & number_haystack))
    
    
if 1==-1:   
    setz={1}
    print(type(setz))
    setz.pop()
    print(setz)
    setz.add("ey")
    print(setz)
    setz.add("nose")
    print(setz)
    
if 1==-1: # Básicamente creamos un diccionario a partir de una lista con el comando dict()
    
    DIAL_CODES = [
     (86, 'China'),
     (91, 'India'),
     (1, 'United States'),
     (62, 'Indonesia'),
     (55, 'Brazil'),
     (92, 'Pakistan'),
     (880, 'Bangladesh'),
     (234, 'Nigeria'),
     (7, 'Russia'),
     (81, 'Japan'),
     ]
    
    
    dic= dict(DIAL_CODES)
    print(dic)
    dic= dict(sorted(DIAL_CODES))
    print(dic)
        
# Pasar de code points a bytes es encoding, lo contrario es decoding

if 1==-1:
    decoded="holá"
    encoded = decoded.encode("utf8")
    print(encoded)
    decoded= encoded.decode("utf8")
    print(decoded)

    
if 1==-1:  
    cafe = bytes('café', encoding="utf8")
    print(cafe)
    cafe2="café".encode("utf8")
    if cafe==cafe2:
        print("yes") # Son iguales
        
    print(cafe[:1]) # Trozos de bytes siguen siendo bytes
    
    array=bytearray(cafe)
    print(array)
    print(array[3:]) # Trozos de bytearrays siguen siendo bytearrays
   
if 1==-1:
    
   x = '31 4B CE A9'
   print(bytes.fromhex(x)) # Devuelve un conjunto en forma de bytes a partir de un número hexagesimal o un conjunto de ellos


if 1==-1: # Obtener en forma de bytes un array

    from array import array as a
    
    x= a("h",[n for n in range(4)])
    oct=bytes(x)
    print(oct)

if 1==-1: # Obtener dimensiones de un GIF
    import struct
    fmt = '<3s3sHH' # formato
    with open('filter.gif', 'rb') as fp: # se le asigna a fp el comando del file (nombre del file, acción)
        img = memoryview(fp.read()) # Se crea un memoryview de la lectura del GIF
    
    header = img[:10] # Otro memoryview partiendo el primero
    bytes(header) # Se convierte en bytes
    
    struct.unpack(fmt, header) #Convertir el memoryview a una tupla con el tipo, la versión, la altura y la anchura
    
    del header 
    del img #Eliminar los memoyviews para descargar las memorias


if 1==-1:

    city = 'São Paulo' # No todos los codecs pueden codificar todos los carácteres, por ejemplo, el codec cp437 no puede codificar la virgulilla, si pueden utf8, utf16 e iso8859_1, así que podemos hacer lo siguiente:
    
    city.encode('cp437') # Tal cual, da fallo
    
    city.encode('cp437', errors='ignore') # Ignorar errores, pasa al siguiente carácter
    
    city.encode('cp437', errors='replace') # Reemplazar errores, lo reemplaza con '?'
    
    city.encode('cp437', errors='xmlcharrefreplace') # Lo reemplaza con una entidad XML
    
    
    
if 1==-1: # Hay codecs como 'cp1252', 'iso8859_1', y 'koi8_r' que son capaces de decodificar cualquier cadena de bytes sin errores

    octets = b'Montr\xe9al'
    print(octets.decode('cp1252')) # Del latín, por lo que traduce perfectamente
    print(octets.decode('iso8859_1')) # Destinado al griego, lo malinterpreta pero no emite error
    print(octets.decode('koi8_r')) # Es para ruso, por eso sustituye erróneamente la letra pero sin mostrar errores
    print(octets.decode('utf8')) # Error


if 1==-1: # Al guardar el txt especificamos el codec como utf-8, en lugar del default Windows 1252, por lo que para abrirlo debemos de especificar utf-8 otra vez
   
    fp=open('cafe.txt', 'w', encoding='utf8')
    fp.write('café')
    fp.close()
    fp2=open('cafe.txt','r',encoding=("utf8")).read()
    print(fp2)


if 1==-1:

    fp = open('cafe.txt', 'w', encoding='utf_8')
    fp.write('café')
    fp.close() # Creamos un archivo con codec utf-8, escribimos café y lo cerramos
    
    import os
    print(os.stat('cafe.txt').st_size) # El os.stat().st_size nos indica un tamaño de 5 bytes
    
    fp2 = open('cafe.txt')
    print(fp2)
    fp2.encoding 
    print(fp2.read()) # El primer intento se hace sin especificar codec, automaticamente se usará cp1252, pero vemos que al ser erróneo, no lo decodifica correctamente
    
    fp3 = open('cafe.txt', encoding='utf_8') 
    print(fp3)
    print(fp3.read()) # Ahora especificamos utf-8 como codec y al ser efectivamente el codec del archivo, lo decodifica bien
    
    fp4 = open('cafe.txt', 'rb') 
    print(fp4)
    print(fp4.read()) # Se abre como binario
    

if 1==-1:
    import sys, locale
    
    expressions = """
     locale.getpreferredencoding()
     type(my_file)
     my_file.encoding
     sys.stdout.isatty()
     sys.stdout.encoding
     sys.stdin.isatty()
     sys.stdin.encoding
     sys.stderr.isatty()
     sys.stderr.encoding
     sys.getdefaultencoding()
     sys.getfilesystemencoding()
     """
     
     # Por ejemplo, en locale.getpreferredencoding() la función evalue nos devolverá cp1252, ya que es el encode predefinido de windows 10, y en
     
    my_file = open('dummy', 'w')
    
    for e in expressions.split(): # Dividimos el array mediante los espacios
        
        value = eval(e) # El eval normalmente evalua lo que haya dentro del paréntesis. Y en sys.stdout.encoding devolverá UTF-8 ya que es el encode de la consola.
        print(e.rjust(30), '->' , repr(value))
    


if 1==-1:   
    s1 = 'café'
    s2 = 'cafe\u0301'
    # las expresiones s1 y s2 son canónicamente equivalente, pero no analíticamente equivalentes por error de python, por lo que su longitud será desigual y en la igualdad aparecerá un "no"
    print(s1, s2)
    print(len(s1), len(s2))
    
    if s1 == s2:
        print("yes")
    else:
        print("no")
    
  

if 1==-1: # Podemos arreglar el error de arriva por medi de la normalización Unicode. La forma NFC comprime al máximo los coe points, mientras que la NFD los expande.
    
    from unicodedata import normalize
    
    s1 = 'café'
    s2 = 'cafe\u0301'
    s1NFC= normalize("NFC",s1)
    print(s1NFC)
    print(len(s1NFC))
    s2NFC= normalize("NFC",s2)
    print(s2NFC)
    print(len(s2NFC))
    s1NFD= normalize("NFD",s1)
    print(s1NFD)
    print(len(s1NFD))
    s2NFD= normalize("NFD",s2)
    print(s2NFD)
    print(len(s2NFD))
        
    # Podemos ver que todos devuelven la misma palabra, que ambos NFT tienes la misma len y que sucede lo mismo con los NFD, sin embargo si comparamos NFT con NFD vemos que los NFD miden más, tal y como se podía predecir.
        
    if s1NFC==s2NFC and s1NFD==s2NFD:
        print("works") # efectivamente funciona tal y cómo pensábamos
        


if 1==-1:
    
    from unicodedata import normalize, name
    
    ohm = '\u2126'
    
    print(name(ohm)) # la función name te nombra el contenido de UN caracter
    
    ohm_c = normalize('NFC', ohm) # Normalizamos por medio de NFC
    print(name(ohm_c)) # Vemos que al normalizarlo la expresión cambia
    print(ohm == ohm_c) # Obviamente no es lo mismo ya que ohm_c está normalizado por NFC y ohm no
    print(normalize('NFC', ohm) == normalize('NFC', ohm_c)) # Una vez que normalizamos ambos por el mismo código (NFC) vemos que la igualdad se cumpple


if 1==-1: # Usando NFKC Y NFKD se hará una descomposición compatible de cada carácter.
    
    from unicodedata import normalize, name
    
    half = '½'
    print(normalize('NFKC', half)) # 1/2 no es un mal sustituto, así que estamos conformes en este caso
    
    four_squared = '4²'
    print(normalize('NFKC', four_squared)) # Aquí, sin embargo, 42 es un terrible sustituto de 4**2, con una aplicación podríamos almacenarlo de mjeor manera, pero la función normalize no conoce de formatos
    
    micro = 'µ'
    micro_kc = normalize('NFKC', micro)
    print(micro, micro_kc)
    
    print(ord(micro), ord(micro_kc))
    
    print(name(micro), name(micro_kc))



if 1==-1:  # El Case Folding consiste en, esencialmente, convertir todo a minúscula

    from unicodedata import normalize, name
    
    micro = 'µ' 
    print(name(micro)) # MICRO SIGN
    
    micro_cf = micro.casefold() #Lo convertimos a signo en minúsculas con el name.casefold()
    print(name(micro_cf)) # SMALL NU (minúsuclas)
    
    print(micro, micro_cf)
    
    eszett = 'ß'
    print(name(eszett))
    
    eszett_cf = eszett.casefold()
    print(eszett, eszett_cf)




if 1==-1: # El código está 100% hecho por mí, algo alejado del concepto del libro, pero basicamente normaliza el texto mediante NFD para que separe cada carácter incluidas las tildes y luego pasa por un filtrado.
    
    from unicodedata import normalize, combining
    
    def sin_tildes(txt):
        y=""
        x=normalize("NFD",txt)
        for w in x:
            if combining(w):
                pass
            else:
                y+=w
        return(normalize("NFC",y))
        
    print(sin_tildes("éý"))
            

if 1==-1: # Este es bastante similar al anterior utilizando el concepto del libro

    import unicodedata
    import string
    
    def shave_marks_latin(txt):
    
     norm_txt = unicodedata.normalize('NFD', txt) # Normalizamos con NFD
     latin_base = False
     keepers = []
     for c in norm_txt: 
         
         if unicodedata.combining(c) and latin_base:  # El combining sólo se activará en caso de tilde, y latin_base debe estar en true para que el if se pueda activar y omitir la tilde
             continue  # En caso de tilde inicia el siguiente caracter del bucle for
    
         if not unicodedata.combining(c): # Sólo se activará en caso de letra
             latin_base = c in string.ascii_letters # Si la letra se encuentra en ascii, latin_base cambia a True
             
         keepers.append(c) 
         
     shaved = ''.join(keepers)
     return unicodedata.normalize('NFC', shaved) 
    
    
    
    print(shave_marks_latin("éy"))


if 1==-1: # Básicamente lo pongo por si algún día me viene bien, le veo más bien poca aplicación a este tocho de código entendible pero sin sentido de existir.

    import unicodedata
    import string
    
    
    def shave_marks_latin(txt):
        
         norm_txt = unicodedata.normalize('NFD', txt) # Normalizamos con NFD
         latin_base = False
         keepers = []
         for c in norm_txt: 
             
             if unicodedata.combining(c) and latin_base:  # El combining sólo se activará en caso de tilde, y latin_base debe estar en true para que el if se pueda activar y omitir la tilde
                 continue  # En caso de tilde inicia el siguiente caracter del bucle for
        
             if not unicodedata.combining(c): # Sólo se activará en caso de letra
                 latin_base = c in string.ascii_letters # Si la letra se encuentra en ascii, latin_base cambia a True
                 
             keepers.append(c) 
             
         shaved = ''.join(keepers)
         return unicodedata.normalize('NFC', shaved)
     
        
    def dewinize(txt):
     
     single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""", """'f"*^<''""---~>""")
     
     multi_map = str.maketrans({ 
     '€': '<euro>',
     '…': '...',
     'Œ': 'OE',
     '™': '(TM)',
     'œ': 'oe',
     '‰': '<per mille>',
     '‡': '**',
    })
     
     multi_map.update(single_map)
     return txt.translate(multi_map) 
    
    def asciize(txt):
     no_marks = shave_marks_latin(dewinize(txt)) 
     no_marks = no_marks.replace('ß', 'ss') 
     return unicodedata.normalize('NFKC', no_marks)
    
    
    order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
    
    print(asciize(order)) # asciize applies dewinize, drops diacritics, and replaces the 'ß'.
    print(dewinize(order)) # dewinize replaces curly quotes, bullets, and ™ (trademark symbol).
    
if 1==-1: # Para ordenar texto no ASCII en python se suele utilizar el locale.strxfrm

    import locale
    
    fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
    sorted_fruits = sorted(fruits, key=locale.strxfrm)
    print(sorted_fruits)


if 1==-1:
    import pyuca
    
    fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
    print(sorted(fruits, key=pyuca.Collator().sort_key)) # La key pyuca.Collator().sort_key es una manera UniCode de ordenar un array


if 1==-1: # No tengo ni la más mínima idea de lo que hacen la mitad de las funciones de este código, pero no me sobra el tiempo
    import unicodedata
    import re
    re_digit = re.compile(r'\d')
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
    for char in sample:
     print('U+%04x' % ord(char), 
     char.center(6), 
     're_dig' if re_digit.match(char) else '-', 
     'isdig' if char.isdigit() else '-', 
     'isnum' if char.isnumeric() else '-', 
     format(unicodedata.numeric(char), '5.2f'), 
     unicodedata.name(char), 
     sep='\t')


if 1==-1: # Más de lo mismo, puede que algún día vuelva a este archivo para entender este código si es imprescindible, pero todo indica a que no.
    import re
    re_numbers_str = re.compile(r'\d+') 
    re_words_str = re.compile(r'\w+')
    re_numbers_bytes = re.compile(rb'\d+') 
    re_words_bytes = re.compile(rb'\w+')
    text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef" 
     " as 1729 = 1³ + 12³ = 9³ + 10³.") 
    text_bytes = text_str.encode('utf_8') 
    print('Text', repr(text_str), sep='\n ')
    print('Numbers')
    print(' str :', re_numbers_str.findall(text_str)) 
    print(' bytes:', re_numbers_bytes.findall(text_bytes)) 
    print('Words')
    print(' str :', re_words_str.findall(text_str)) 
    print(' bytes:', re_words_bytes.findall(text_bytes))


if 1==-1:
    
    import os
    print(os.listdir(r'D:\Steam\steamapps\common\assettocorsa\content')) # Abrir la dirección que quieras    
