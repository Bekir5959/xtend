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

### 1. Görsel Açma

- "File" menüsüne tıklayın ve "Open" seçeneğine tıklayın.
- Resim dosyasını seçmek için dosya açma penceresi açılacaktır. Desteklenen formatlar arasında `.png`, `.jpg`, `.bmp`, `.gif`, ve `.xtend` bulunmaktadır.
- `.xtend` dosyasını açmak isterseniz, program bu dosyayı çözerek içindeki görseli görüntüleyecektir.

### 2. Görseli Kaydetme

- Görseli `.xtend` formatında kaydetmek için "File" menüsünde "Save as .xtend" seçeneğini tıklayın.
- Dosya kaydetme penceresi açılacak ve kaydedilecek yer ve dosya adı seçilecektir.
- Kaydederken, program WebP formatında kaydedilen resmi şifreleyip sıkıştırarak `.xtend` formatına dönüştürecektir.

### 3. Görseli Görüntüleme

- Yüklediğiniz resimler ekranın merkezinde görüntülenir.
- Görselin çözünürlüğü, son değiştirilme tarihi ve dosya boyutu gibi bilgiler alt kısımda gösterilecektir.

### 4. Hakkında Bilgi

- "Help" menüsünde yer alan "About" seçeneğine tıklayarak program hakkında bilgi alabilirsiniz.
- Bu bölümde XTEND Project'in geliştiricisi ve lisans bilgileri yer almaktadır.

### 5. Görselde Gezinti

- Görseli kaydırmak için farenizin orta tuşunu veya kaydırma çubuğunu kullanabilirsiniz.
- Görseli yakınlaştırmak veya uzaklaştırmak için fare tekerleği ile veya `Ctrl` tuşuna basılı tutarak tekerleği döndürebilirsiniz.

### 6. Zoom (Yakınlaştırma/Uzaklaştırma)

- Görseli yakınlaştırmak için `Ctrl` tuşuna basılı tutup fare tekerleğini yukarıya kaydırın.
- Görseli uzaklaştırmak için `Ctrl` tuşuna basılı tutup fare tekerleğini aşağıya kaydırın.
- Alternatif olarak, `Shift` tuşu ile birlikte fare tekerleğini kullanarak yakınlaştırma ve uzaklaştırma yapabilirsiniz.

## XTEND Dosya Formatı

- `.xtend` dosyası, WebP formatında kaydedilmiş bir görselin XOR şifrelemesi ile güvenli hale getirilmiş ve Brotli algoritması ile sıkıştırılmış halidir.
- Bu dosyalar, görselin içeriğini güvenli bir şekilde saklamak için tasarlanmıştır.
- Kullanıcılar, `.xtend` dosyasını çözmek ve görseli görüntülemek için programı kullanabilirler.

## Yöntemler ve Fonksiyonlar

### XOR Şifreleme

Program, XOR şifrelemesi ile veriyi güvenli hale getirir. Bu şifreleme işlemi, görsel dosyasının her baytını bir anahtar (varsayılan olarak 0xAA) ile XOR işlemine tabi tutarak şifreler. Şifreleme ve çözme işlemi aynıdır, yani şifrelenmiş veriyi aynı anahtarla tekrar şifrelediğinizde orijinal veriye ulaşabilirsiniz.

### WebP Formatı

Görseller, şeffaflık (alfa kanalını) destekleyen WebP formatında kaydedilir. WebP, düşük dosya boyutlarıyla yüksek kaliteli görseller sunan bir formattır.

### Brotli Sıkıştırma

Görsel verisi, Brotli algoritması ile sıkıştırılır. Brotli, veriyi yüksek oranda sıkıştırarak dosya boyutunu küçültür, böylece görselin aktarılması ve saklanması daha verimli hale gelir.

## Notlar

- Programda geçici dosyalar kullanılır. Herhangi bir işlem sırasında geçici dosyalar oluşturulur ve işlem tamamlandığında bu dosyalar otomatik olarak temizlenir.
- Görsellerdeki herhangi bir değişiklik, `.xtend` dosyasına kaydedilmeden önce görüntülenebilir, düzenlenebilir ve kaydedilebilir.
- `.xtend` dosyaları sadece bu program ile açılabilir ve çözülüp görsel olarak işlenebilir.
- **Windows**: [XTEND APP](https://archive.org/download/xtend_file/app.exe) dosyasını indirin ve kurulum gerektirmeden çalıştırın.
