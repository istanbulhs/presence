
AnyoneInTheHouse?
================

Wireless'a bağlı cihaz olup olmadığını kontrol eden basit bir betik.

Modem'e bağlanıp, istemcilerin listelendiği sayfayı çekiyor. Kaç tane istemci 
olduğunu sayıp onun sayısını dönüyor. Hata alırsa eksi bir sayı dönüyor. Bağlı 
istemci olmazsa 0 dönüyor. 

Geliştirmek isteyenler çektiğim html dosyasını şurdan bulabilirler: 
https://github.com/istanbulhs/AnyoneInTheHouse/blob/master/
AnyoneInTheHouseScript/test/data/wlstationlist.cmd


Bağlı Olduğu Kütüphaneler
-------------------------

* `Spyne <http://spyne.io>`_\. Yuklemek icin asagidaki dort komuttan begendiginizi
  kullanabilirsiniz: ::

    # pip install spyne
    $ easy_install --user spyne
    # easy_install spyne
    $ sudo easy_install spyne

* `Requests <http://python-requests.org>`_\. Yuklemek icin asagidaki dort komuttan
  begendiginizi kullanabilirsiniz: ::

    # pip install requests
    $ easy_install --user requests
    # easy_install requests
    $ sudo easy_install requests


Kurulum
-------

Gelistirici kurulumu: ::

      python setup.py develop --user

Kullanici / sunucu kurulumu: ::

      python setup.py install [--user]

Kullanımı
---------

SimpleHttpServer ile çalışıyor. Ayrıca bir sunucuya ihtiyaç duymuyor. Kurulumdan
sonra: ::

    anyone_daemon

komutuyla calistiriliyor.

Arkasından tarayıcıda: http://sunucu/kac-kisi

* Bağlı istemci varsa, sayısını dönüyor.
* Yoksa 0 dönüyor.
* Hata dönerse eksi bir sayı dönüyor.

Yapılabilecekler
----------------

* config parametreleri ayri bir dosyaya aktarılabilir
* Sürekli çalışıp çalışmadığını kontrol eden bir script yazılabilir.
* bootup'ta betiğin çalışması için linux'ta ne yapılması gerektiği yazılabilir.
  (ve bizim sunucuya da eklenebilir)
* test yazılabilir
