# Union-chan

Union-chan merupakan maskot dari [Union Project](https://unionproject.herokuapp.com). Bot ini merupakan implementasi pada Discord. Bot ini menggunakan [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing)

## Berkontribusi
### Windows
Bila anda merupakan pemula, dan anda memakai Sistem Operasi Windows, silahkan untuk mengunduh dan menginstall [Github Desktop](https://desktop.github.com/). Bila anda tidak menguasai bahasa Python, anda dapat berkontribusi pada data JSON yang berisi pola kalimat dan respon untuk bot ini [disini](https://github.com/34gang/union-chan/blob/master/unionchan/src/data/conversation.json). Fork repository ini, clone repository ini, kemudian edit di text editor favorit anda. Silahkan untuk menambahkan data dengan format yang sama dengan file tersebut. Berikutlah templatenya:
```json
{"tag": "salam",
         "patterns": ["Hai", "Apa kabar?", "Ada orang disana?", "Halo", "Yo", "Lagi apa", "Hai union chan"],
         "responses": ["Heyyyy", "Haloo", "Hai hai"],
         "context_set": ""
},
```
Jangan lupa untuk menghapus tanda koma di data paling akhir. Berikan commit message yang baik, dan ajukan pull request. Selengkapnya bisa anda lihat [disini](https://idratherbewriting.com/learnapidoc/pubapis_github_desktop_client.html)
### Linux
Bila anda menggunakan Linux, saya berasumsi bahwa anda pasti sudah berpengalaman dengan git. Jika tidak, silahkan fork repository ini, kemudian jalankan perintah berikut di terminal anda:

#### Debian/Ubuntu based
```
$ sudo apt-get install git
```
### RedHat/Fedora
```
$ sudo yum install git
```
### Arch/Manjaro
```
$ sudo pacman -S git
```
Kemudian untuk clone dan change directory:
```
$ git clone https://github.com/nama-anda/union-chan.git
$ cd /path/ke/directory
```
Kemudian tambahkan data, kode bila anda berpengalaman, atau apaun yang menurut anda dapat berguna. Setelah itu, jalankan:
```
$ git remote add origin https://github.com/nama-anda/union-chan.git
$ git remote add upstream https://github.com/34gang/union-chan.git
$ git add -A
$ git commit -m "Commit Message, usahakan agar anda membuatnya dengan baik"
$ git push origin master
```
Kemudian ajukan pull request.

## Test dan Debug
Untuk test dan debug, silahkan membaca panduan yang ada di folder [docs](docs)

## TODO:
- Menambah lebih, lebih banyak data
- Convert ke tensorflow 2 dan keras

## Lisensi
Bot ini berada dibawah lisensi [MIT](https://choosealicense.com/licenses/mit/)
