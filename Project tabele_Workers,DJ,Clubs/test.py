"""Konzolni interfejs (meni) koji koristi DAO klase iz dao.py."""
from dao import KlubDAO, ZaposleniDAO, RasporedDAO
from datetime import datetime

def input_date(prompt):
    s = input(prompt).strip()
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Neispravan format datuma. Očekuje se YYYY-MM-DD.")
        return None

def prikazi_klubove():
    klubovi = KlubDAO.list_all()
    print('\n📍 Klubovi:')
    for k in klubovi:
        print(f"ID: {k[0]} | {k[1]} | {k[2]}")

def prikazi_zaposlene():
    zaposleni = ZaposleniDAO.list_all()
    print('\n👥 Zaposleni:')
    for z in zaposleni:
        print(f"ID: {z[0]} | {z[1]} {z[2]} | {z[3]} | {z[4]}")

def prikazi_raspored():
    rasp = RasporedDAO.list_all()
    print('\n📅 Raspored:')
    for r in rasp:
        print(f"ID: {r[0]} | {r[1]} {r[2]} -> {r[3]} | {r[4]}")

def meni():
    while True:
        print('\n=== SISTEM ZA UPRAVLJANJE OSOBLJEM ===')
        print('1. ➕ Dodaj klub')
        print('2. 📋 Prikazi klubove')
        print('3. 👤 Dodaj zaposlenog')
        print('4. 👥 Prikazi zaposlene')
        print('5. ✏️ Azuriraj zaposlenog')
        print('6. ❌ Obrisi zaposlenog')
        print('7. 🗓️ Dodeli raspored')
        print('8. 📅 Prikazi raspored')
        print('9. ✏️ Azuriraj raspored')
        print('10. ❌ Obrisi raspored')
        print('0. 🚪 Izlaz')

        opt = input('\nIzaberi opciju: ').strip()
        if opt == '1':
            naziv = input('Naziv kluba: ')
            adresa = input('Adresa: ')
            KlubDAO.create(naziv, adresa)
            print('✅ Klub dodat.')
        elif opt == '2':
            prikazi_klubove()
        elif opt == '3':
            ime = input('Ime: ')
            prezime = input('Prezime: ')
            uloga = input('Uloga (konobar/DJ): ')
            kontakt = input('Kontakt: ')
            ZaposleniDAO.create(ime, prezime, uloga, kontakt)
            print('✅ Zaposleni dodat.')
        elif opt == '4':
            prikazi_zaposlene()
        elif opt == '5':
            prikazi_zaposlene()
            id_zap = int(input('ID zaposlenog za azuriranje: '))
            ime = input('Novo ime (ENTER preskoci): ')
            prezime = input('Novo prezime (ENTER preskoci): ')
            uloga = input('Nova uloga (ENTER preskoci): ')
            kontakt = input('Novi kontakt (ENTER preskoci): ')
            updates = {}
            if ime: updates['ime'] = ime
            if prezime: updates['prezime'] = prezime
            if uloga: updates['uloga'] = uloga
            if kontakt: updates['kontakt'] = kontakt
            changed = ZaposleniDAO.update(id_zap, **updates)
            print(f'✏️ Ažurirano {changed} redova.')
        elif opt == '6':
            prikazi_zaposlene()
            id_zap = int(input('ID zaposlenog za brisanje: '))
            ZaposleniDAO.delete(id_zap)
            print('❌ Zaposleni obrisan.')
        elif opt == '7':
            prikazi_zaposlene()
            id_zap = int(input('ID zaposlenog: '))
            prikazi_klubove()
            id_klub = int(input('ID kluba: '))
            datum = input_date('Datum (YYYY-MM-DD): ')
            if datum:
                RasporedDAO.create(id_zap, id_klub, datum)
                print('📅 Raspored dodeljen.')
        elif opt == '8':
            prikazi_raspored()
        elif opt == '9':
            prikazi_raspored()
            id_rasp = int(input('ID rasporeda za azuriranje: '))
            novi_klub = input('Novi ID kluba (ENTER preskoci): ')
            novi_datum = input('Novi datum YYYY-MM-DD (ENTER preskoci): ')
            updates = {}
            if novi_klub: updates['id_kluba'] = int(novi_klub)
            if novi_datum:
                try:
                    updates['datum'] = datetime.strptime(novi_datum, '%Y-%m-%d').date()
                except ValueError:
                    print('❌ Neispravan datum.')
            if updates:
                changed = RasporedDAO.update(id_rasp, **updates)
                print(f'✏️ Ažurirano {changed} redova.')
        elif opt == '10':
            prikazi_raspored()
            id_rasp = int(input('ID rasporeda za brisanje: '))
            RasporedDAO.delete(id_rasp)
            print('❌ Raspored obrisan.')
        elif opt == '0':
            print('👋 Izlaz iz programa.')
            break
        else:
            print('⚠️ Nepoznata opcija.')
