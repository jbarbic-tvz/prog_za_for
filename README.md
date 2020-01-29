# Aplikacija za testiranja sigurnosti embedded uređaja
Programiranje za forenziku, projekt.

## Struktura generalno

```shell
README
main.py
sub_1.py
report_sub_1.txt
sub_2.py
report_sub_2.txt
sub_3.py
report_sub_3.txt
full_report.txt
tester.log
```

## Sub skripta pravila

Svaki sub skripta prima 3 argumenta arg1, arg2 i arg3

Poziv funkcije generalno:

```python
import sub_script
sub_script.sub_function(arg1, arg2, arg3)
```

Oba argumenta su u string formatu

 - *arg1* - da li kod pokretanja radi ili ne radi report file, stanja su: **[doreport|noreport]**
 - *arg2* - kako se zove report file (npr. report_port_scan.txt)
 - *arg3* - target IP

Primjer poziva glavne funkcije:

```shell
sudo ./main.py
```

## Report datoteka

Svaka podskripta generira `.txt` UTF-8 report koji ce poslje jedna funkcija objediniti u zajednicki `.txt`.

Primjer generiranog report filea:

```report_port_scan.txt

Target IP address/hostname: 91.214.105.2
Port range - min: 1
Port range - max: 2000
threads: 200
=============================================
Scanning started in:  2020-01-29 10:29:45
=============================================
[*] Port 22 /ssh  is open
[*] Port 80 /http  is open
[*] Port 256  is open
[*] Port 259  is open
[*] Port 257  is open
[*] Port 262  is open
[*] Port 264  is open
[*] Port 443 /https  is open
[*] Port 500  is open
[*] Port 900  is open
[*] Port 1720  is open

```

**NAPOMENA** Samo se ubaci neko zaglavlje u `.txt` a ostalo se napravi da se ispis iz neke komande npr. `nmap` redirekta u report file
