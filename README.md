# Aplikacija za testiranja sigurnosti embedded uređaja
Programiranje za forenziku, projekt.

**TODO** Moramo se dogovoriti kako cemo nazvati projekt

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

Generalno:

```python
import sub_script
sub_script.sub_function(arg1, arg2, arg3)
```

Oba argumenta su u string formatu

 - *arg1* - da li kod pokretanja radi ili ne radi report file, stanja su: **[doreport|noreport]**
 - *arg2* - kako se zove report file (npr. report_port_scan.txt)
 - *arg3* - target IP

Primjer poziva sa argumentima:

```shell
port_scan.py doreport report_port_scan.txt 192.168.1.71
```

## Report datoteka

Svaka podskripta generira `.txt` UTF-8 report koji ce poslje jedna funkcija objediniti u zajednicki `.txt`.

Primjer generiranog report filea:

```report_port_scan.txt
---------------
 Scanned ports
---------------
22/tcp ssh
443/tcp
5123/udp
```

**NAPOMENA** Samo se ubaci neko zaglavlje u `.txt` a ostalo se napravi da se ispis iz neke komande npr. `nmap` redirekta u report file
