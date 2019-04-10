# Wahlmodul: Internet of Things (IoT)

_Vorlesung zum fachwissenschaftlichen Modul **Internet of Things** im [Bachelorstudiengang Informatik](https://www.th-rosenheim.de/technik/informatik-mathematik/) an der [Hochschule Rosenheim](https://www.th-rosenheim.de)._				

## Organisatorisches

**Vorlesungstermin**: Donnerstag, 08:00 - 11:15; Raum B0.11


**Kommunikation**: via [Mattermost](https://inf-mattermost.fh-rosenheim.de/inf-iot/channels/town-square) ([einschreiben](https://inf-mattermost.fh-rosenheim.de/signup_user_complete/?id=beamxgitujyyika1h8bx5rzuje))

## Leistungsnachweis

- **PStA** : Die Projektarbeit wird im Rahmen der Übung durchgeführt. Abschlusspräsentation ist am 04. Juli (letzter Vorlesungstermin!)

## Empfohlene Literatur

- Perry Lea:  [Internet of Things for Architects: Architecting IoT solutions by implementing sensors, communication infrastructure, edge computing, analytics, and security](https://www.amazon.de/Internet-Things-Architects-communication-infrastructure/dp/1788470591/) (Englisch Edition)

- Andrew Minteer: [Analytics for the Internet of Things (IoT): Intelligent analytics for your intelligent devices](https://www.amazon.de/Analytics-Internet-Things-IoT-Intelligent/dp/1787120732/) (Englisch Edition)

## Inhalt

- **21. März: Einführung in das Internet der Dinge** ([Skript](/assets/00-einfuehrung/00-Einfuehrung.pdf), [Übung](https://github.com/hsro-inf-iot/00_uebung))

	Wir starten diese Vorlesung ganz klassisch. Zunächst klären wir alles Organisatorische, vor allem wie das PStA ablaufen wird. Danach geht es mit einen Überblick und Scope der Vorlesung weiter. Gerne erzähle ich etwas zur Geschichte vom Internet der Dinge (Internet of Things; IoT). Möchte gerne motivieren, warum das Internet der Dinge so hip ist, welche Beziehungen zum Industrial IoT oder auch zur Industrie 4.0 bestehen. Danach schauen wir uns im Detail ein paar Szenarien aus verschiedenen Bereichen an.

     In der Übung schauen wir, ob Azure-Cloud Zugriffe funktionieren. 

- **28. März: IoT Architekturen** ([Skript](/assets/01-vorlesung/01-Vorlesung.pdf), [Übung](https://github.com/hsro-inf-iot/01_uebung))

     Hier steigen wir nun ein in das Thema IoT. Wie ist IoT überhaupt definiert? Welche Elemente von IoT gibt es? Welche IoT Topologien  (Edge/Fog/Cloud) gibt es und wie genau unterscheiden sich diese?

     In der Übung werden wir versuchen ein IoT Entwickler Board ([MXChip](https://microsoft.github.io/azure-iot-developer-kit/)) zu verbinden.

- **4. April: Things und  Sensoren** ([Skript](/assets/02-vorlesung/02-Vorlesung.pdf), [Übung](https://github.com/hsro-inf-iot/01_uebung))

     Nachdem wir sehr high-level IoT Architekturen und Topologien betrachtet haben, tauchen wir hier tiefer in die Themen _Things_ (Dinge) und Sensoren ein. Dazu versuchen eine Kategorisierung zu erstellen.
     

     Als Übung beschäftigen wir uns nochmal mit der Übung aus der Vorwoche.

- **11. April: From Device to Cloud** ([Skript](/assets/03-vorlesung/03-Vorlesung.pdf), [Übung](https://github.com/hsro-inf-iot/03_uebung))

     Wir schauen darauf, wie Things kommunizieren und welche Protokolle es gibt, z.B. Bluetooth, BLE, ZigBee,6LowPan, LORA. Ausserdem schauen wir uns an, wie via IP/TCP Verbindungen vom Ding mit der Cloud kommuniziert werden kann, z.B. HTTP/ Rest, MQTT und CoAP.

     Wenn Zeit bleibt, müssen wir uns auch etwas mit dem Thema _Security_ beschäftigen.

     In der Übung lassen wir unseren MXChip mal via MQTT mit einem anderen Service kommunizieren.

- **18. April: Vorlesungsfrei - Ostern**

- **25. April: IoT Analytics** ([Skript], [Übung])

     Nachdem Oster-Break geht es im nächsten Block Richtung Analyse von Daten. Denn IoT ist schließlich mehr als nur Dinge, die verbunden sind. Denn was nützen uns die Dinge, wenn wir mit den Daten nichts machen. Also müssen wir uns dem Themen Big Data, Data Storage und Datenverarbeitung Konzepten beschäftigen.

     In der Übung arbeiten mit den Daten, die uns unser MXChip liefert.

- **02. Mai: Big Data in IoT** ([Skript], [Übung])

     Wir schauen mal das Thema Big Data etwas genauer an. Es sollte jeder verstehen, was _Map-and-Reduce_ ist. In diesem Zusammenhang betrachten wir auch Data Ingest, Lamda Architekturen und Stream Processing.

     In der Übung schauen wir, dass wir Hadoop und Spark verwenden können und erwecken ein _Map-and-Reduce_ Job zum Leben. Ach ja, und natürlich werden wir auf Azure einen Stream-Analytics Job implementieren und instanzieren.

- **09. Mai: Data Exploration** ([Skript], [Übung])

     Nachdem wir nun gelernt haben, welche Möglichkeiten wir zum Verarbeiten von großen Datenmengen haben. Bietet es sich an, zu verstehen, wonach man in den Daten überhaupt sucht und was man erkennen kann (z.B. Muster, Anomalien, etc). Also Data Exploration und Visualisierung wird ein Thema sein. Ebenso Dashboard BI und Time Series Daten.

     In der Übung werden wir mal wieder den MXChip herannehmen und damit arbeiten.

- **16. Mai: IoT Platformen** ([Skript], [Übung])

     Wir starten diese Vorlesung mit einen Überblick über existierende IoT Cloud Platformen.
     Im 2. Teil der Vorlesung beschäftigen wir uns mit dem Design einer IoT Lösung. Hierzu nehmen wir exemplarisch Anforderungen auf und entwerfen eine IoT Lösungs-Architektur.

     In der Übung würde ich gerne in Gruppenarbeit das Thema Anforderungen und Architektur angehen.

- **23. Mai: Entwicklung einer IoT Lösung** ([Skript], [Übung])

     Wir machen weiter mit der Entwicklung unserer IoT Lösung. In dem nächsten Schritt bauen wir eine Datenpipeline auf und schauen uns evtl. das Thema _Provisioning_ an.

     In der Übung geht es weiter mit der Gruppenarbeit.

- **30. Mai: Vorlesungsfrei; Christi Himmelfahrt**

- **05. Juni: Gastvortrag - Digitalisierung** ([Skript], [Übung])

     Die Idee ist, dass wir uns anschauen, was das Thema _Digitaliserung_ für Firmen bedeutet.

- **13. Juni: Data Science in IoT** ([Skript], [Übung])

     In dieser Vorlesung schauen wir uns die Daten mit der Data Science-Brille mal genauer an und wie wir die Analysieren und daraus lernen können, also: Maschinelles Lernen (ML) und relevante Themen, z.B. Feature Engineering, Missing Data, Metrics (ROC, Recall, …), Bias,.

     In der Übung nehmen wir uns Daten her und wenden darauf ein paar ML Ansätze an.

- **20. Juni: Vorlesungsfrei - Fronleichnam**

- **27. Juni: Intelligente Cloud und intelligente Edge** ([Skript], [Übung])

     In der Vorlesung werden wir uns ein weiteres relevantes Thema ansehen: Wie werden Analysen verteilt? Was soll in der Cloud laufen, was kann man auf die Edge packen?
     Natürlich kommen wir hier am Thema Docker nicht vorbei. Also machen wir ganz geschwind eine kurze Einführung in Docker.

     In der Übung machen wir ein bischen Docker und so.

- **04. Juli: PStA Abschlusspraesentationen**

     PStA Praesentationen.



## Interessante Links:

- [IoT Geschichte kurz erklärt](https://www.youtube.com/watch?v=PYH27AnSiUU)
