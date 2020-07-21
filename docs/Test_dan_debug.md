# Test dan Debug

Bila anda ingin mengetes bot dan membantu untuk men-debug bot, install requirements yang ditampilkan pada requirements.txt dengan pip atau conda, dapatkan token anda dari situs Discord Developer dan tulis sebagai parameter pada client.run() di file main.

## Linux
Untuk linux, Change directory ke [bin/binary directory](../unionchan/bin) dengan:
```
$ cd union-chan/unionchan/bin
```
Kemudian run [debug.sh](../unionchan/bin/debug.sh) dengan:
```
$ sh debug.sh
```
Tolong dicatat bahwa [debug.sh](../unionchan/bin/debug.sh) membutuhkan channel spesifik untuk men-debug. Anda dapat menambahkan channel spesifik tersebut di file [main](unionchan/main.py). Cari variabel `debugChannel`, copy id channel discord anda dengan klik kanan pada channel discord kemudian Copy Id, dan paste disana. Tolong diingat untuk dipaste tidak dalam bentuk `string`. Bila anda tidak ingin mendebug, hanya mencoba saja, silahkan run:
```
$ sh start.sh
```
Start biasa ini tidak membutuhkan channel khusus, dan bot dapat berjalan di seluruh channel yang ada pada server, kecuali channel yang direstrict.

Bila anda telah menambahkan data baru dan ingin mengetrain modelnya kembali, silahkan run [train.sh](unionchan/bin/train.sh) dengan:
```
$ sh train.sh
```
Bila anda ingin men-debug atau mencoba secara local dalam terminal anda, cd ke [src](../unionchan/src) dan run:
```
$ python runlocal.py
```
## Windows
Untuk windows, anda harus memiliki python terlebih dahulu. Bila anda belum menginstal python, silahkan download dari [sini](https://python.org) Change directory ke [main file](../unionchan/main.py) secara langsung, kemudian run:
```
D:\union-chan\unionchan> python main.py --start
```
Tolong diingat bahwa anda harus change directory ke path dimana anda meletakkan folder union-chan. Bila anda ingin men-debug, silahkan tambahkan argumen berikut:
```
D:\union-chan\unionchan> python main.py --debug
``` 
Dan bila anda ingin melatih kembali model, silahkan change directory ke [source directory](../unionchan/src) kemudian run:
```
D:\union-chan\unionchan\src> python convertdata.py
```
Bila anda ingin men-debug secara local, tidak dalam discord, melainkan dalam command prompt, run:
```
D:\union-chan\unionchan\src> python runlocal.py
```