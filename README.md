# Oson Ulash bot

Telegram orqali fayllarni yuklab olish uchun bot.

Bu bot orqali siz o'z fayllaringizni obunachilaringiz bilan baham ko'rishingiz mumkin.

Nega bu botdan foydalanish kerak?

Chunki bu botda siz fayllaringizni yuklab olinishlar statistikasini ko'rishingiz mumkin. Yuklab olishlar sonini va muddatini belgilashingiz mumkin. Shaxsiy kanallaringizga majburiy obuna o'rnatishingiz mumkin.


## Features

- fayllarni yuklab olish uchun kanallarga majburiy obuna bo'lish
- statistika
- yuklab olish uchun cheklov qo'yish
- yuklab olish muddatini, sonini belgilash
- 2 GB gacha bo'lgan fayl, rasm, audio, video va boshqa fayllarni yuklab olish

## Deployment

clone repo

```bash
git clone https://github.com/mirmakhamat/easy-share-bot.git
cd easy-share-bot
```

create environment

```bash
python3 -m venv venv
source venv/bin/activate
```

install requirements

```bash
pip install -r requirements.txt
```

create `.env` file and add configurations like `example.env` file


migrate to database

```bash
python migrate.py
```

run

```bash
python main.py
```

## Contributing

Contributions are always welcome!