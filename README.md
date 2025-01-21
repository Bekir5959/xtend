# XTEND Project

XTEND, Bekir tarafından geliştirilen ve özgün dosya uzantısı `.xtend` ile sıkıştırılmış ve şifrelenmiş görselleri işlemek için kullanılan bir araçtır. Bu proje, görselleri WebP formatında kaydeder, XOR şifrelemesi ile güvenli hale getirir ve Brotli algoritması ile sıkıştırır. Kullanıcılar, `.xtend` dosyalarını açabilir, görselleri görüntüleyebilir, şifrelenmiş görselleri kaydedebilir ve çözebilirler.

## Özellikler

- **XOR Şifreleme**: Görselleri şifrelemek için XOR şifreleme kullanır.
- **WebP Formatı**: Görselleri kaydederken WebP formatını kullanır.
- **Brotli Sıkıştırma**: Veriyi sıkıştırmak için Brotli algoritmasını kullanır.
- **Görsel Görüntüleyici**: `.xtend` dosyalarını açabilir ve içindeki görselleri görüntüleyebilirsiniz.
- **Kapsamlı Menü**: Resimleri açma, kaydetme, ve "Hakkında" menüsünü içerir.
- **Geçici Dosya Yönetimi**: Uygulama çalışırken geçici dosyalar oluşturur ve siler.
- **Çift Yönlü Dönüşüm**: `.xtend` dosyasını görsel dosyasına dönüştürme ve görsel dosyasını `.xtend` formatına kaydetme.

## Kullanım

1. **Görsel Açma**: "Open" menüsünden resim dosyasını seçebilirsiniz.
2. **Görsel Kaydetme**: Görseli `.xtend` formatında kaydetmek için "Save as .xtend" seçeneğini kullanın.
3. **Görseli Görüntüleme**: Yüklediğiniz resimler ekranda gösterilecektir.
4. **Hakkında Bilgi**: "About" menüsünden proje hakkında bilgi alabilirsiniz.

## Kurulum

### Gereksinimler

Proje, aşağıdaki kütüphaneleri kullanır:

- Python 3.x
- `PyQt5`
- `Pillow` (PIL)
- `brotli`

### Kurulum Adımları

1. **Python 3.x'i yükleyin** (Eğer yüklemediyseniz).
2. **Gerekli kütüphaneleri yükleyin**:

```bash
pip install -r requirements.txt
