# Test dan Debug

Bila anda ingin mengetes bot dan membantu untuk men-debug bot, install requirements yang ditampilkan pada requirements.txt dengan pip atau conda, dapatkan token anda dari situs Discord Developer dan tulis sebagai parameter pada client.run() di file main.

## Linux
Untuk linux, Change directory ke [bin/binary directory](unionchan/bin) dengan:
```
$ cd union-chan/unionchan/bin
```
Kemudian run [debug.sh](unionchan/bin/debug.sh) dengan:
```
$ sh debug.sh
```
Tolong dicatat bahwa [debug.sh](unionchan/bin/debug.sh) membutuhkan channel spesifik untuk men-debug. Anda dapat menambahkan channel spesifik tersebut di file [main](unionchan/main.py). Cari variabel `debugChannel`, copy id channel discord anda dengan klik kanan pada channel discord kemudian Copy Id, dan paste disana. Tolong diingat untuk dipaste tidak dalam bentuk `string`. Bila anda tidak ingin mendebug, hanya mencoba saja, silahkan run:
```
$ sh start.sh
```
Start biasa ini tidak membutuhkan channel khusus, dan bot dapat berjalan di seluruh channel yang ada pada server, kecuali channel yang direstrict.

Bila anda telah menambahkan data baru dan ingin mengetrain modelnya kembali, silahkan run [train.sh](unionchan/bin/train.sh) dengan:
```
$ sh train.sh
```