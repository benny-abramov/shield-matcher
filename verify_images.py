import urllib.request
import urllib.error
import sys

# All player photos from the game
player_photos = {
    'mbappe': 'Kylian_Mbappe_France_v_Senegal_16_June_2026-391_(cropped).jpg',
    'messi': 'Leo_Messi_Argentina_v_Egypt_7_July_2026-1.jpg',
    'haaland': 'Erling_Haaland_Morocco_v_Norway_7_June_2026-51.jpg',
    'bellingham': 'Jude_Bellingham_England_v_Ghana_23_June_2026-061_(cropped).jpg',
    'salah': 'Mohamed_Salah_Argentina_v_Egypt_7_July_2026-163_(cropped).jpg',
    'kane': 'Harry_Kane_England_v_Ghana_23_June_2026-024_(cropped).jpg',
    'vini': 'Vinícius_Júnior_Brazil_V_Morocco_13_June_2026-207_(cropped).jpg',
    'yamal': 'Lamine_Yamal_France_v_Spain_7.24.26-142.jpg',
    'ronaldo': 'Cristiano_Ronaldo_Croatia_v_Portugal_2_July_2026-075_(cropped).jpg',
    'saka': 'Bukayo_Saka_England_v_Ghana_23_June_2026-057_(cropped).jpg',
    'palmer': 'Cole_Palmer_2025_FIFA_Club_World_Cup_Final.jpg',
    'musiala': 'Jamal_Musiala_Ecuador_v_Germany_25_June_2026-174_(cropped).jpg',
    'dembele': 'Ousmane_Dembele_France_v_Senegal_16_June_2026-341_(cropped)_2.jpg',
    'debruyne': 'Kevin_De_Bruyne_USMNT_v_Belgium_Mar_28_2026-64_(cropped).jpg',
    'wirtz': 'Florian_Wirtz_2024.jpg',
    'lautaro': 'Edison_Ndreca_Inter_(cropped_Lautaro_Martínez)_(cropped_further).jpg',
    'pedri': 'Pedri_Argentina_v_Spain_19_July_2026-197_(cropped).jpg',
    'son': 'Son_Heung-min_-_2022_(52552243725)_(cropped).jpg',
    'neymar': 'Neymar_Junior_Brazil_V_Morocco_13_June_2026-40.jpg',
    'pulisic': 'Christian_Pulisic_USMNT_v_Belgium_Mar_28_2026-73_(cropped).jpg',
    # Legends
    'pele': 'Pele_con_brasil_(cropped).jpg',
    'beckham': 'David_Beckham_UNICEF_(cropped2).jpg',
    'zidane': 'Zinedine_Zidane_by_Tasnim_03.jpg',
    'ronaldinho': 'Ronaldinho_in_2019.jpg',
    'henry': 'Thierry_Henry_(51649035951)_(cropped).jpg',
    'maradona': 'Argentina_celebrando_copa_(cropped).jpg',
    'cruyff': 'Johan_Cruijff_(1974).jpg',
    'kaka': 'Kaká_visited_Stadium_St._Petersburg.jpg',
    'r9': '12.12.2025_–_Cerimônia_de_lançamento_do_SBT_News_-_54980664160_(cropped2).jpg',
    'pirlo': '20150616_-_Portugal_-_Italie_-_Genève_-_Andrea_Pirlo_(cropped).jpg',
    'rooney': 'Wayne_Rooney_(50121495731)_(cropped).jpg',
}

# Club logos
club_logos = {
    'rma': 'Real_Madrid_CF.svg',
    'bar': 'FC_Barcelona_crest.svg',
    'atm': 'Atletico_Madrid_2017_logo.svg',
    'mci': 'Manchester_City_FC_badge.svg',
    'mun': 'Manchester_United_FC_crest.svg',
    'liv': 'Liverpool_FC.svg',
    'ars': 'Arsenal_FC.svg',
    'che': 'Chelsea_FC.svg',
    'tot': 'Tottenham_Hotspur.svg',
    'eve': 'Everton_FC_logo.svg',
    'bay': 'FC_Bayern_München_logo_(2017).svg',
    'bvb': 'Borussia_Dortmund_logo.svg',
    'psg': 'Paris_Saint-Germain_F.C..svg',
    'mon': 'AS_Monaco_FC.svg',
    'bor': 'Logo_des_Girondins_de_Bordeaux.svg',
    'juv': 'Juventus_FC_-_starlogo.svg',
    'int': 'Inter_Milan_2021.svg',
    'mil': 'Logo_of_AC_Milan.svg',
    'nap': 'SSC_Napoli_2024.svg',
    'rom': 'AS_Roma_Logo_2017.svg',
    'mia': 'Inter_Miami_CF_logo.svg',
    'lafc': 'Los_Angeles_FC.svg',
    'lag': 'LA_Galaxy_logo.svg',
    'cos': 'New_York_Cosmos_(2010).svg',
    'nsr': 'Al_Nassr_FC_logo.svg',
    'san': 'Santos_Logo.png',
    'spfc': 'Sao_Paulo_FC.svg',
    'ajx': 'AFC_Ajax.svg',
    'fey': 'Feyenoord_logo.svg',
    'psv': 'PSV_Eindhoven.svg',
    'boc': 'Boca_Juniors_logo18.svg',
    'riv': 'River_Plate_logo.svg',
}

def check_url(name, filename):
    from urllib.parse import quote
    url = f'https://commons.wikimedia.org/wiki/Special:FilePath/{quote(filename)}?width=200'
    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'ShieldMatcherBot/1.0')
        resp = urllib.request.urlopen(req, timeout=10)
        status = resp.getcode()
        final_url = resp.geturl()
        if status == 200:
            print(f'  OK    {name}: {filename}')
            return True
        else:
            print(f'  FAIL  {name}: {filename} -> HTTP {status}')
            return False
    except urllib.error.HTTPError as e:
        print(f'  FAIL  {name}: {filename} -> HTTP {e.code}')
        return False
    except Exception as e:
        print(f'  FAIL  {name}: {filename} -> {e}')
        return False

print("=== CHECKING PLAYER PHOTOS ===")
failed_players = []
for name, filename in player_photos.items():
    if not check_url(name, filename):
        failed_players.append(name)

print(f"\n=== CHECKING CLUB LOGOS ===")
failed_clubs = []
for name, filename in club_logos.items():
    if not check_url(name, filename):
        failed_clubs.append(name)

print(f"\n=== SUMMARY ===")
print(f"Players: {len(player_photos) - len(failed_players)}/{len(player_photos)} OK")
print(f"Clubs: {len(club_logos) - len(failed_clubs)}/{len(club_logos)} OK")
if failed_players:
    print(f"Failed players: {', '.join(failed_players)}")
if failed_clubs:
    print(f"Failed clubs: {', '.join(failed_clubs)}")
