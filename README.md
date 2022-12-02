# Chess Tournament Project (Satranç Turnuvası Projesi)

**Amaç :** Swiss-System kurallarını referans alarak bir satranç turnuvası projesi geliştirmek.

**Girdi :** Yarışmacıların önceki yarışmalarda elde ettikleri skorlar.

**Çıktı :** En yüksek toplam puana sahip yarışmacı.

---

**Açıklama :**
- Veriler [Mockaroo](https://www.mockaroo.com/) kullanılarak rastgele bir şekilde oluşturulmuştur.
- İlk turda, yarışmacılar önceki yarışmalardan elde ettikleri skora göre eşleştirilir. 
- Yarışmacıların skorlarına galibiyet durumunda 1 puan, beraberlik durumunda 0.5 puan, kayıp durumunda 0 puan eklenir.
- Tek sayıda oyuncu varsa her turda bir oyuncu açıkta kalır ve o oyuncu 1 puan alır. Aksi durumda, her oyuncu her turda oynar.
- Renk tekrarını önlemek için 2.turdan itibaren taş rengi rastgele  seçilmiştir. 
- Her yarışmacı benzer bir skora sahip rakiple eşleştirilir. Örneğin, 2 puan skor aralığında başka oyuncu yoksa 1.5 puan skor aralığındaki birinci kişiyle eşleştirilir. Bu durumda da başka oyuncu yoksa  müsait olan bir sonraki aralıktaki birinci kişiyle eşleştirilir. 
- Her tur için maç eşleştirmesi bir önceki tur bittikten sonra yapılır ve maç sonuçlarına bağlıdır.
- Turnuvanın sonunda en yüksek puana sahip olan oyuncu kazanan oluyor. 
