import json

# Data Lengkap 12 Game Indie
games_data = [
    {
        "title": "ULTRAKILL",
        "release_date": "3 September 2020 (Early Access)",
        "publisher": "New Blood Interactive",
        "developer": "Arsi 'Hakita' Patala",
        "genre": "Action, FPS, Boomer Shooter",
        "synopsis": "Game FPS retro ultra-violet yang menggabungkan gaya penembak klasik dengan sistem penilaian berbasis kombo layaknya Devil May Cry. Karakter utama adalah robot yang menggunakan darah sebagai bahan bakar.",
        "rating": "Overwhelmingly Positive (98%)",
        "steam_url": "https://store.steampowered.com/app/1229490/ULTRAKILL/"
    },
    {
        "title": "Dead Cells",
        "release_date": "7 Agustus 2018",
        "publisher": "Motion Twin, Motion Twin",
        "developer": "Motion Twin, Evil Empire",
        "genre": "Rogue-lite, Metroidvania, Action",
        "synopsis": "Jelajahi kastil yang terus berubah dan luas dalam game aksi bergenre rogue-lite metroidvania ini. Hadapi musuh dalam pertarungan 2D yang brutal dan cepat menggunakan berbagai senjata dan sihir.",
        "rating": "Overwhelmingly Positive (97%)",
        "steam_url": "https://store.steampowered.com/app/588650/Dead_Cells/"
    },
    {
        "title": "Hyper Light Drifter",
        "release_date": "31 Maret 2016",
        "publisher": "Heart Machine",
        "developer": "Heart Machine",
        "genre": "Action RPG, Hack and Slash",
        "synopsis": "Sebuah RPG aksi petualangan 2D dengan gaya visual pixel-art 16-bit yang memukau. Pemain mengendalikan Drifter, seorang pengembara yang mengidap penyakit misterius, menjelajahi reruntuhan dunia kuno.",
        "rating": "Very Positive (4%)",
        "steam_url": "https://store.steampowered.com/app/257850/Hyper_Light_Drifter/"
    },
    {
        "title": "Celeste",
        "release_date": "25 Januari 2018",
        "publisher": "Extremely OK Games",
        "developer": "Maddy Makes Games",
        "genre": "Platformer, Precision Platformer",
        "synopsis": "Bantu Madeline bertahan hidup melawan iblis dalam dirinya saat dia melakukan perjalanan ke puncak Gunung Celeste. Sebuah game platformer presisi tinggi dengan narasi mendalam tentang kesehatan mental.",
        "rating": "Overwhelmingly Positive (97%)",
        "steam_url": "https://store.steampowered.com/app/504230/Celeste/"
    },
    {
        "title": "Hollow Knight",
        "release_date": "24 Februari 2017",
        "publisher": "Team Cherry",
        "developer": "Team Cherry",
        "genre": "Metroidvania, Action-Adventure",
        "synopsis": "Pecahkan misteri di bawah kota kuno Dirtmouth yang runtuh. Jelajahi dunia bawah tanah yang luas, lawan makhluk-makhluk yang terinfeksi, dan bertemanlah dengan serangga aneh dalam gaya gambar tangan klasik.",
        "rating": "Overwhelmingly Positive (97%)",
        "steam_url": "https://store.steampowered.com/app/367520/Hollow_Knight/"
    },
    {
        "title": "Undertale",
        "release_date": "15 September 2015",
        "publisher": "tobyfox",
        "developer": "tobyfox",
        "genre": "RPG, Story Rich",
        "synopsis": "Sebuah game RPG unik di mana Anda mengendalikan seorang anak manusia yang jatuh ke bawah tanah penuh monster. Keunikan utamanya: Anda tidak harus membunuh siapapun untuk memenangkan game ini.",
        "rating": "Overwhelmingly Positive (96%)",
        "steam_url": "https://store.steampowered.com/app/391540/Undertale/"
    },
    {
        "title": "Deltarune",
        "release_date": "31 Oktober 2018 (Chapter 1)",
        "publisher": "tobyfox",
        "developer": "tobyfox",
        "genre": "RPG, Turn-Based",
        "synopsis": "Sekuel spiritual dari Undertale yang berlatar di dunia berbeda. Menampilkan sistem pertarungan tim, karakter baru yang ikonik seperti Kris, Susie, dan Ralsei, serta musik memukau gubahan Toby Fox.",
        "rating": "Overwhelmingly Positive (98%)",
        "steam_url": "https://store.steampowered.com/app/1671210/DELTARUNE/"
    },
    {
        "title": "Stardew Valley",
        "release_date": "26 Februari 2016",
        "publisher": "ConcernedApe",
        "developer": "ConcernedApe",
        "genre": "Farming Sim, RPG, Cozy",
        "synopsis": "Anda mewarisi sebidang tanah pertanian tua milik kakek Anda di Stardew Valley. Berbekal alat-alat bekas dan sedikit koin, mulailah kehidupan baru untuk mengelola ladang dan berbaur dengan warga kota.",
        "rating": "Overwhelmingly Positive (98%)",
        "steam_url": "https://store.steampowered.com/app/413150/Stardew_Valley/"
    },
    {
        "title": "Hades",
        "release_date": "17 September 2020",
        "publisher": "Supergiant Games",
        "developer": "Supergiant Games",
        "genre": "Rogue-like, Hack and Slash, Action",
        "synopsis": "Berperanlah sebagai Zagreus, pangeran abadi Underworld, yang mencoba mendobrak keluar dari cengkeraman dewa kematian (Hades). Game rogue-like legendaris dengan kombinasi aksi cepat dan cerita mitologi Yunani.",
        "rating": "Overwhelmingly Positive (98%)",
        "steam_url": "https://store.steampowered.com/app/1145360/Hades/"
    },
    {
        "title": "Shovel Knight: Treasure Trove",
        "release_date": "26 Juni 2014",
        "publisher": "Yacht Club Games",
        "developer": "Yacht Club Games",
        "genre": "Platformer, 2D, Retro",
        "synopsis": "Game petualangan aksi klasik menyapu dunia dengan gameplay yang luar biasa, karakter berkesan, dan estetika retro 8-bit. Berjuanglah demi cinta sejati menggunakan senjata andalan berupa sekop.",
        "rating": "Overwhelmingly Positive (95%)",
        "steam_url": "https://store.steampowered.com/app/250760/Shovel_Knight_Treasure_Trove/"
    },
    {
        "title": "Cuphead",
        "release_date": "29 September 2017",
        "publisher": "Studio MDHR Entertainment",
        "developer": "Studio MDHR Entertainment",
        "genre": "Run and Gun, Shoot 'Em Up, Hardcore",
        "synopsis": "Game aksi run-and-gun klasik yang berfokus pada pertarungan bos. Terinspirasi oleh kartun tahun 1930-an, visual dan audio dibuat secara manual dengan teknik zaman dulu (gambar tangan dan musik jazz original).",
        "rating": "Overwhelmingly Positive (96%)",
        "steam_url": "https://store.steampowered.com/app/268910/Cuphead/"
    },
    {
        "title": "Hotline Miami",
        "release_date": "23 Oktober 2012",
        "publisher": "Devolver Digital",
        "developer": "Dennaton Games",
        "genre": "Action, Top-Down Shooter, Action Game",
        "synopsis": "Game aksi top-down bersuasana tahun 1989 di Miami yang penuh dengan kebrutalan mentah, baku tembak keras, dan pertarungan jarak dekat. Didukung oleh soundtrack synthwave yang sangat adiktif.",
        "rating": "Overwhelmingly Positive (97%)",
        "steam_url": "https://store.steampowered.com/app/219150/Hotline_Miami/"
    }
]

# Template HTML dengan CSS Modern & Responsif
html_template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Katalog Game Indie Terbaik</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --accent-color: #38bdf8;
            --muted-text: #94a3b8;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
        }
        header h1 {
            color: var(--accent-color);
            margin-bottom: 5px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
        }
        .card {
            background-color: var(--card-bg);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border: 1px solid #334155;
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
            border-color: var(--accent-color);
        }
        .card-header h2 {
            margin-top: 0;
            font-size: 1.5rem;
            color: var(--accent-color);
        }
        .meta-info {
            font-size: 0.85rem;
            color: var(--muted-text);
            margin-bottom: 15px;
            line-height: 1.4;
        }
        .meta-info strong {
            color: var(--text-color);
        }
        .synopsis {
            font-size: 0.95rem;
            line-height: 1.5;
            margin-bottom: 20px;
            flex-grow: 1;
        }
        .rating {
            background-color: #0284c7;
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 0.85rem;
            display: inline-block;
            margin-bottom: 15px;
            font-weight: bold;
        }
        .steam-btn {
            display: block;
            text-align: center;
            background-color: #171a21;
            color: #fff;
            text-decoration: none;
            padding: 10px;
            border-radius: 6px;
            font-weight: bold;
            font-size: 0.9rem;
            transition: background-color 0.2s;
            border: 1px solid #66c0f4;
        }
        .steam-btn:hover {
            background-color: #66c0f4;
            color: #171a21;
        }
    </style>
</head>
<body>

    <header>
        <h1>Katalog Utama Game Indie</h1>
        <p>Daftar 12 game indie legendaris beserta detail lengkap dan link Steam resmi</p>
    </header>

    <div class="container">
        {game_cards}
    </div>

</body>
</html>
"""

# Proses pembuatan komponen kartu game
cards_html = ""
for game in games_data:
    cards_html += f"""
        <div class="card">
            <div class="card-header">
                <h2>{game['title']}</h2>
                <div class="meta-info">
                    <strong>Rilis:</strong> {game['release_date']}<br>
                    <strong>Genre:</strong> {game['genre']}<br>
                    <strong>Pengembang:</strong> {game['developer']}<br>
                    <strong>Penerbit:</strong> {game['publisher']}
                </div>
                <p class="synopsis">{game['synopsis']}</p>
            </div>
            <div>
                <div class="rating">⭐ {game['rating']}</div>
                <a href="{game['steam_url']}" target="_blank" class="steam-btn">Lihat di Steam</a>
            </div>
        </div>
    """

# Satukan data ke template utama dan simpan menjadi index.html
final_html = html_template.format(game_cards=cards_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Katalog index.html berhasil dibuat!")
