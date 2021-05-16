import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "darties.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import sqlite3
from products.models import Product

def add_villes() :
     
    id_ville|lib_ville|lib_continent|lib_pays|lib_departement|lib_reg_anc|lib_reg_nouv
    v = Ville.objects.create(title='my title', price=25)


    v.save()








def show_tables():
    
    conn = sqlite3.connect('developpers.db')
    c = conn.cursor()

    c.execute("SELECT * FROM developpers WHERE first_name = 'alessio';" )
    results = c.fetchall()
    print(results)


    c.execute("SELECT * FROM technos;" )
    results = c.fetchall()
    print(results)

    conn.commit()
    conn.close()







if __name__ == "__main__":


    print('ok')
    add_villes()