# prog_za_for
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

Svaki sub skripta prima 2 argumenta arg1 i arg2

Generalno:

```shell
sub_script.py arg1 arg2
```

Oba argumenta su u string formatu

arg1 - da li kod pokretanja radi ili ne radi report file, stanja su: **[doreport|noreport]**
arg2 - kako se zove report file (npr. report_port_scan.txt)


Primjer poziva sa argumentima:

```shell
port_scan.py doreport report_port_scan.txt
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
