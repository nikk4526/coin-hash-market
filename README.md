# Key Switcher

**Key Switcher** — утилита для анализа повторного использования Bitcoin-адреса с разными публичными ключами.

## Зачем?

Некоторые адреса (особенно P2PKH) могут быть использованы с разными публичными ключами, что:
- Нарушает приватность
- Указывает на multisig или компрометацию ключа

## Использование

```bash
python key_switcher.py <bitcoin_address>
```

## Пример

```bash
python key_switcher.py 1BoatSLRHtKNngkdXEeobR76b53LETtpyT
```

## Выходные данные

- Количество уникальных публичных ключей
- Предупреждение, если ключ менялся

## Лицензия

MIT
