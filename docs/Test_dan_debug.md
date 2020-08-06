# Test dan Debug

Bila anda ingin mengetes bot dan membantu untuk men-debug bot, install requirements yang ditampilkan pada requirements.txt dengan pip atau conda, dapatkan token anda dari situs Discord Developer dan tulis sebagai parameter pada client.run() di file main.

## Linux
Untuk Linux, change directory ke `union-chan/unionchan`, kemudian run:
```
$ python main.py --start
```
Jangan lupa untuk mengganti token dengan token milik anda.

Untuk men-debug, run:
```
$ python main.py --debug
```
Tolong diingat bahwa anda harus menyertakan debug channel agar Union-chan dapat berjalan dalam debug mode.

Bila anda ingin train Union-chan kembali, silahkan run change directory ke `union-chan/unionchan`kemudian run:
```
$ python train.py
```
Untuk mengetes secara local, change directory juga ke tempat yang sama dengan train, kemudian run:
```
$ python runlocal.py
```

## Windows
Untuk windows, anda harus memiliki python terlebih dahulu. Bila anda belum menginstal python, silahkan download dari [sini](https://python.org) Change directory ke `union-chan\unionchan`secara langsung, kemudian run:
```
D:\union-chan\unionchan> python main.py --start
```
Tolong diingat bahwa anda harus change directory ke path dimana anda meletakkan folder union-chan. Bila anda ingin men-debug, silahkan tambahkan argumen berikut:
```
D:\union-chan\unionchan> python main.py --debug
``` 
Dan bila anda ingin melatih kembali model, silahkan change directory ke `union-chan\unionchan kemudian run:
```
D:\union-chan\unionchan> python train.py
```
Bila anda ingin men-debug secara local, tidak dalam discord, melainkan dalam command prompt, run:
```
D:\union-chan\unionchan> python runlocal.py
```